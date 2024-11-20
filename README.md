# Vectr

**Vectr** is a Python-based tool designed to simplify stock option analysis. Built on the powerful `yfinance` module and supported by additional libraries such as `Flask`, `Pandas`, and `Plotly`, Vectr provides users with an intuitive interface for exploring and visualizing stock options data.

### **🔑Key Features:**
- *Search Any Optionable Stock Ticker(s)*: Easily search for single or multiple stock tickers across the entire stock market. ("Optionable" stocks are those with available options for purchase.)

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


Once you've successfully completed the prior step of your choice and access the web application, you will reach the home page:

![GitHubPicture1_Search_Tickers](https://github.com/user-attachments/assets/cd802404-624d-4f67-8fee-3f6cb3928ed8)

From here, you can search a singular ticker or multiple tickers, either comma or space separated.  You can then hit 'Enter' or press the 'Search' button to extract the option chain data

![GitHubPicture2_Search_Tickers_Cont](https://github.com/user-attachments/assets/9a017fa5-f778-4841-97dc-97d072ea6e66)


Here's a sample of the option chain pulled for AAPL stock:
![image](https://github.com/user-attachments/assets/1bf826ca-b889-43fa-9852-6d15e89298a3)

Here's some further detail on data is visualized for you:
![image](https://github.com/user-attachments/assets/081ed27e-ab4a-4a4a-8279-101ae1ba14a4)
