from file_utils import process_folder
from file_utils import move_files_by_extension
import os


#def main():
       #days_old = 30              # configurable threshold

    #print(f"Scanning '{source_folder}' for files older than {days_old} days...")
    #process_folder(source_folder, target_folder, days_old)


    # Move all `.log` files regardless of age
    #print(f"Scanning '{source_folder}' for .txt files ...")
    
    #move_files_by_extension(source_folder, target_folder, extension=".pdf")



# def main():
   
#     source_folder = input("Enter the source folder path: ").strip()
#     target_folder = input("Enter the target folder path: ").strip()



#     print("Choose an option:")
#     print("1. Move files older than N days")
#     print("2. Move files with a specific extension")

#     choice = input("Enter 1 or 2: ").strip()

#     if choice == "1":
#         days_old = int(input("Enter number of days: ").strip())
#         print(f"Scanning '{source_folder}' for files older than {days_old} days...")
#         process_folder(source_folder, target_folder, days_old)

#     elif choice == "2":
#         extension = input("Enter file extension (e.g. .txt, .log, .pdf): ").strip()
#         print(f"Scanning '{source_folder}' for {extension} files...")
#         move_files_by_extension(source_folder, target_folder, extension)

#     else:
#         print("Invalid choice. Please run again.")



def main():
    # Default paths
    default_source = "Source"
    default_target = "Target"

    while True:
        print("\n--- File Management Menu ---")
        print("1. Move files older than N days")
        print("2. Move files with a specific extension")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "3":
            print("Exiting program. Goodbye!")
            break

        # Ask for source and target folders, with defaults
        source_folder = input(f"Enter source folder path (default: {default_source}): ").strip()
        if not source_folder:
            source_folder = default_source

        target_folder = input(f"Enter target folder path (default: {default_target}): ").strip()
        if not target_folder:
            target_folder = default_target

        # Validate source folder
        if not os.path.exists(source_folder):
            print(f"Source folder '{source_folder}' does not exist. Try again.")
            continue

        if choice == "1":
            days_old = int(input("Enter number of days: ").strip())
            print(f"Scanning '{source_folder}' for files older than {days_old} days...")
            process_folder(source_folder, target_folder, days_old)

        elif choice == "2":
            extension = input("Enter file extension (e.g. .txt, .log, .pdf): ").strip()
            print(f"Scanning '{source_folder}' for {extension} files...")
            move_files_by_extension(source_folder, target_folder, extension)

        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()