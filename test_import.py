import sys
print("Python Path:", sys.path)

try:
    import adam_o1
    print("Successfully imported adam_o1")
except ImportError as e:
    print(f"Import Error: {e}")
    
try:
    from adam_o1 import adam_o1_graph
    print("Successfully imported adam_o1_graph")
except ImportError as e:
    print(f"Import Error: {e}")
