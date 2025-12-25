import os
import shutil
import time

def ensure_folder_exists(folder_path: str) -> None:
    """Ensure the target folder exists, create if missing."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def is_file_older_than(file_path: str, days: int) -> bool:
    """Check if a file is older than given number of days."""
    cutoff = time.time() - (days * 86400)  # seconds in days
    file_mtime = os.path.getmtime(file_path)
    return file_mtime < cutoff

def move_file(file_path: str, target_folder: str) -> None:
    """Move a file to target folder."""
    shutil.move(file_path, target_folder)
    print(f"Moved: {file_path} -> {target_folder}")

def process_folder(source_folder: str, target_folder: str, days: int) -> None:
    """Process all files in source_folder and move those older than `days`."""
    ensure_folder_exists(target_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path) and is_file_older_than(file_path, days):
            move_file(file_path, target_folder)


def move_files_by_extension(source_folder: str, target_folder: str, extension: str) -> None:
    """
    Move all files with the given extension from source_folder to target_folder.
    Example: extension=".txt" or extension=".log"
    """
    ensure_folder_exists(target_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if it's a file and matches extension
        if os.path.isfile(file_path) and filename.lower().endswith(extension.lower()):
            try:
                move_file(file_path, target_folder)
            except Exception as e:
                print(f"Error moving {file_path}: {e}")

                