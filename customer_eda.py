import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
data = pd.read_csv("customer_data.csv")

# Create graphs folder
if not os.path.exists("graphs"):
    os.makedirs("graphs")

print("First 5 rows")
print(data.head())

print("\nDataset Info")
data.info()

print("\nStatistical Summary")
print(data.describe())

# -----------------------
# Gender Distribution
# -----------------------
plt.figure(figsize=(6,4))

sns.countplot(x='Gender', data=data)

plt.title("Gender Distribution")

plt.tight_layout()
plt.savefig("graphs/gender_distribution.png", dpi=300)

plt.show()

# -----------------------
# Age Distribution
# -----------------------
plt.figure(figsize=(6,4))

plt.hist(data['Age'], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("graphs/age_distribution.png", dpi=300)

plt.show()

# -----------------------
# Income Distribution
# -----------------------
plt.figure(figsize=(6,4))

plt.hist(data['Annual Income (k$)'], bins=10)

plt.title("Annual Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("graphs/income_distribution.png", dpi=300)

plt.show()

# -----------------------
# Spending Score vs Income
# -----------------------
plt.figure(figsize=(6,5))

sns.scatterplot(
    x=data['Annual Income (k$)'],
    y=data['Spending Score (1-100)']
)

plt.title("Income vs Spending Score")

plt.tight_layout()
plt.savefig("graphs/income_vs_spending.png", dpi=300)

plt.show()

# -----------------------
# Age vs Spending Score
# -----------------------
plt.figure(figsize=(6,5))

sns.scatterplot(
    x=data['Age'],
    y=data['Spending Score (1-100)']
)

plt.title("Age vs Spending Score")

plt.tight_layout()
plt.savefig("graphs/age_vs_spending.png", dpi=300)

plt.show()

# -----------------------
# Correlation Heatmap
# -----------------------
plt.figure(figsize=(6,5))

sns.heatmap(data.corr(numeric_only=True), annot=True)

plt.title("Customer Data Correlation")

plt.tight_layout()
plt.savefig("graphs/correlation_heatmap.png", dpi=300)

plt.show()