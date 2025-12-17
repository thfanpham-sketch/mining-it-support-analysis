import pandas as pd


df = pd.read_csv("mining_it_incidents.csv")
df["downtime_hours"] = df["downtime_minutes"] / 60


print("=== First 5 rows ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Missing Values ===")
print(df.isnull().sum())

print("\n=== Most Common Issue Types ===")
issue_counts = df["issue_type"].value_counts()
print(issue_counts)

print("\n=== Total Downtime by System (hours) ===")

downtime_by_system = (
    df.groupby("system")["downtime_hours"]
    .sum()
    .sort_values(ascending=False)
)

print(downtime_by_system)

#Identify unresolved high-severity IT incidents

print("\n=== Unresolved High-Severity Incidents ===")

critical_issues = df[
    (df["severity"] == "High") &
    (df["resolved"] == "No")
]

if critical_issues.empty:
    print("No unresolved high-severity incidents.")
else:
    print(critical_issues[[
        "incident_id",
        "date",
        "site",
        "system",
        "issue_type",
        "downtime_minutes"
    ]].to_string(index=False))
