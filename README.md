# Daily Expense and Pocket Money Tracker in Python

### Submitted by: Kriti Pal | [25BAI10713]

## 📝 Overview
This is a simple, command-line (CLI) application designed to help students manage and monitor their personal finances. It allows users to record daily expenses and track pocket money (receivables) from various sources, aiding in better budgeting and financial awareness.

## ✨ Features
* **Transaction Management:** Manually enter expenses and receivables with details like amount, date, source tagging, and notes.
* **Data Integrity:** Implements rigorous input validation and robust error handling to prevent data corruption.
* **Reporting & Analytics:** Generate clear financial reports (total income/expense, net balance) and category-wise analysis of spending.
* **Data Persistence:** Transactions are stored persistently in a JSON file.

## 🛠️ Technologies/Tools Used
* **Primary Language:** Python 3.x
* **Storage:** JSON files (flat file persistence)
* **Testing Framework:** `pytest` (for automated unit testing)
* **Version Control:** Git

## 🚀 Steps to Install & Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/kriti25bai10713-hue/daily-expense-and-pocket-money-tracker-.git
    cd Daily-Expense-Tracker
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    ```bash
    python src/main.py
    ```

## 🧪 Instructions for Testing

The project implements automated unit testing to verify core business logic, such as input validation and report generation accuracy, as required by the report. The tests are located in the **`tests/`** directory.

1.  **Ensure Dependencies are Installed:** Make sure `pytest` is installed (listed in `requirements.txt`).

2.  **Execute Tests:** Run the test suite from the root directory of the project:
    ```bash
    pytest tests/
    ```
    Successful execution confirms that all mandatory non-functional requirements (like **Error Handling**) are working correctly.
