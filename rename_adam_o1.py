import os
import re
import shutil

def replace_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        # Replace "Adam-o1" with "Adam-o1" (case-sensitive)
        content = content.replace('Adam-o1', 'Adam-o1')
        # Replace "adam-o1" with "adam-o1" (case-sensitive)
        content = content.replace('adam-o1', 'adam-o1')
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Processed file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        # Process files
        for file in files:
            if file.endswith(('.py', '.md', '.txt', '.json', '.html', '.js', '.css', '.bat', '.sh', '.ps1', '.example')):
                file_path = os.path.join(root, file)
                replace_in_file(file_path)
        
        # Handle directories with "adam-o1" in their name
        for i, dir_name in enumerate(dirs):
            if 'adam-o1' in dir_name.lower():
                old_path = os.path.join(root, dir_name)
                new_name = dir_name.replace('adam-o1', 'adam-o1')
                new_path = os.path.join(root, new_name)
                print(f"Renaming directory: {old_path} -> {new_path}")
                
                # Need to update the dirs list too to avoid issues with os.walk
                dirs[i] = new_name
                
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"Error renaming directory {old_path}: {str(e)}")

if __name__ == "__main__":
    base_dir = r"C:\CC-WorkingDir\Adam-o1-main"
    process_directory(base_dir)
    print("Replacement completed!")
