# Data Processing Script

## Overview
This script processes IMF (data of solarwind source, OMNI) and eFlux data files, combines them based on matching date and time information, and exports the combined data into an Excel file.

## Requirements
- Python 3.9
- `pandas` library
- `openpyxl` library
- `numpy` library
- `re` library

## Usage
1. **Initial Setup:**
    - Ensure the IMF and eFlux files are placed in the specified directories.
    - Update `file_dir_eFlux` and `file_dir_main` with the appropriate file paths.

## Script Details
- **Functions:**
  - `number_to_string(num)`: Converts a number to a zero-padded string.
  - `list_files_in_directory(directory)`: Lists and sorts files in a directory.
  - `read_eflux_file(file)`: Reads an eFlux file into a DataFrame.
  - `read_IMF_file()`: Reads the IMF file into a DataFrame.
  - `df_to_openpyxl(dataframe, workbook)`: Converts a DataFrame to an openpyxl worksheet.
  - `namedtuples_to_array(namedtuples)`: Converts namedtuple to a numpy array.
  - `extract_time(s)`: Extracts time from a string using regex.
  - `extract_datetime_info(string)`: Extracts date and time information from a string using regex.

- **Processing Flow:**
  1. **Initialize Excel Workbook:** Creates an empty workbook with defined column headers.
  2. **Read IMF Data:** Reads the IMF data file into a DataFrame.
  3. **List eFlux Files:** Lists all eFlux files in the specified directory.
  4. **Process Each eFlux File:**
     - Extracts date and time information from the filename.
     - Filters the IMF DataFrame for matching date and time records.
     - Reads the eFlux file into a DataFrame.
     - Combines the IMF and eFlux data row by row.
  5. **Save Excel File:** Saves the combined data into an Excel file.

## Output
- The script generates an Excel file named `test.xlsx` in the specified output directory (`file_dir_main`).

This README provides a concise overview of the script's functionality, requirements, usage, and processing details. Ensure the directories and file paths are correctly specified before running the script.