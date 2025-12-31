from flask import Flask, request, render_template, redirect, url_for, flash
import os
from file_utils import process_folder, move_files_by_extension

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

# Default paths
DEFAULT_SOURCE = "Source"
DEFAULT_TARGET = "Target"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = request.form.get("choice")
        source_folder = request.form.get("source_folder") or DEFAULT_SOURCE
        target_folder = request.form.get("target_folder") or DEFAULT_TARGET

        # Validate source folder
        if not os.path.exists(source_folder):
            flash(f"Source folder '{source_folder}' does not exist.")
            return redirect(url_for("index"))

        if choice == "1":  # Move files older than N days
            days_old = int(request.form.get("days_old"))
            process_folder(source_folder, target_folder, days_old)
            flash(f"Moved files older than {days_old} days from {source_folder} to {target_folder}")

        elif choice == "2":  # Move files by extension
            extension = request.form.get("extension")
            move_files_by_extension(source_folder, target_folder, extension)
            flash(f"Moved {extension} files from {source_folder} to {target_folder}")

        else:
            flash("Invalid choice. Please try again.")

        return redirect(url_for("index"))

    return render_template("index.html")
    


if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000, debug=True)

    