import os
import hashlib


def find_duplicates(directory):
    """Finds duplicate files in a directory and its subdirectories.

    Args:
        directory: The directory to search for duplicates.

    Returns:
        A dictionary where keys are file hashes and values are lists of duplicate file paths.
    """

    hashes = {}
    duplicates = {}

    for root, subdirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            # Calculate the hash of the file
            try:
                with open(filepath, "rb") as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
            except IOError as e:
                print(f"Error reading file {filepath}: {e}")
                continue

            # Check if the hash is already in the dictionary
            if file_hash in hashes:
                duplicates.setdefault(file_hash, []).append(filepath)
            else:
                hashes[file_hash] = filepath

    return duplicates


# Example usage:
directory_to_scan = "C:\SYNOLOGY\CODING\Chat Exports"

duplicates = find_duplicates(directory_to_scan)

if duplicates:
    print("Duplicate files found:")
    for file_hash, file_paths in duplicates.items():
        print(f"- Hash: {file_hash}")
        for file_path in file_paths:
            print(f"  - {file_path}")
else:
    print("No duplicate files found.")
