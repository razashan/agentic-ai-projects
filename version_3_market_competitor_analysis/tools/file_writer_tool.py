# =============================================================================
# FILE: file_writer_tool.py
# PURPOSE:
#   This module defines a tool function for writing HTML reports to file.
#   Used by agents to persist generated competitive analysis reports.
# =============================================================================

import datetime
from pathlib import Path


# -----------------------------------------------------------------------------
# TOOL FUNCTION: write_to_file
# -----------------------------------------------------------------------------
def write_to_file(content: str) -> dict:
    """
    Writes the given HTML content to a timestamped HTML file.

    Args:
        content (str): Full HTML content as a string to be saved to disk.

    Returns:
        dict: A dictionary containing the status and generated filename.
    """

    # Get the current date and time, format it as YYMMDD_HHMMSS.
    timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # Construct the output filename using the timestamp.
    filename = f"output/{timestamp}_competitive_analysis_report.html"

    # Ensure the "output" directory exists.
    Path("output").mkdir(exist_ok=True)

    # Write the HTML content to the constructed file.
    Path(filename).write_text(content, encoding="utf-8")

    # Return a dictionary indicating success, and the filename that was written.
    return {
        "status": "success",
        "file": filename
    }
