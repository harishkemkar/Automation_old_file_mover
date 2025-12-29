import os
import time
import pytest
from file_utils import is_file_older_than, ensure_folder_exists, move_file

def test_is_file_older_than(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("dummy")

    # Set file modified time to 2 days ago
    old_time = time.time() - (2 * 86400)
    os.utime(test_file, (old_time, old_time))

    assert is_file_older_than(str(test_file), 1) is True
    assert is_file_older_than(str(test_file), 3) is False

def test_ensure_folder_exists(tmp_path):
    folder = tmp_path / "new_folder"
    ensure_folder_exists(str(folder))
    assert folder.exists()

def test_move_file(tmp_path):
    source = tmp_path / "source.txt"
    target_dir = tmp_path / "target"
    source.write_text("dummy")
    target_dir.mkdir()

    move_file(str(source), str(target_dir))
    assert (target_dir / "source.txt").exists()