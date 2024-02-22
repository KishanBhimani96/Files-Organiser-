
# Download Organiser Script

## Overview
The Download Organiser Script is a Python-based automation tool designed to monitor a specified folder (e.g., Downloads) and automatically organise files into designated subfolders based on their file type. This script aims to reduce digital clutter, enhance productivity, and maintain an organised digital workspace by categorising files into appropriate folders like Images, Documents, etc., without manual intervention.

## Features
- **Real-time Monitoring**: Watches for new files in the specified directory and organises them as soon as they appear.
- **Customisable File Handling**: Easily adjustable rules for which file types get moved to which directories.
- **Support for Multiple File Types**: Includes default handling for common file types such as images (JPEG, PNG) and documents (PDF, DOCX), with the flexibility to add more.
- **Automatic Folder Creation**: If the designated folder for a specific file type doesn't exist, the script creates it automatically.

## Requirements
- Python 3.x
- `watchdog` Python package for monitoring directory changes.

## Installation
1. **Ensure Python 3.x is Installed**: This script requires Python 3. Ensure you have it installed by running `python --version` in your command line.
2. **Install Dependencies**: Install the `watchdog` package using pip:
   ```
   pip install watchdog
   ```

## Configuration
Before running the script, configure the `folder_to_track` and `folder_destinations` variables in the script to match your desired folders.

- `folder_to_track`: This should be the path to the folder you want to monitor (e.g., your Downloads folder).
- `folder_destinations`: This is a dictionary mapping file extensions to the folders where files of that type should be moved.

Example configuration:
```python
folder_to_track = '/Users/yourname/Downloads'
folder_destinations = {
    'jpeg': '/Users/yourname/Pictures',
    'jpg': '/Users/yourname/Pictures',
    'png': '/Users/yourname/Pictures',
    'heic': '/Users/yourname/Pictures',
    'gif': '/Users/yourname/Pictures',
    'pdf': '/Users/yourname/Documents',
    'docx': '/Users/yourname/Documents',
}
```

## Usage
To run the script, navigate to the script's directory in your terminal or command prompt and execute:
```
python organize_downloads.py
```
The script will continue running in the background, monitoring the specified folder and organising new files according to the defined rules.

## Contributing
Contributions to enhance the functionality, add new features, or improve the efficiency of the Download Organiser Script are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE.md).
