# Simple script to test if we can import and run the Adam-o1 app
import os
import sys

print("Current directory:", os.getcwd())
print("Python path:", sys.path)

try:
    import streamlit
    print("Streamlit imported successfully")
except ImportError as e:
    print(f"Error importing streamlit: {e}")

try:
    import adam_o1
    print("adam_o1 imported successfully")
except ImportError as e:
    print(f"Error importing adam_o1: {e}")

print("All imports successful. You can now run the Adam-o1 application with:")
print("streamlit run streamlit_ui.py")
