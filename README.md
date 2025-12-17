# SC-Zip-Tools

These tools are used for compressing/decompressing Supercell's game assets, _specifically_ for CSV and TOML files. Just drag and drop the files onto the tool (OR use it via CLI arguments), and it will do the work for you. Make sure to run `setup.py` before using any scripts!

The `.pyw` ([python no-console extension](https://docs.python.org/2/using/windows.html#executing-scripts)) file should be run using `Python`. It has been used to prevent unnecessary console flashing. If you are unable to run `.pyw` files, rename them to `.py` . Requires Python version >=3.5

For any errors or feedback, feel free to message me anytime on discord `@generic_name_1911`.

## Usage:

A. **Drag 'N Drop:** Self explanatory. Also works through CLI.

B. **File Explorer:** Double click the script to open file explorer to select files. Use it if DND doesn't work.

## Features:

- The tool is **Cross-Platform**. That is, it works on all major operating systems like Windows, macOS, and Linux.
- Supports **Batch Conversion**. You can use it to convert multiple files at once.
- **Same Directory** output. The script saves the decompressed files in the same folder as the originals, no matter where you run it from.
- **Open Source**. Licensed under GNU GPLv3.
- **Supported compression formats** (from sc-compression):
  - LZMA
  - SC
  - SCLZ
  - SIG
  - ZSTD

## Credits:

- This tool relies on [sc-compression by danila-schelkov](https://github.com/danila-schelkov/sc-compression)

## Licensing Notice:

```
Copyright (C) 2024 generic_name_1911

This program is free software: You can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```