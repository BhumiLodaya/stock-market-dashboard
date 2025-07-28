# 📈 Stock Market Dashboard – June 2025

This project is a full-fledged stock market dashboard built using Python's Dash framework. It allows you to visualize stock performance by sector, ticker, and date, with data stored in a MySQL database.

## 📂 Files Included

| File | Description |
|------|-------------|
| `graph.py` | Main Dash dashboard with stock visualizations |
| `insert_stock_to_mysql.py` | Script to insert data from the CSV to MySQL |
| `stock_market_june2025.csv` | Raw stock market dataset used for MySQL |

---

## 🚀 Features

- Visualize sector-wise stock performance  
- Custom date and ticker comparisons  
- MySQL-powered backend  
- Interactive Dash and Plotly visualizations  

---

## 🛠️ How to Run

### 1. Clone the Repository
bash
git clone https://github.com/your-username/stock-market-dashboard.git
cd stock-market-dashboard


### 2.Install Requirements
bash
Copy
Edit
pip install -r requirements.txt


### 3. Configure MySQL
Create a database in MySQL (e.g., stock_db)

Update DB credentials in insert_stock_to_mysql.py and graph.py


### 4. Insert Data into MySQL
bash
Copy
Edit
python insert_stock_to_mysql.py


### 5. Run the Dashboard
bash
Copy
Edit
python graph.py
The dashboard will open in your browser at http://127.0.0.1:8050/.

<details>
<summary>Click to view MySQL table structure</summary>

sql
CREATE TABLE stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10),
    sector VARCHAR(100),
    date DATE,
    open_price FLOAT,
    close_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    volume INT
);

### ✅ Tech Stack (at a glance)
Give a quick summary of tools used.

markdown
Copy
Edit
## 🧰 Tech Stack

- **Frontend**: Dash, Plotly
- **Backend**: Python, MySQL
- **Data Handling**: Pandas

### ✅ Author & Acknowledgments

## 👤 Author

**Bhumi Paresh Lodaya**  
B.Tech in Computer Science  
Data Science & Cybersecurity Enthusiast

---

## 🙏 Acknowledgements

- [Plotly Dash Documentation](https://dash.plotly.com/)
- [MySQL Docs](https://dev.mysql.com/doc/)
- 

## 📝 License

This project is licensed under the [MIT License](LICENSE).
