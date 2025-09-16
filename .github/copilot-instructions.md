# Copilot Instructions for Data Science Workspace

## Overview
This workspace is focused on data analysis, visualization, and machine learning using Python and Jupyter Notebooks. The main workflow involves cleaning datasets, performing exploratory data analysis (EDA), running SQL-like queries, and building predictive models. Most work is done interactively in notebooks, with CSV files as primary data sources.

## Key Files & Structure
- **Notebooks**: All analysis is performed in `.ipynb` files (e.g., `Understanding and Forecasting Student Performance in India.ipynb`).
- **CSV Data**: Data files (e.g., `StudentsPerformance.csv`, `titanic.csv`, `nba.csv`) are loaded directly in notebooks.
- **Scripts**: Occasional `.py` files for utility functions or quick checks.
- **Visualization**: Uses `matplotlib`, `seaborn`, and sometimes `plotly` for plots.

## Patterns & Conventions
- **Data Loading**: Use `pandas.read_csv()` for all CSV imports.
- **Data Cleaning**: Standardize categorical values, check for duplicates, and handle missing data in initial notebook cells.
- **Feature Engineering**: Derived columns (e.g., `average_score`, `performance_category`) are added before analysis.
- **SQL Operations**: SQL queries are written as markdown cells for documentation and sometimes executed via pandas or SQLite.
- **EDA**: Visualizations are grouped by subject, demographic, or intervention (see EDA section in main notebook).
- **Machine Learning**: Models are built using `scikit-learn` with clear separation between regression and classification tasks. Categorical features are encoded with `pd.get_dummies()` or `LabelEncoder`.
- **Results**: Print metrics and feature importances in notebook cells for transparency.

## Developer Workflow
- **Interactive Development**: All code is run and debugged in Jupyter Notebooks. No automated test suite or build system is present.
- **Environment**: Python environment should include `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`. Install missing packages via pip if needed.
- **Data Updates**: If new data is added, update notebook cells to reflect new file paths and rerun relevant analysis.

## Integration Points
- **External Data**: All data is local CSV or Excel files. No external APIs or databases are integrated.
- **SQL**: SQL queries are for documentation or use with pandas/SQLite, not for production database integration.

## Examples
- See `Understanding and Forecasting Student Performance in India.ipynb` for end-to-end workflow: data cleaning, EDA, SQL, ML.
- Use `df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)` for feature engineering.
- Visualize with `sns.histplot(df['math score'], kde=True)` or similar.

## Tips for AI Agents
- Always check for missing values and duplicates before analysis.
- Follow the notebook structure: cleaning → EDA → SQL → ML.
- Use markdown cells for documentation and SQL queries.
- Reference CSV files by their exact name and path.
- Prefer pandas for all data manipulation.

---
If any section is unclear or missing, please provide feedback for further refinement.
