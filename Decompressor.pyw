import os
import sys
from sc_compression import decompress as decompress_data

def process_file(file_path):
    
    if not os.path.isfile(file_path) or not file_path.endswith((".toml", ".csv")):
        return
        
    with open(file_path, "rb") as f:
        file_data = f.read()
        processed_data, *extra_data = decompress_data(file_data)  
        
    with open(file_path, "wb") as f:
        f.write(processed_data)
        
if __name__ == "__main__":
    for file_path in sys.argv[1:]:
        process_file(file_path)