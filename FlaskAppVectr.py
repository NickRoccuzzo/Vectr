from flask import Flask, render_template, request, jsonify
from markupsafe import escape
import pandas as pd
import threading
import time
import os
from VectrPyLogic import save_options_data, calculate_and_visualize_data
from sectors import get_etf_performance
from holdings import update_holdings
import shutil
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

# Global variable to track the last update time
last_holdings_update = 0
holdings_update_interval = 24 * 60 * 60  # Update once every 24 hours

def update_holdings_background():
    """Run the holdings update in a background thread."""
    def run_update():
        update_holdings()
        global last_holdings_update
        last_holdings_update = time.time()
    thread = threading.Thread(target=run_update)
    thread.start()


# Apply security headers after every request
@app.after_request
def apply_security_headers(response):
    # Add X-Frame-Options header to prevent clickjacking
    response.headers['X-Frame-Options'] = 'DENY'
    # Add X-Content-Type-Options to prevent MIME-sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# S&P 500 Sectors Page
@app.route("/sp500sectors")
def sp500sectors():
    global last_holdings_update

    etfs = ["XLRE", "XLE", "XLU", "XLK", "XLB",
            "XLP", "XLY", "XLI", "XLC", "XLV", "XLF", "XBI"]

    # Check if holdings data needs to be updated
    current_time = time.time()
    if current_time - last_holdings_update > holdings_update_interval or not os.path.exists('sectors'):
        update_holdings_background()

    performance = get_etf_performance(etfs)

    # Initialize a dictionary to hold holdings data
    holdings_data = {}

    for etf in etfs:
        # Construct the file path for the holdings .xlsx file
        holdings_file = os.path.join('sectors', f"{etf}_holdings.xlsx")
        if os.path.exists(holdings_file):
            try:
                # Read the .xlsx file using pandas
                df = pd.read_excel(holdings_file)
                # Format the 'Weight' column with percentages
                df["Weight"] = df["Weight"].apply(lambda x: f"{x}%")
                # Convert the DataFrame to HTML with Bootstrap classes
                holdings_html = df.to_html(classes='table table-striped holdings-table', index=False)
                # Store the HTML in the holdings_data dictionary
                holdings_data[etf] = holdings_html
            except Exception as e:
                print(f"Error reading {holdings_file}: {e}")
                holdings_data[etf] = '<p>Error loading holdings data.</p>'
        else:
            holdings_data[etf] = '<p>Holdings data is being updated. Please refresh the page in a few moments.</p>'

    return render_template("SP500sectors.html", performance=performance, holdings_data=holdings_data)

@app.route("/get_performance")
def get_performance():
    etf = request.args.get("etf")
    timeframe = request.args.get("timeframe")
    etfs = [etf]
    performance = get_etf_performance(etfs)
    return jsonify({"performance": performance.get(etf, {}).get(timeframe, "N/A")})

@app.route("/get_performance_group")
def get_performance_group():
    timeframe = request.args.get("timeframe")
    etfs = ["XLRE", "XLE", "XLU", "XLK", "XLB", "XLP", "XLY", "XLI", "XLC", "XLV", "XLF", "XBI"]
    performance = get_etf_performance(etfs)
    result = {etf: {"performance": metrics.get(timeframe)} for etf, metrics in performance.items()}
    return jsonify(result)

# CONTACT PAGE
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

# GETTING STARTED PAGE
@app.route('/getting-started', methods=['GET'])
def getting_started():
    return render_template('getting_started.html')

# Process ticker for visualization
@app.route('/process_ticker', methods=['POST'])
def process_ticker():
    ticker = request.form.get('ticker', '').strip().upper()

    # Escape user input to prevent XSS
    ticker = escape(ticker)

    if not ticker:
        return jsonify({'error': 'No ticker provided'}), 400

    try:
        save_options_data(ticker)
        fig = calculate_and_visualize_data(ticker, width=1200, height=525)
        graph_json = json.dumps(fig, cls=PlotlyJSONEncoder)

        # Clean up the temporary data directories
        folder_path = os.path.join(os.getcwd(), ticker)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)

        return jsonify({'ticker': ticker, 'graph_json': graph_json})
    except Exception as e:
        error = f"An error occurred while processing {ticker}: {e}"
        print(error)
        return jsonify({'error': error}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
