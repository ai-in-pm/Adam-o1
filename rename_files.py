import os
import re
import shutil

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        # Process files with "archon" in their name
        for file in files:
            if 'archon' in file.lower():
                old_path = os.path.join(root, file)
                new_name = file.replace('archon', 'adam-o1')
                new_path = os.path.join(root, new_name)
                print(f"Renaming file: {old_path} -> {new_path}")
                
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"Error renaming file {old_path}: {str(e)}")

if __name__ == "__main__":
    base_dir = r"C:\CC-WorkingDir\Adam-o1-main"
    rename_files(base_dir)
    print("File renaming completed!")
