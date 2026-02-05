# =============================================================================
# FILE: file_writer_tool_sql.py
# PURPOSE:
#   Tool function to save generated SQL queries to timestamped text files.
# =============================================================================

import datetime
from pathlib import Path
import sqlite3
import pandas as pd

# ---------------------------------------------------------------------------
# TOOL FUNCTION: write_sql_to_file
# ---------------------------------------------------------------------------
def write_sql_to_file(sql_query: str, folder: str = "output") -> dict:
    """
    Saves a SQL query string to a timestamped .txt file.

    Args:
        sql_query (str): The SQL query string to save.
        folder (str): Folder where the file will be saved. Default is "output".

    Returns:
        dict: Status dictionary with file path and message.
    """

    # Ensure folder exists
    Path(folder).mkdir(exist_ok=True)

    # Create timestamped filename
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f"{folder}/{timestamp}_sql_query.txt"

    try:
        # Write SQL query to file
        Path(filename).write_text(sql_query.strip(), encoding="utf-8")

        return {
            "status": "success",
            "file": filename,
            "message": "SQL query saved successfully."
        }

    except Exception as e:
        return {
            "status": "error",
            "file": filename,
            "message": f"Error: {str(e)}"
        }


def fetch_data_and_save_to_file(
    sql_file_path: str,
    db_file_path: str = "datatechcon.db",
    output_folder: str = "output"
) -> dict:
    """
    Executes a SQL query from a file against a SQLite database and saves the results to a text file.

    Args:
        sql_file_path (str): Path to the .txt file containing the SQL query.
        db_file_path (str): Path to the SQLite database file.
        output_folder (str): Folder to save the results. Default: "output".

    Returns:
        dict: Status dictionary containing file path and message.
    """

    # Ensure output folder exists
    Path(output_folder).mkdir(exist_ok=True)

    # Read SQL query from file
    try:
        sql_query = Path(sql_file_path).read_text(encoding="utf-8").strip()
    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error reading SQL file: {str(e)}"
        }

    # Connect to SQLite database and execute query
    try:
        conn = sqlite3.connect(db_file_path)
        cursor = conn.cursor()
        cursor.execute(sql_query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Fetch column names
        columns = [description[0] for description in cursor.description]

        conn.close()

    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Database query error: {str(e)}"
        }

    # Save results to text file
    try:
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        result_file = f"{output_folder}/{timestamp}_query_results.txt"

        with open(result_file, "w", encoding="utf-8") as f:
            # Write column headers
            f.write("\t".join(columns) + "\n")
            # Write rows
            for row in rows:
                f.write("\t".join(str(item) for item in row) + "\n")

        return {
            "status": "success",
            "file": result_file,
            "message": f"Query executed successfully. {len(rows)} rows saved."
        }

    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error writing results to file: {str(e)}"
        }



def analyze_data_and_save_to_file(
    data_file_path: str,
    intent: str,
    output_folder: str = "output"
) -> dict:
    """
    Performs analysis on a tab-separated data file based on the intent
    and saves the results to a timestamped text file.

    Args:
        data_file_path (str): Path to the tab-separated data file.
        intent (str): Intent label for the type of analysis.
        output_folder (str): Folder to save the results. Default: "output".
    
    intent = intent.upper().strip()

    Returns:
        dict: Status dictionary with file path and message.
    """

    # Ensure output folder exists
    Path(output_folder).mkdir(exist_ok=True)

    # Read data
    try:
        df = pd.read_csv(data_file_path, sep="\t")
    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error reading data file: {str(e)}"
        }

    # Perform analysis based on intent
    try:
        result_df = None

        if intent == "COURSE_SALES":
            if "title" in df.columns and "total_enrollments" in df.columns:
                result_df = df.groupby("title")["total_enrollments"].sum().reset_index()
                result_df = result_df.sort_values("total_enrollments", ascending=False)
            else:
                raise ValueError("Missing required columns for COURSE_SALES")

        elif intent == "ENROLLMENT_ANALYSIS":
            if "total_enrollments" in df.columns:
                result_df = pd.DataFrame({
                    "total_enrollments": [df["total_enrollments"].sum()]
                })
            else:
                result_df = pd.DataFrame({"message": ["No enrollment data found."]})

        elif intent == "INSTRUCTOR_PERFORMANCE":
            if "instructor" in df.columns and "total_enrollments" in df.columns:
                result_df = df.groupby("instructor")["total_enrollments"].sum().reset_index()
                result_df = result_df.sort_values("total_enrollments", ascending=False)
            else:
                raise ValueError("Missing required columns for INSTRUCTOR_PERFORMANCE")

        elif intent == "REVENUE_ANALYSIS":
            if "title" in df.columns and "total_enrollments" in df.columns and "price" in df.columns:
                df["revenue"] = df["total_enrollments"] * df["price"]
                result_df = df.groupby("title")["revenue"].sum().reset_index()
                result_df = result_df.sort_values("revenue", ascending=False)
            elif "title" in df.columns and "price" in df.columns:
                result_df = df[["title", "price"]].sort_values("price", ascending=False)
            else:
                raise ValueError("Missing required columns for REVENUE_ANALYSIS")

        else:  # GENERAL_ANALYTICS or unknown
            result_df = df.describe(include="all").reset_index()

    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error performing analysis: {str(e)}"
        }

    # Save results to text file
    try:
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        result_file = f"{output_folder}/{timestamp}_analysis_results.txt"

        result_df.to_csv(result_file, sep="\t", index=False)

        return {
            "status": "success",
            "file": result_file,
            "message": f"Analysis completed successfully. {len(result_df)} rows saved."
        }

    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error saving analysis results: {str(e)}"
        }


def generate_insights_and_save_to_file(
    analysis_file_path: str,
    intent: str,
    output_folder: str = "output"
) -> dict:
    """
    Generates meaningful insights from analysis results and saves to a text file.

    Args:
        analysis_file_path (str): Path to the analysis results file (tab-separated).
        intent (str): Intent label to guide insight generation.
        output_folder (str): Folder to save insights file. Default: "output".
    
    intent = intent.upper().strip()

    Returns:
        dict: Status dictionary with file path and message.
    """

    # Ensure output folder exists
    Path(output_folder).mkdir(exist_ok=True)

    # Read analysis results
    try:
        df = pd.read_csv(analysis_file_path, sep="\t")
    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error reading analysis file: {str(e)}"
        }

    # Generate insights
    try:
        insights = []

        if df.empty:
            insights.append("No data available for generating insights.")
        else:
            if intent == "COURSE_SALES":
                top_course = df.iloc[0]
                insights.append(f"The top-selling course is '{top_course['title']}' with {top_course['total_enrollments']} enrollments.")
                insights.append("Complete course sales ranking:")
                for idx, row in df.iterrows():
                    insights.append(f"{idx+1}. {row['title']}: {row['total_enrollments']} enrollments")

            elif intent == "ENROLLMENT_ANALYSIS":
                total_enrollments = df["total_enrollments"].sum() if "total_enrollments" in df.columns else 0
                insights.append(f"Total enrollments across all courses: {total_enrollments}")

            elif intent == "INSTRUCTOR_PERFORMANCE":
                top_instructor = df.iloc[0]
                insights.append(f"The best-performing instructor is '{top_instructor['instructor']}' with {top_instructor['total_enrollments']} enrollments.")
                insights.append("Instructor performance ranking:")
                for idx, row in df.iterrows():
                    insights.append(f"{idx+1}. {row['instructor']}: {row['total_enrollments']} enrollments")

            elif intent == "REVENUE_ANALYSIS":
                top_course = df.iloc[0]
                if "revenue" in df.columns:
                    insights.append(f"The course generating the highest revenue is '{top_course['title']}' with total revenue of {top_course['revenue']}.")
                    insights.append("Revenue breakdown by course:")
                    for idx, row in df.iterrows():
                        insights.append(f"{idx+1}. {row['title']}: {row['revenue']}")
                elif "price" in df.columns:
                     insights.append(f"The most expensive course is '{top_course['title']}' priced at {top_course['price']}.")
                     insights.append("Price ranking:")
                     for idx, row in df.iterrows():
                         insights.append(f"{idx+1}. {row['title']}: {row['price']}")

            else:  # GENERAL_ANALYTICS
                insights.append("Summary of analysis:")
                for col in df.columns:
                    insights.append(f"{col}: {df[col].iloc[0] if not df[col].empty else 'N/A'}")

        # Save insights to file
        timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        insights_file = f"{output_folder}/{timestamp}_insights.txt"

        with open(insights_file, "w", encoding="utf-8") as f:
            for line in insights:
                f.write(line + "\n")

        return {
            "status": "success",
            "file": insights_file,
            "message": f"Insights generated successfully. Content: {' '.join(insights)}",
            "insights": insights
        }

    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error generating insights: {str(e)}"
        }

def read_file_content(file_path: str) -> dict:
    """
    Reads the content of a text-based file (e.g., SQL results) and returns it as a string.
    
    Args:
        file_path (str): Path to the file to read.
        
    Returns:
        dict: Status dictionary with content or error message.
    """
    try:
        content = Path(file_path).read_text(encoding="utf-8")
        return {
            "status": "success",
            "content": content,
            "message": "File read successfully."
        }
    except Exception as e:
        return {
            "status": "error",
            "content": None,
            "message": f"Error reading file {file_path}: {str(e)}"
        }

def save_text_file(content: str, filename_prefix: str = "analysis", output_folder: str = "output") -> dict:
    """
    Saves a string content to a timestamped text file.
    
    Args:
        content (str): Text content to save.
        filename_prefix (str): Prefix for the filename (e.g., 'analysis', 'insights').
        output_folder (str): Folder to save the file.
        
    Returns:
        dict: Status dictionary with file path.
    """
    # Ensure output folder exists
    Path(output_folder).mkdir(exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = f"{output_folder}/{timestamp}_{filename_prefix}.txt"
    
    try:
        Path(filename).write_text(content, encoding="utf-8")
        return {
            "status": "success",
            "file": filename,
            "message": f"File saved successfully to {filename}"
        }
    except Exception as e:
        return {
            "status": "error",
            "file": None,
            "message": f"Error saving file: {str(e)}"
        }