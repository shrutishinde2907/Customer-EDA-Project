# Customer Segmentation and Behavior Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on customer data to understand customer behavior and identify patterns in age, income, and spending habits.

Customer segmentation helps businesses target marketing campaigns and improve customer experience.

## Objectives

* Analyze demographic characteristics of customers.
* Understand customer spending behavior.
* Identify relationships between income and spending score.
* Discover patterns useful for business decision-making.

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Visual Studio Code

## Dataset

The dataset contains the following columns:

* CustomerID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

## Project Structure

```
Customer_EDA_Project
│
├── customer_eda.py
├── customer_data.csv
└── graphs
    ├── gender_distribution.png
    ├── age_distribution.png
    ├── income_distribution.png
    ├── income_vs_spending.png
    ├── age_vs_spending.png
    └── correlation_heatmap.png
```

## Visualizations Created

1. Gender distribution
2. Age distribution
3. Annual income distribution
4. Income vs spending score
5. Age vs spending score
6. Correlation heatmap

## Steps to Run the Project

1. Install Python.
2. Install required libraries:

```
pip install pandas
pip install matplotlib
pip install seaborn
```

3. Run the Python file:

```
python customer_eda.py
```

## Expected Output

The program generates visualizations showing customer demographics and spending behavior.

## Insights

* Younger customers may have higher spending scores.
* Income levels influence purchasing behavior.
* Customer groups can be segmented based on spending patterns.

## Conclusion

EDA helps businesses understand customers better and create effective marketing strategies.

## Author

Student Data Science Project
