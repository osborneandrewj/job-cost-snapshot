import sqlite3

conn = sqlite3.connect('job_costs.db')
cur = conn.cursor()

with open('schema.sql', 'r') as f:
    cur.executescript(f.read())

# Sample data
projects = [
    ("Medical Office Buildout", "Active", 50000),
    ("Retail Store Renovation", "Completed", 75000),
    ("Warehouse Expansion", "Active", 120000),
    ("Restaurant Construction", "Planned", 200000),
]

# Insert sample data
cur.executemany("""
INSERT INTO projects (name, status, budget) VALUES (?, ?, ?)
                """, projects)

# Sample data for 'vendors' table
vendors = [
    ("ABC Construction", "General Contractor", "123-456-7890"),
    ("XYZ Electrical", "Electrical Contractor", "987-654-3210"),
    ("Quality Plumbing", "Plumbing Contractor", "555-555-5555"),
]

cur.executemany("""
INSERT INTO vendors (name, type, contact_info) VALUES (?, ?, ?)
                """, vendors)

# Sample data for 'cost_codes' table
cost_codes = [
    ("100", "Labor"),
    ("200", "Materials"),
    ("300", "Rental Equipment"),
    ("400", "Subcontractor Costs"),
]
cur.executemany("""
INSERT INTO cost_codes (code, description) VALUES (?, ?)
                """, cost_codes)

# Sample data for 'costs' table
costs = [
    # Project 1 – Under budget (Total: 24,000 vs Budget: 50,000)
    (1, 1, 1, 'L', 12000, "Plumbing labor", "2024-05-01"),
    (1, 2, 2, 'M', 8000, "Electrical materials", "2024-05-05"),
    (1, 3, 2, 'M', 4000, "Piping materials", "2024-05-07"),

    # Project 2 – Over budget (Total: 80,000 vs Budget: 75,000)
    (2, 1, 1, 'L', 20000, "Labor for renovation", "2024-04-01"),
    (2, 2, 3, 'S', 20000, "Subcontractor wiring", "2024-04-10"),
    (2, 3, 2, 'M', 40000, "Fixtures and finishes", "2024-04-15"),

    # Project 3 – Under budget (Total: 70,000 vs Budget: 120,000)
    (3, 1, 1, 'L', 30000, "Framing labor", "2024-06-01"),
    (3, 2, 2, 'M', 20000, "Concrete materials", "2024-06-05"),
    (3, 3, 3, 'E', 20000, "Equipment rental", "2024-06-07"),

    # Project 4 – Over budget (Total: 210,000 vs Budget: 200,000)
    (4, 1, 1, 'L', 100000, "Full kitchen labor", "2024-07-01"),
    (4, 2, 4, 'S', 70000, "HVAC subcontractor", "2024-07-05"),
    (4, 3, 2, 'M', 40000, "Interior materials", "2024-07-07"),
]

cur.executemany("""
INSERT INTO costs (project_id, vendor_id, cost_code_id, cost_type, amount, description, incurred_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, costs)

# Commitments to model CMiC and other Construction ERP systems
# Sample data for 'commitments' table
commitments = [
    # Project 1
    (1, 1, 1, 'L', 15000),  # Committed labor with ABC Construction
    (1, 2, 2, 'M', 10000),  # Materials from XYZ Electrical

    # Project 2
    (2, 1, 1, 'L', 18000),
    (2, 2, 4, 'S', 12000),

    # Project 3
    (3, 3, 3, 'E', 25000),

    # Project 4
    (4, 1, 2, 'M', 80000),
    (4, 2, 4, 'S', 100000),
]

cur.executemany("""
INSERT INTO commitments (project_id, vendor_id, cost_code_id, cost_type, committed_amount)
                VALUES (?, ?, ?, ?, ?)
                """, commitments)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database seeded with sample data successfully.")