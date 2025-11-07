import pandas as pd
import matplotlib.pyplot as plt
from db_config import get_engine

print("🔗 Connecting to MySQL database...")
engine = get_engine()
print(" SQLAlchemy connection successful!")

# Load data from MySQL into a DataFrame
df = pd.read_sql("SELECT * FROM movies", engine)
print(f"Loaded {len(df)} records from database")

# Bar chart: number of movies per genre
genre_counts = df['genre'].value_counts()

plt.figure(figsize=(6, 4))
genre_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.tight_layout()

# Save chart (optional)
plt.savefig("data/movies_genre_chart.png")

# Display chart
plt.show()
