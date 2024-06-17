# NASA Data Download Script

## Overview
This script automates the process of downloading specific files from a given NASA webpage. It targets files with names containing "Eflux_e,all.txt" and saves them to a specified local directory.

## Requirements
- Python 3.9
- `requests` library
- `beautifulsoup4` library

## Usage
1. **Initial Setup:**
    - Set the `initial_url` to the target webpage.
    - Set the `file_folder` to the desired local directory for saving the downloaded files.

## Script Details
- **Fetching the Webpage:** The script sends a GET request to the specified `initial_url` to retrieve its content.
- **Parsing HTML:** It uses BeautifulSoup to parse the HTML content of the webpage.
- **Finding Links:** The script searches for all `<a>` tags where the `href` attribute contains "Eflux_e,all.txt".
- **Downloading Files:** For each found link, the script:
  - Constructs the file URL.
  - Downloads the file content.
  - Saves the file to the specified directory with its original name.
- **Completion Message:** Once all files are downloaded, the script prints a confirmation message.

## File Structure
- **initial_url:** The URL of the webpage containing the download links.
- **file_folder:** The directory path where downloaded files will be saved.
