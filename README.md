
# Duplicate File Remover Script

This Python script helps you find and manage duplicate files within a specified directory and its subdirectories.

## Prerequisites

- Python 3.x installed on your system.

## Usage

Follow these steps to use the script:

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your_username/duplicate-file-remover.git
   ```

2. **Navigate to the Script Directory**

   Move into the directory containing the script:

   ```bash
   cd duplicate-file-remover
   ```

3. **Run the Script**

   Execute the Python script by running the following command:

   ```bash
   python duplicate_remover.py
   ```

4. **Enter the Directory Path**

   When prompted, enter the full path of the directory you want to search for duplicate files.

   Example:
   ```
   Enter the directory to search for duplicates: /path/to/your/directory
   ```

5. **Review Duplicate Files**

   The script will display a list of duplicate files found within the specified directory and its subdirectories.

6. **Move Duplicates to a Separate Directory**

   The script will create a directory named "duplicates_found" within the specified directory (if it doesn't already exist) and move the duplicate files into that directory, leaving the original files intact.

7. **Review Results**

   Once the process is complete, you can review the duplicate files moved to the "duplicates_found" directory.

## Additional Notes

- The script uses cryptographic hashing to determine file duplicates based on content.
- Please ensure you have sufficient permissions to read, write, and move files within the specified directory.
- It's recommended to review the duplicate files before taking any further action.

---

Feel free to customize this README file based on your specific project requirements and preferences.