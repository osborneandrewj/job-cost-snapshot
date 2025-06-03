
# Job Cost Snapshot (CMiC/Sage-Inspired ERP Mini System)

This is a lightweight construction ERP simulation built using **Python** and **SQLite** — inspired by real-world platforms like **CMiC** and **Sage 100 Contractor**.

It models core job costing workflows:

- Projects, vendors, cost codes, and cost types
- Actual vs. budget tracking
- CMiC-style **commitments** (planned spend vs actual spend)
- Sage-style **cost code/type** reporting
- Exports to CSV for business intelligence use

---

## Features

✅ Job Cost Summary
Shows budget, actuals, remaining, and over/under status per project

✅ Cost Breakdown by Code + Type
Aggregates spending by phase and cost type (Labor, Materials, Subcontractor, etc.)

✅ Commitments Module (CMiC-style)
Tracks committed amounts (e.g., purchase orders, subcontracts) vs actuals and remaining commitment

✅ Clean SQLite + Python data model

- Easy to extend (e.g. add billing, change orders, forecasting)
- Portable and runnable locally

---

## Schema Overview

projects – Project setup: name, status, budget
vendors – Subcontractors or suppliers
cost_codes – CSI-style phase codes
costs – Actual job costs with type (L/M/S)
commitments – Planned spend by project/vendor/code

---

## How to Run It

1. Install requirements:

```bash
pip install pandas
```

2. Seed the database:

```bash
python data_seed.py
```

3. Run reports:

```bash
python report.py
```

4. Review exported CSVs:

- `project_budget_summary.csv`
- `cost_breakdown_by_code.csv`
- `commitments_vs_actuals.csv`

---

## 📂 File Overview

| File             | Purpose                                  |
| ---------------- | ---------------------------------------- |
| `schema.sql`   | Defines all tables                       |
| `data_seed.py` | Seeds initial project, vendor, cost data |
| `report.py`    | Runs summary and breakdown reports       |
| `README.md`    | This project overview                    |

---

## Inspired by

This project was built to simulate core ERP logic found in:

- **CMiC**: Commitment-based forecasting, job cost inquiry
- **Sage 100 Contractor**: Phase/type-based cost tracking, job reports

---

## Future Enhancements

- Add `change_orders` to update budget dynamically
- Add `billing` and `invoices` to calculate over/under billing
- Integrate with Jupyter or Streamlit for dashboards
- Convert into a small web app using Flask

---

## License

MIT — use it, fork it, remix it.
