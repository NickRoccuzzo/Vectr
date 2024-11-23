import os
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def update_holdings(etfs=None):
    """Download and process holdings data for a list of ETFs."""
    # List of ETFs to process
    if etfs is None:
        etfs = ["XLRE", "XLE", "XLU", "XLK", "XLB",
                "XLP", "XLY", "XLI", "XLC", "XLV", "XLF", "XBI"]

    # Directory to save the cleaned files
    output_dir = "sectors"

    # Base URL for downloading holdings
    base_url = "https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-{}.xlsx"

    # Headers for the HTTP requests
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.ssga.com/us/en/intermediary/etfs/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def process_etf(etf):
        """Download and process a single ETF."""
        try:
            # Construct the download URL for the current ETF
            url = base_url.format(etf.lower())

            # Download the ETF holdings file
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Load the Excel file into pandas directly from memory
                df = pd.read_excel(response.content, skiprows=4)

                # Drop unnecessary columns
                columns_to_drop = ["Identifier", "SEDOL", "Sector", "Local Currency", "Shares Held"]
                df = df.drop(columns=columns_to_drop, errors="ignore")

                # Keep only the top 10 holdings
                df = df.head(10)

                # Format the 'Weight' column with two decimal places
                df["Weight"] = df["Weight"].apply(lambda x: round(x, 2))

                # Save the cleaned-up DataFrame to the output folder
                cleaned_file_path = os.path.join(output_dir, f"{etf}_holdings.xlsx")
                df.to_excel(cleaned_file_path, index=False)
                print(f"Data cleaned and saved to {cleaned_file_path}.")
            else:
                print(f"Failed to download {etf} holdings. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error processing {etf}: {e}")

    # Use ThreadPoolExecutor to run tasks concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(process_etf, etfs)

    print("All tasks completed.")

# Ensure the script can still be run directly
if __name__ == "__main__":
    update_holdings()
