# Vectr

⚠️⚠️ UNDER CONSTRUCTION ⚠️⚠️
( Version 2.0 in the works currently -- expected Feb. 2025 )

**Vectr** is a Python-based tool designed to simplify stock option analysis. Built on the powerful `yfinance` module and supported by additional libraries such as `Flask`, `Pandas`, and `Plotly`, Vectr provides users with an intuitive interface for exploring and visualizing stock options data.  

### **🔑Key Features:**
- *Search Any Optionable Stock Ticker(s)*: Easily search for single or multiple stock & ETF tickers across the entire stock market. ("Optionable" stocks are those with available options for purchase.)

- *Dynamic Visualizations*: Generate interactive line graphs, bar graphs, and other visual enhancements to analyze options chains.

- *Market Insights*: Assess whether the market sentiment for a stock is bullish or bearish based on its options data.


------------


### **⚙️ How It Works:**

<details>
  <summary>... in a <b>Docker Container</b></summary>

  1. **Clone the Repository**:
     ```bash
     git clone https://github.com/NickRoccuzzo/Vectr
     cd Vectr
     ```

  2. **Build the Docker Image**:
     ```bash
     docker build -t vectr-app .
     ```

  3. **Run the Docker Container**:
     ```bash
     docker run -d -p 5000:5000 vectr-app
     ```

  4. **Access the Application**:
     - Open your browser and navigate to:
       ```
       http://127.0.0.1:5000
       ```

</details>

<details>
  <summary>... in a <b>Virtual Environment (venv)</b></summary>

  1. **Clone the Repository**:
     ```bash
     git clone https://github.com/NickRoccuzzo/Vectr
     cd Vectr
     ```

  2. **Create and Activate a Virtual Environment**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Linux/Mac
     .\venv\Scripts\activate   # On Windows
     ```

  3. **Install Dependencies**:
     ```bash
     pip install -r requirements.txt
     ```

  4. **Run the Flask Application**:
     ```bash
     python FlaskAppVectr.py
     ```

  5. **Access the Application**:
     - Open your browser and navigate to:
       ```
       http://127.0.0.1:5000
       ```

  6. **Deactivate the Virtual Environment (when done)**:
     ```bash
     deactivate
     ```

</details>

<details>
  <summary>... in an <b>IDE (e.g., PyCharm, VSCode)</b></summary>

  1. **Clone the Repository**:
     - Use your IDE's terminal or any terminal to clone the repository:
       ```bash
       git clone https://github.com/NickRoccuzzo/Vectr.git
       cd Vectr
       ```

  2. **Open the Project**:
     - Open the cloned directory as a project in your IDE (e.g., **File > Open** in PyCharm or VSCode).

  3. **Optional: Set Up a Virtual Environment**:
     - While not strictly required, it’s recommended to set up a virtual environment to keep dependencies isolated.
     - **In PyCharm**:
       - Go to **File > Settings > Project > Python Interpreter**.
       - Add a new virtual environment or point the interpreter to an existing one.
     - **In VSCode**:
       - Create a virtual environment in the terminal:
         ```bash
         python3 -m venv venv
         ```
       - Activate it:
         ```bash
         source venv/bin/activate  # On Linux/Mac
         .\venv\Scripts\activate   # On Windows
         ```

  4. **Install Dependencies**:
     - If your environment doesn’t already have the necessary packages, install them using:
       ```bash
       pip install -r requirements.txt
       ```

  5. **Run the Application**:
     - Open `FlaskAppVectr.py` in your IDE and click the **Run** button (or use the IDE’s shortcut to run the Python file).

  6. **Access the Application**:
     - Open your browser and navigate to:
       ```
       http://127.0.0.1:5000
       ```

</details>

------------


Once you've successfully completed the steps of your choice and access the web application, you will reach the home page:

![image](https://github.com/user-attachments/assets/64cb39dc-1022-40de-8c58-fa4e2738d34f)


From here, you can either search a singular ticker or multiple tickers.  
Tickers can be separated with commas, spaces, or both.  You can then hit 'Enter' or press the 'Search' button to extract the option chain data

![GitHubPicture2_Search_Tickers_Cont](https://github.com/user-attachments/assets/9a017fa5-f778-4841-97dc-97d072ea6e66)


Here's a sample of the option chain pulled for AAPL stock:
![image](https://github.com/user-attachments/assets/1bf826ca-b889-43fa-9852-6d15e89298a3)


... Along with a further breakdown of what data & insight the graphs will be providing to the end user:

(NOTE: You can hover over most data points on the graphs to gain further info)
![image](https://github.com/user-attachments/assets/081ed27e-ab4a-4a4a-8279-101ae1ba14a4)

------------

### 🔎 Data Visualizations and Insights
(Select any of the below to gain further information)

<details>
  <summary>🔹 <b>Current Stock Price Line</b></summary>

  - A bright blue horizontal line is plotted on the graph to represent the current price of the stock.
  - This helps users quickly see where the current price stands relative to the available options data.

</details>

<details>
  <summary>📊 <b>Bar Graphs for Open Interest (OI)</b></summary>

  - For each expiration date, the cumulative Open Interest (OI) for both **Call** and **Put** contracts are visualized with green & red bar graphs
  - Users can hover over any of the bars across the entire graph to see the # of OI for either **Calls** or **Puts** for a particular expiration date.
  - Outliers are immediately visible, drawing attention to expiration dates with an unusual amount of interest in one side or the other.

</details>

<details>
  <summary>📈 <b>Line Graphs for Highest Open Interest Contracts</b></summary>

  - Line graphs are plotted using the **specific Call & Put contracts with the highest Open Interest** at each expiration date.
  - These data points reflect the strike prices that the market considers **most significant**.
  - **For example:** If strike prices are $5, $10, $15, and $20, and the **$10** Call contract & **$5** Put contract have the highest Open Interest, those will be graphed as the key data points for that expiration date

</details>

<details>
  <summary>⚖️ <b>Weighted Average Line Graph</b></summary>

  - This graph provides an "average" line between the most active Call and Put for a given expiration date, weighted by Open Interest.
  - Strike prices with higher Open Interest have a greater impact on this line, giving users a clearer sense of market sentiment.
  - Example: If **100** Call contracts are bought at a $100 strike price, and **30** Put contracts are bought at a $50 strike price, the average line will slightly favor the Call options, resulting in the average line favoring an upward movement.

</details>

<details>
  <summary>🟩 <b>Dynamic Highlights for Key Data Points</b></summary>

  - Each data point with the highest Open Interest is marked with **dynamic squares** to catch the user's eye.
  - The larger the square is, the higher the Open Interest is for that particular strike.
  - These squares are dynamically sized in relation to the ***entire*** option chain.
  - These highlights make it easy to spot which contracts or expiration dates are experiencing significant market activity.

</details>

<details>
  <summary>🐂 <b>Net Call/Put Premium & Volume</b></summary>

  - Two annotations in the top-left corner of the Plotly graph display these aggregate values:
    - **Premium**: The total dollar amount spent across the option chain at the time of the query.
    - **Volume**: The total number of contracts purchased at the time of the query.
  - These metrics provide insights into the type of flow the chain is experiencing, helping users determine whether sentiment is more **bullish** or **bearish**.

</details>

By combining these elements, Vectr ensures users can effortlessly identify trends, analyze market sentiment, and focus on the most impactful data points.

------------

### Sectors of the S&P 500

If the user selects the **S&P 500 Sectors** hyperlink, they'll be taken to a page displaying the performance of various sectors within the S&P 500.

![image](https://github.com/user-attachments/assets/0e0f48b1-51ab-46bd-8f01-c82fca01c99a)

- **Default View**:
  - The displayed percentages initially represent the **1-day performance** for each sector.
  - This gives users a quick snapshot of the most recent market trends.

- **Customizable Timeframes**:
  - The user can select a different timeframe from the available options (e.g., 1-week, 1-month, 1-year, etc.) to analyze which sectors are **outperforming** or **underperforming** relative to others.
  - This feature provides flexibility to observe both short-term and long-term trends across the S&P 500 sectors.

![image](https://github.com/user-attachments/assets/eb1c45ff-5093-4427-96b9-d4e93de0f4c2)

- **ETF Holdings View**:
  - The user can also select any of the ETFs displayed as well to view the **Top 10 Holdings** of that particular ETF, along with the weighting of each holding:

![image](https://github.com/user-attachments/assets/de20ff7a-cb26-40ee-b3aa-79e5e348fc1e)


This interactive page offers a clear, concise view of market performance, helping users make more informed decisions based on sector trends.

------------
**⚠️ WARNING: NOT FINANCIAL ADVICE ⚠️**

Vectr is an ongoing project, and new features and improvements are regularly being added. Feedback is welcome as we continue to refine and enhance the application.
