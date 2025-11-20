import os
import tkinter as tk
from tkinter import filedialog
from sc_compression.signatures import Signatures
from sc_compression import compress

root = tk.Tk()
root.withdraw()

for path in filedialog.askopenfilenames():
    if not os.path.isfile(path):
        continue
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".toml", ".csv", ".sc"):
        continue

    with open(path, "rb") as f:
        data = f.read()

    if data.startswith((b"Sig:", b"]", b"SC")):
        continue
        
    out = compress(data, Signatures.SC if ext == ".sc" else Signatures.LZMA, 3)

    with open(path, "wb") as f:
        f.write(out)
