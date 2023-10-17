# Importing libraries
import os
import shutil
import time

# Get the source directory path from user input
source_dir = input("Enter the path: ")

# Check if the provided path exists and is a directory
if os.path.exists(source_dir) and os.path.isdir(source_dir):
    while True:
        # List all files in the source directory
        files = os.listdir(source_dir)

        # Iterate through the files in the source directory
        for file in files:
            if os.path.isfile(os.path.join(source_dir, file)):
                # Split the file name and extension
                filename, extension = os.path.splitext(file)
                extension = extension[1:]  # Remove the dot from the extension

                # Check if a directory for the file's extension exists
                if os.path.exists(os.path.join(source_dir, extension)):
                    # Move the file to its respective extension directory
                    shutil.move(os.path.join(source_dir, file), os.path.join(source_dir, extension, file))
                else:
                    # If the directory does not exist, create it and move the file
                    os.makedirs(os.path.join(source_dir, extension))
                    shutil.move(os.path.join(source_dir, file), os.path.join(source_dir, extension, file))

                # Print a message for the moved files 
                print(f"Moved '{file}' to '{extension}'")

        # checking after every 10 seconds.
        time.sleep(10) 
else:
    print("The provided path is not a valid directory.")
