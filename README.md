# Movie Data Pipeline

This project is a Python-based ETL (Extract, Transform, Load) pipeline designed to process movie datasets. It extracts data from CSV files, cleans it, transforms it, loads it into a MySQL database, and generates visualizations and analytical queries.

## Technologies Used

- Python 3.14, Pandas for data manipulation
- SQLAlchemy for ORM and database interaction
- PyMySQL as MySQL database driver
- MySQL for data storage and querying
- Git for version control and GitHub for repository hosting
- Python virtual environments for dependency management

## Environment Setup

1. Clone the repository:git clone https://github.com/00Bhavani/movie-data-pipeline.git
cd movie-data-pipeline

2. Create and activate a Python virtual environment:
- On Windows (Git Bash):
  ```
  "/c/Program Files/Python314/python.exe" -m venv env
  source env/Scripts/activate
  ```

3. Install dependencies:
pip install -r requirements.txt

4. Configure database connection details in the `.env` file.

## Running the ETL Pipeline

Run the following command to extract, transform, and load your movie data into MySQL:
python etl_pipeline.py

## Generating Visualizations and Running Queries
- To generate charts and graphs from the data:
python visualize_results.py

- Use MySQL Workbench or another MySQL client to run SQL queries contained in `queries.sql` for deeper analysis.

This project showcases abilities in Python scripting, data engineering, SQL database management, and data visualization, providing full end-to-end data pipeline implementation.

## Author

Bhavani Shree CG
