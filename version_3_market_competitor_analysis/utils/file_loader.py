# =============================================================================
# FILE: file_loader.py
# PURPOSE:
#   Utility function to load instruction and description files from disk.
# =============================================================================

from pathlib import Path


def load_instructions_file(file_path: str) -> str:
    """
    Loads the content of an instructions or description file.

    Args:
        file_path (str): Relative or absolute path to the file.

    Returns:
        str: The file content as a string.
    """
    try:
        path = Path(file_path)
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"Error: File not found at {file_path}"
    except Exception as e:
        return f"Error loading file: {str(e)}"
