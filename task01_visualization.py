import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read CSV (skip metadata rows)
df = pd.read_csv("data/population_data.csv", skiprows=4)

# Step 2: Check columns (for understanding)
print(df.columns)

# Step 3: Select a single year (1960 is safe)
population_1960 = df['1960']

# Step 4: Remove missing values
population_1960 = population_1960.dropna()

# Step 5: Create histogram
plt.figure()
plt.hist(population_1960, bins=20)
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.title("Population Distribution by Country (1960)")

# Step 6: Save output
plt.savefig("output/population_distribution_1960.png")

# Step 7: Show graph
plt.show()
