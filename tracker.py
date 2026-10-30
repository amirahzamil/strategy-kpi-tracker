"""Strategy KPI Tracker
Calculates achievement and status for each KPI in a balanced scorecard
and draws charts. All data in kpi_data.csv is FICTIONAL, for demonstration.

Usage: python tracker.py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("kpi_data.csv")
os.makedirs("charts", exist_ok=True)


def achievement(row):
    """Achievement % (for 'lower is better' KPIs the ratio is flipped)."""
    if row["better"] == "higher":
        return row["actual"] / row["target"] * 100
    return row["target"] / row["actual"] * 100


def status(pct):
    if pct >= 100:
        return "Achieved"
    if pct >= 85:
        return "On track"
    return "Behind"


df["achievement_pct"] = df.apply(achievement, axis=1).round(1)
df["status"] = df["achievement_pct"].apply(status)

# Chart 1: average achievement per perspective
by_perspective = df.groupby("perspective")["achievement_pct"].mean().sort_values()
by_perspective.plot(kind="barh", title="Average Achievement by Perspective (%)")
plt.axvline(100, color="gray", linestyle="--")
plt.savefig("charts/achievement_by_perspective.png", bbox_inches="tight")
plt.close()

# Chart 2: every KPI, colored by status
colors = {"Achieved": "green", "On track": "orange", "Behind": "red"}
ordered = df.sort_values("achievement_pct")
plt.barh(ordered["kpi"], ordered["achievement_pct"],
         color=ordered["status"].map(colors))
plt.axvline(100, color="gray", linestyle="--")
plt.title("KPI Achievement (%)")
plt.savefig("charts/kpi_status.png", bbox_inches="tight")
plt.close()

df.to_csv("kpi_results.csv", index=False)

print("Status summary:")
print(df["status"].value_counts().to_string())
print(f"\nWeakest KPI: {ordered.iloc[0]['kpi']} ({ordered.iloc[0]['achievement_pct']}%)")
print(f"Weakest perspective: {by_perspective.index[0]}")
print("Results saved to kpi_results.csv and charts/")
