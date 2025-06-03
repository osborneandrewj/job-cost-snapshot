import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('job_costs.db')

# === 1. Job Cost Summary: Budget vs Actual Costs ===
summary_query = """
SELECT
   p.id,
    p.name AS project,
    p.budget,
    IFNULL(SUM(c.amount), 0) AS actual_costs,
    (p.budget - IFNULL(SUM(c.amount), 0)) AS remaining_budget,
    CASE
        WHEN p.budget > IFNULL(SUM(c.amount), 0) THEN 'Under Budget'
        WHEN p.budget < IFNULL(SUM(c.amount), 0) THEN 'Over Budget'
        ELSE 'On Budget'
    END AS budget_status
FROM projects p
LEFT JOIN costs c ON p.id = c.project_id
GROUP BY p.id
"""

summary_df = pd.read_sql_query(summary_query, conn)
print("Project Budget Summary")
print(summary_df)

# === 2. Cost Breakdown by Cost Code ===
breakdown_query = """
SELECT
    p.name AS project,
    cc.code AS cost_code,
    cc.description AS cost_description,
    c.cost_type,
    SUM(c.amount) AS total_spent
FROM costs c
JOIN projects p ON c.project_id = p.id
JOIN cost_codes cc ON c.cost_code_id = cc.id
GROUP BY p.id, cc.id, c.cost_type
ORDER BY p.id, cc.id, c.cost_type
"""

breakdown_df = pd.read_sql_query(breakdown_query, conn)
print("\nCost Breakdown by Cost Code")
print(breakdown_df.to_string(index=False))

commitment_report_query = """
SELECT
    p.name AS project,
    cc.code AS cost_code,
    cc.description AS cost_description,
    co.cost_type,
    IFNULL(SUM(co.committed_amount), 0) AS committed,
    IFNULL(SUM(c.amount), 0) AS actual,
    IFNULL(SUM(co.committed_amount), 0) - IFNULL(SUM(c.amount), 0) AS remaining_commitment
FROM projects p
LEFT JOIN commitments co ON p.id = co.project_id
LEFT JOIN cost_codes cc ON co.cost_code_id = cc.id
LEFT JOIN costs c ON 
    c.project_id = co.project_id AND 
    c.cost_code_id = co.cost_code_id AND 
    c.cost_type = co.cost_type
GROUP BY p.id, cc.code, co.cost_type
ORDER BY p.id, cc.code
"""

commitment_df = pd.read_sql_query(commitment_report_query, conn)
print("\nCommitment vs Actuals")
print(commitment_df.to_string(index=False))

# === 3. Export Reports to CSV ===
summary_df.to_csv('project_budget_summary.csv', index=False)
breakdown_df.to_csv('cost_breakdown_by_code.csv', index=False)
commitment_df.to_csv('commitment_vs_actuals.csv', index=False)

# Close the database connection 
conn.close()