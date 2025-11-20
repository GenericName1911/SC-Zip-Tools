import os
import tkinter as tk
from tkinter import filedialog
from sc_compression import decompress as decompress_data

root = tk.Tk()
root.withdraw()

for path in filedialog.askopenfilenames():
    if not os.path.isfile(path):
        continue
    if not path.endswith((".toml", ".sc", ".csv")):
        continue

    with open(path, "rb") as f:
        data = f.read()

    out, *extra_data = decompress_data(data)

    with open(path, "wb") as f:
        f.write(out)
      
