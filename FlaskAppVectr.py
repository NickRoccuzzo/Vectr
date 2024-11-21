from flask import Flask, render_template, request, jsonify, make_response
from markupsafe import escape
import os
from VectrPyLogic import save_options_data, calculate_and_visualize_data
from sectors import get_etf_performance
import shutil
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

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
    etfs = ["XLRE", "XLE", "XLU", "XLK", "XLB", "XLP", "XLY", "XLI", "XLC", "XLV", "XLF"]
    performance = get_etf_performance(etfs)
    return render_template("SP500sectors.html", performance=performance)

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
    etfs = ["XLRE", "XLE", "XLU", "XLK", "XLB", "XLP", "XLY", "XLI", "XLC", "XLV", "XLF"]
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
