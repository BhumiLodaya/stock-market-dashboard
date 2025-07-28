📊 Stock Market Dashboard with MySQL & Dash
An interactive and dynamic stock market dashboard built using Plotly Dash, Pandas, and MySQL, designed to provide insightful visualizations of stock performance across sectors, tickers, and time ranges.

<br/>
📁 Project Structure
graphql
Copy
Edit
stock-dashboard/
│
├── graph.py                    # Main Dash app file
├── insert_stocks_to_mysql.py  # Loads CSV data into MySQL
├── stock_market_june2025.csv  # Cleaned stock market dataset
├── README.md                   # Project documentation
🚀 Features
✅ Real-Time Visualizations:
Line graph for closing price trends of selected tickers and sectors

Sector-wise stock price comparison

Pie chart showing sector contributions to total market cap

High vs. Low price comparison across selected tickers and dates

Auto-adaptive visuals when:

Only sector is selected

No ticker/date is chosen

Multiple tickers selected

✅ Smart Filtering:
Dropdown filters for Sector, Ticker, and Date

Automatically handles missing or unordered dates

Dynamically adjusts visual content depending on filter combinations

✅ MySQL Backend:
Dataset is stored in a MySQL database

Efficient querying and data fetching for scalable performance

Python script auto-creates the table and inserts data

💾 Setup Instructions
1️⃣ Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/stock-dashboard.git
cd stock-dashboard
2️⃣ Install Required Packages
bash
Copy
Edit
pip install pandas plotly dash mysql-connector-python sqlalchemy
3️⃣ Set Up MySQL
Create a database in MySQL:

sql
Copy
Edit
CREATE DATABASE stock_dashboard_db;
Update your MySQL credentials in insert_stocks_to_mysql.py:

python
Copy
Edit
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_NAME = "stock_dashboard_db"
4️⃣ Load Data into MySQL
bash
Copy
Edit
python insert_stocks_to_mysql.py
5️⃣ Run the Dashboard
bash
Copy
Edit
python graph.py
Open your browser and navigate to http://127.0.0.1:8050

📂 Dataset
Filename: stock_market_june2025.csv

Fields:

Ticker

Date

Open Price

Close Price

High

Low

Volume

Sector

Market Cap

📈 Future Improvements
Add prediction of future stock prices using ML

Live stock API integration (e.g., Alpha Vantage, Yahoo Finance)

User login & session history

Export chart as PDF or PNG

🙋‍♀️ Author
👤 Bhumi Lodaya
📧 bhumilodaya23@gmail.com
📎 Interested in Data Science, Cybersecurity & Intelligent Dashboards

🏷️ License
This project is licensed under the MIT License.
