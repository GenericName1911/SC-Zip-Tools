import os
import sys
from sc_compression.signatures import Signatures
from sc_compression import compress

def process_file(file_path):
    if not os.path.isfile(file_path) or not file_path.endswith((".toml", ".csv", ".sc")):
        return
        
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # Compress with LZMA if not already compressed.
    if not file_data.startswith((b"Sig:", b"]", b"SC")):
        processed_data = compress(file_data, Signatures.LZMA, 3) # Change "LZMA" to "SC" for COC files
        with open(file_path, "wb") as f:
            f.write(processed_data)

if __name__ == "__main__":
    for file_path in sys.argv[1:]: # Loop for multi-file support.
        process_file(file_path)
