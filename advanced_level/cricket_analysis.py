@@ -0,0 +1,107 @@
import matplotlib

matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fielding_data.csv")

weights = {
    "CP": 2,
    "GT": 3,
    "C": 5,
    "DC": -4,
    "ST": 4,
    "RO": 6,
    "MRO": -3,
    "DH": 5
}

for col in weights.keys():
    df[col] = 0

df["RunsSaved"] = df["Runs"]



def classify(row):
    pick = str(row["Pick"]).lower()
    throw = str(row["Throw"]).lower()

    if "clean" in pick:
        row["CP"] = 1
    if "good throw" in pick:
        row["GT"] = 1
    if "catch" in pick and "drop" not in pick:
        row["C"] = 1
    if "drop" in pick:
        row["DC"] = 1
    if "stumping" in throw:
        row["ST"] = 1
    if "run out" in throw:
        row["RO"] = 1
    if "missed run out" in throw:
        row["MRO"] = 1
    if "direct hit" in throw:
        row["DH"] = 1

    return row


df = df.apply(classify, axis=1)

df["PS"] = (
        df["CP"] * weights["CP"] +
        df["GT"] * weights["GT"] +
        df["C"] * weights["C"] +
        df["DC"] * weights["DC"] +
        df["ST"] * weights["ST"] +
        df["RO"] * weights["RO"] +
        df["MRO"] * weights["MRO"] +
        df["DH"] * weights["DH"] +
        df["RunsSaved"]
)


player_stats = df.groupby("Player Name").agg({
    "CP": "sum",
    "GT": "sum",
    "C": "sum",
    "DC": "sum",
    "ST": "sum",
    "RO": "sum",
    "MRO": "sum",
    "DH": "sum",
    "RunsSaved": "sum",
    "PS": "sum"
}).reset_index()

player_stats = player_stats.sort_values(by="PS", ascending=False)


print("\n Player Performance Analysis:\n")
print(player_stats)

print("\n Best Fielder:")
print(player_stats.iloc[0]["Player Name"])

print("\n Needs Improvement:")
print(player_stats.iloc[-1]["Player Name"])


plt.figure()
plt.bar(player_stats["Player Name"], player_stats["PS"])
plt.xticks(rotation=45)
plt.title("Player Performance Score")
plt.xlabel("Players")
plt.ylabel("Performance Score")
plt.tight_layout()

plt.savefig("performance.png")
print("\n Graph saved as 'performance.png'")


player_stats.to_csv("fielding_analysis_output.csv", index=False)

print("Output saved as 'fielding_analysis_output.csv'")
