import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# Setup
os.makedirs("outputs", exist_ok=True)

# Load data
df = pd.read_csv("Dataset .csv", encoding="utf-8")

df = df.dropna(subset=['Latitude', 'Longitude'])

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Setup
os.makedirs("outputs", exist_ok=True)

# === BAR CHART: Top 10 Cities ===
grouped = df.groupby('City').agg({
    'Restaurant ID': 'count'
}).rename(columns={'Restaurant ID': 'Total Restaurants'}).reset_index()

top_cities = grouped.sort_values(by='Total Restaurants', ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(data=top_cities, x='City', y='Total Restaurants', palette='viridis')
plt.title("Top 10 Cities by Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
chart_path = "outputs/top_cities.png"
plt.savefig(chart_path)




# === Generate Single HTML Page ===
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Location Analysis Dashboard</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
        }}
        h1, h2 {{
            color: #2c3e50;
        }}
        iframe {{
            border: 2px solid #ccc;
            margin-bottom: 40px;
        }}
        img {{
            max-width: 100%;
        }}
    </style>
</head>
<body>
    <h1>📍 Restaurant Location Analysis</h1>

    <h2>3. Top 10 Cities by Number of Restaurants</h2>
    <img src="top_cities.png" alt="Top Cities Chart">


</body>
</html>
"""

with open("outputs/dashboard.html", "w", encoding='utf-8') as f:
    f.write(html_template)

print("✅ Dashboard created: outputs/dashboard.html")
