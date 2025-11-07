import pandas as pd
from tqdm import tqdm
from db_config import get_engine

# ---------- EXTRACT ----------
print("Extracting movie dataset...")

data_path = "data/movies.csv"
df = pd.read_csv(data_path)
print(f"Loaded {len(df)} records from {data_path}")

# ---------- TRANSFORM ----------
print("Cleaning and transforming data...")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing titles
df.dropna(subset=['title'], inplace=True)

# Capitalize movie titles properly
df['title'] = df['title'].str.title()

# Convert release year to integer if possible
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0).astype(int)

print("Data cleaned and transformed successfully!")

# ---------- LOAD ----------
print("Loading data into destination...")

try:
    engine = get_engine()
    df.to_sql("movies", engine, if_exists="replace", index=False)
    print(" Data loaded into database (PostgreSQL)")
except Exception as e:
    print("Database not configured or connection failed.")
    print("Saving transformed data to CSV instead...")
    df.to_csv("data/movies_transformed.csv", index=False)
    print("Saved data to data/movies_transformed.csv")

print("ETL process completed!")

