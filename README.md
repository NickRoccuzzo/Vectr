# Vectr
![image](https://github.com/user-attachments/assets/0a7116f1-e6b9-4d49-abc2-a6ee1a4ccc56)



**Vectr** is a Python-based tool designed to simplify stock option analysis. Built on the powerful `yfinance` module and supported by additional libraries such as `Flask`, `Pandas`, and `Plotly`, Vectr provides users with an intuitive interface for exploring and visualizing stock options data.

### **🔑Key Features:**
- *Search Any Optionable Stock Ticker(s)*: Easily search for single or multiple stock tickers across the entire stock market. ("Optionable" stocks are those with available options for purchase.)

- *Dynamic Visualizations*: Generate interactive line graphs, bar graphs, and other visual enhancements to analyze options chains.

- *Market Insights*: Assess whether the market sentiment for a stock is bullish or bearish based on its options data.


------------


### **⚙️ How It Works:**

<details>
  <summary>Running Vectr in a <b>Docker Container</b></summary>

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
  <summary>Running Vectr in a <b>Virtual Environment (venv)</b></summary>

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

![GitHubPicture2_Search_Tickers_Cont](https://github.com/user-attachments/assets/9a017fa5-f778-4841-97dc-97d072ea6e66)


![image](https://github.com/user-attachments/assets/1bf826ca-b889-43fa-9852-6d15e89298a3)


![image](https://github.com/user-attachments/assets/081ed27e-ab4a-4a4a-8279-101ae1ba14a4)
