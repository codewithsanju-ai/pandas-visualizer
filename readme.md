# 📊 Sales Data Analyzer & Visualization

A beginner-friendly Python project for analyzing sales data using **Pandas, NumPy, Matplotlib, and Seaborn**. This project provides a menu-driven interface to explore datasets, handle missing values, perform mathematical and statistical operations, combine datasets, create pivot tables, and generate visualizations.

## 📌 Project Overview

The **Sales Data Analyzer** is a console-based data analysis application developed using Python and Object-Oriented Programming (OOP).

Users can load a CSV dataset and perform different data analysis operations through a simple menu system. The project helps beginners understand how Python libraries can be used to analyze sales information and visualize business data.

## ✨ Features

### 1. 📂 Load Dataset
- Load sales data from CSV files.
- Read data using Pandas.
- Display the loaded dataset.
- Support CSV files with Latin-1 encoding.

### 2. 🔍 Explore Data
- Display the first five rows using `head()`.
- Display the last five rows using `tail()`.
- Display all column names.
- Check column data types using `dtypes`.
- Display dataset information using `info()`.

### 3. 🧹 Handle Missing Values
- Check missing values in each column.
- Fill missing values using a mean value.
- Remove rows containing missing values.
- Replace missing values with a custom value such as `"Unknown_value"`.

### 4. 🧮 DataFrame Operations
- Perform mathematical operations on sales columns.
- Combine datasets using Pandas `merge()`.
- Split data using `loc` and `iloc`.
- Merge datasets using an outer join based on `order_id`.

### 5. 📈 Search, Sort, and Filter
- Search sales records using an order ID.
- Sort the dataset in ascending order.
- Sort the dataset in descending order.
- Select records based on specific conditions.

### 6. 📊 Aggregate Functions
Calculate important sales metrics using:
- `sum()` — total value
- `max()` — maximum value
- `min()` — minimum value

Supported columns include revenue, profit, discounted price, shipping cost, rating, quantity, and product price.

### 7. 📉 Statistical Analysis
Calculate statistical measures for numerical columns:
- `mean()` — average value
- `median()` — middle value
- `std()` — standard deviation
- `var()` — variance

### 8. 📋 Pivot Table
- Create pivot tables using selected columns.
- Choose index, column, and value fields.
- Apply aggregation functions such as mean, median, standard deviation, variance, and sum.

### 9. 📉 Data Visualization
Generate different types of charts using Matplotlib:

| Chart | Purpose |
|---|---|
| Bar Plot | Compare values across categories |
| Line Plot | Show trends and changes |
| Scatter Plot | Explore relationships between numerical variables |
| Pie Chart | Display proportions of values |
| Histogram | Understand numerical distributions |
| Stack Plot | Compare cumulative values |
| Subplots | Display multiple charts in one figure |

### 10. 💾 Save Visualizations
- Ask the user whether to save a generated graph.
- Save plots as image files.
- Use high-resolution output with `dpi=300`.
- Automatically adjust image boundaries using `bbox_inches="tight"`.

## 🛠️ Technologies Used

- **Python** — core programming language
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical operations
- **Matplotlib** — charts and visualization
- **Seaborn** — statistical visualization library

## 📚 Python Concepts Used

This project demonstrates:

- Object-Oriented Programming (OOP)
- Classes and objects
- Instance attributes and methods
- Conditional statements
- `while` loops
- `match-case` statements
- User input and output
- Functions and method calls
- CSV file handling
- Pandas DataFrames
- Data cleaning and transformation
- Data aggregation and statistics
- Data visualization

## 📁 Project Structure

```text
Sales-Data-Analyzer/
│
├── main.py
├── shopify_sales_dataset_ml_eda5.csv
├── shopify_order_details_20_rows.csv
├── README.md
│
└── visualizations/
    ├── mybarplot.png
    ├── mylineplot.png
    ├── myscatterplot.png
    ├── mypieplot.png
    ├── myhistplot.png
    ├── mystackplot.png
    └── mysubplot.png
```

*Note: The filenames and folder structure above are suggested examples. Adjust them to match your actual project files.*

## ⚙️ Installation and Setup

### Step 1: Install Python

Install Python from the official website:

https://www.python.org/downloads/

### Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 3: Open the Project

```bash
cd Sales-Data-Analyzer
```

### Step 4: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 5: Configure Dataset Paths

Update the CSV file paths in `main.py` to match the location of your dataset files.

For example:

```python
h1.load_data("shopify_sales_dataset_ml_eda5.csv")
```

Keep the dataset in the project folder or provide its correct path.

### Step 6: Run the Program

```bash
python main.py
```

## ▶️ How to Use

1. Run the Python program.
2. Select **Load Dataset** from the main menu.
3. Explore the dataset and inspect its columns.
4. Handle missing values if required.
5. Perform mathematical and statistical operations.
6. Search, sort, combine, or split data.
7. Create pivot tables and visualizations.
8. Choose whether to save generated graphs.
9. Exit the program using the main menu.

## 🎯 Learning Outcomes

After completing this project, users can understand how to:

- Build a menu-driven Python application.
- Organize a program using classes and methods.
- Load and manipulate CSV datasets.
- Inspect and clean data using Pandas.
- Apply mathematical and statistical functions.
- Combine and split datasets.
- Create pivot tables for summarizing data.
- Generate different visualizations.
- Save charts as image files.

## 🚀 Future Improvements

- Add input validation and error handling.
- Validate column names before performing operations.
- Allow users to select the dataset path dynamically.
- Save cleaned datasets to CSV or Excel files.
- Add more filtering options.
- Generate automated sales summary reports.
- Add interactive dashboards.
- Allow users to choose a folder for saving visualizations.
- Create a graphical user interface (GUI).

## ⚠️ Current Limitations

- The program expects specific column names in the dataset.
- Some menu inputs require integers and may fail for invalid input.
- The missing-value mean operation currently uses the `quantity` column's mean for the entire DataFrame.
- The `loc` and `iloc` options use different indexing behavior.
- Dataset paths are currently configured directly in the code.
- Some chart types require numerical columns and compatible data lengths.

## 👨‍💻 Author

**Sanjay Kushwaha**

Python | Data Analysis | Pandas | NumPy | Data Visualization

## 📄 License

This project is intended for educational and learning purposes. You may modify and extend it for your own practice.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub.
