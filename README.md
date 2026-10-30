# Strategy KPI Tracker

A Python tool that tracks strategic KPIs using the balanced scorecard approach.

## What it does
- Reads KPIs grouped by perspective (Customer, Financial, Internal Processes, Learning & Growth)
- Calculates achievement % against each target
- Classifies each KPI as Achieved, On track, or Behind
- Draws charts and saves the results to a CSV file

## Important note
All data in `kpi_data.csv` is **fictional** and created only to demonstrate the tool.
It does not represent any real organization.

## How it works
- For "higher is better" KPIs: achievement = actual / target
- For "lower is better" KPIs (e.g. response time): achievement = target / actual
- Status: 100%+ Achieved, 85-99% On track, below 85% Behind

## How to run
    pip install -r requirements.txt
    python tracker.py

## Built with
Python, Pandas, Matplotlib

## Future ideas
- Track KPIs over several quarters
- Add an interactive dashboard
- Export an Excel report
