# Vectr

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

![GitHubPicture1_Search_Tickers](https://github.com/user-attachments/assets/cd802404-624d-4f67-8fee-3f6cb3928ed8)

From here, you can either search a singular ticker or multiple tickers.  
Tickers can be separated with commas, spaces, or both.  You can then hit 'Enter' or press the 'Search' button to extract the option chain data

![GitHubPicture2_Search_Tickers_Cont](https://github.com/user-attachments/assets/9a017fa5-f778-4841-97dc-97d072ea6e66)


Here's a sample of the option chain pulled for AAPL stock:
![image](https://github.com/user-attachments/assets/1bf826ca-b889-43fa-9852-6d15e89298a3)


... Along with a further breakdown of what data & insight the graphs will be providing to the end user:

(NOTE: You can hover over most data points on the graphs to gain further info)
![image](https://github.com/user-attachments/assets/081ed27e-ab4a-4a4a-8279-101ae1ba14a4)

------------

### Data Visualizations and Insights

The Vectr platform provides a suite of dynamic and interactive visualizations to help users analyze stock options data effectively. Here's what the visualizations include:

- **💲 Current Price Line 💲**:
  - A bright blue horizontal line is plotted on the graph to represent the current price of the stock.
  - This helps users quickly see where the current price stands relative to the available options data.

- **📊 Bar Graphs for Open Interest (OI) 📊**:
  - Visualize the Open Interest (OI)—the number of contracts currently open for each strike price.
  - Users can hover over each bar to see the cumulative OI # of all **Call** or **Put** contracts for that particular expiration date.
  - Outliers are immediately visible, drawing attention to expiration dates with an unusual amount of interest in one side or the other.

- **📈 Line Graphs for Highest Open Interest Contracts 📉**:
  - Line graphs are plotted using the **specific Call & Put contracts with the highest Open Interest** at each expiration date.
  - These data points reflect the strike prices that the market considers **most significant**.
  - **For example:** If strike prices are $5, $10, $15, and $20, and the **$10** Call contract & **$5** Put contract have the highest Open Interest, those will be graphed as the key data points for that expiration.

- **⚖️ Weighted Average Line Graph ⚖️**:
  - This graph provides an "average" view of the market's activity, weighted by Open Interest.
  - Strike prices with higher Open Interest have a greater impact on this line, giving users a clearer sense of market sentiment.
  - Example: If 100 Call contracts are bought at a $100 strike price, and 30 Put contracts are bought at a $50 strike price, the average line will slightly favor the Call options, resulting in an upward movement.

- **🟩 Dynamic Highlights for Key Data Points 🟥**:
  - Each data point with the highest Open Interest is marked with **dynamic squares** to catch the user's eye.
  - These highlights make it easy to spot which contracts or expiration dates are experiencing significant market activity.
 
- **🐂 Net Call/Put Premium & Volume 🐻**:
  - Two annotations in the top-left corner of the Plotly graph display these aggregate values:
    - **Premium**: The total dollar amount spent across the option chain at the time of the query.
    - **Volume**: The total number of contracts purchased at the time of the query.
  - These metrics provide insights into the type of flow the chain is experiencing, helping users determine whether sentiment is more **bullish** or **bearish**.

By combining these elements, Vectr ensures users can effortlessly identify trends, analyze market sentiment, and focus on the most impactful data points.


------------
**⚠️ WARNING: NOT FINANCIAL ADVICE ⚠️**

Vectr is an ongoing project, and new features and improvements are regularly being added. Feedback is welcome as we continue to refine and enhance the application.
