from flask import Flask, render_template, request, jsonify, make_response
from markupsafe import escape
import os
from VectrPyLogic import save_options_data, calculate_and_visualize_data
import shutil
import json
from plotly.utils import PlotlyJSONEncoder

app = Flask(__name__)

# Define the path to the JSON file
JSON_PATH = os.path.join(os.getcwd(), 'OptionPlays.json')

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

# ABOUT PAGE
@app.route('/about', methods=['GET'])
def about():
    try:
        with open(JSON_PATH, 'r') as file:
            options_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        options_data = {}

    return render_template('about.html', options_data=options_data)

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

# Update data in OptionPlays.json
@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    ticker = data.get('ticker')
    field = data.get('field')
    new_value = data.get('value')

    try:
        # Load existing data from the JSON file
        with open(JSON_PATH, 'r') as file:
            options_data = json.load(file)

        # Update the specific field for the given ticker
        if ticker in options_data:
            options_data[ticker][field] = new_value

        # Save updated data back to the JSON file
        with open(JSON_PATH, 'w') as file:
            json.dump(options_data, file, indent=4)

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error updating data: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Add a new ticker to OptionPlays.json
@app.route('/add_ticker', methods=['POST'])
def add_ticker():
    data = request.json
    ticker = data.get('ticker')
    expiry = data.get('expiry')
    notes = data.get('notes')

    try:
        # Load existing data from the JSON file
        with open(JSON_PATH, 'r') as file:
            options_data = json.load(file)

        # Add the new ticker to the data
        options_data[ticker] = {
            "ticker": ticker,
            "expiry": expiry,
            "notes": notes
        }

        # Save updated data back to the JSON file
        with open(JSON_PATH, 'w') as file:
            json.dump(options_data, file, indent=4)

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error adding ticker: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Remove a ticker from OptionPlays.json
@app.route('/remove_ticker', methods=['POST'])
def remove_ticker():
    data = request.json
    ticker = data.get('ticker')

    try:
        # Load existing data from the JSON file
        with open(JSON_PATH, 'r') as file:
            options_data = json.load(file)

        # Remove the ticker from the data
        if ticker in options_data:
            del options_data[ticker]

            # Save updated data back to the JSON file
            with open(JSON_PATH, 'w') as file:
                json.dump(options_data, file, indent=4)

            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': 'Ticker not found'}), 404
    except Exception as e:
        print(f"Error removing ticker: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json

    try:
        # Save the received data to OptionPlays.json with the new structure
        with open(JSON_PATH, 'w') as file:
            json.dump(data, file, indent=4)

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error saving data: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
