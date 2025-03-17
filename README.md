# OSINT-Exiftool-Automation

OSINT-Exiftool-Automation is designed to monitor a specific folder and extract metadata from files uploaded there. The metadata is then saved to a text file, and the original file is moved to a results folder.


## CONFIGURATION
Before launching the program, ensure the following are configured correctly:

- The path to the folder to be monitored is specified in the WATCH_FOLDER variable.
- The path to the exiftool.exe executable is specified in the EXIFTOOL_PATH variable.
- The results folder is automatically created if it does not exist.

## Notes
- Make sure the exiftool.exe executable is installed and configured correctly on your system.
- The program uses the watchdog library to monitor the folder, which can consume system resources.
- The program deletes the original files after moving them to the results folder. Make sure you configure the results folder correctly to avoid data loss.

## HOW IT WORKS
The program uses the watchdog library to monitor the specified folder.

When a new file is created in the folder, the program is triggered and executes the on_created method.

The on_created method checks if the file is a file (and not a folder) and calls the process_file method if so.

The process_file method retrieves the file's metadata using the exiftool.exe executable.

The metadata is then saved to a text file in the results folder.

The original file is moved to the results folder and deleted from its original location.

## INSTALLATION
Run ```pip install -r requierements.txt``` to install the project dependencies.


## START THE PROGRAM
To launch the program, run the Python script with : ``` python ./osint_exiftool_automation.py ```
The program will launch and begin monitoring the specified folder.