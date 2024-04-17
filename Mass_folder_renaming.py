import os

def rename_folders(path):
    for folder in os.listdir(path):  # Loop through each item in the specified directory
        folder_path = os.path.join(path, folder)  # Get the full path of the current item

        if os.path.isdir(folder_path):  # Check if the item is a directory
            files = os.listdir(folder_path)  # Get a list of files inside the directory
            if files:  # Check if there are files inside the directory
                first_file = files[0]  # Get the name of the first file
                name_parts = first_file.split("_")  # Split the file name by underscores
                new_folder_name = name_parts[0]  # Take only the first part before the first underscore as the new folder name
                new_folder_path = os.path.join(path, new_folder_name)  # Construct the new folder path

                if os.path.exists(new_folder_path):  # Check if the new folder name already exists
                    suffix = 1
                    while True:
                        new_folder_path = os.path.join(path, f"{new_folder_name}_{suffix}")  # Append a suffix to the new folder name
                        if not os.path.exists(new_folder_path):  # Check if the new folder path with the suffix does not exist
                            break
                        suffix += 1  # Increment the suffix if the new folder path already exists
                
                os.rename(folder_path, new_folder_path)  # Rename the folder to the new folder path
                print(f"Renamed '{folder}' to '{os.path.basename(new_folder_path)}'")  # Print a message indicating the renaming
                
            else:
                print(f"No files found in directory '{folder}'")  # Print a message if no files are found in the directory
        else:
            print(f"'{folder}' is not a directory")  # Print a message if the item is not a directory


folder_path = 'F:\\Scripting\\assets\\Assets'  # Specify the directory path
rename_folders(folder_path)  # Call the function to rename folders within the directory
