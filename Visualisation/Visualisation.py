import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Netflix dataset
df = pd.read_csv("data/cleaned/netflix_cleaned.csv")

print("Dataset loaded successfully!")
print("Total titles:", len(df))

# Chart 1: Movies vs TV Shows
df["type"].value_counts().plot(kind="bar")
plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_types.png")
plt.show()

# Chart 2: Netflix titles by release year
df["release_year"].value_counts().sort_index().plot(kind="line")
plt.title("Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_by_year.png")
plt.show()

# Chart 3: Top 10 Genres
genres = df["listed_in"].dropna().str.split(", ").explode()
genres.value_counts().head(10).sort_values().plot(kind="barh")
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig("top_10_genres.png")
plt.show()

print("All three charts created successfully!")
