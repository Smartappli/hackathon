import os
from utils.reader_writer import read_vocabulary_file


def create_or_recover_vocabulary(file_path):
    """
    Creates or retrieves the vocabulary list from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.
    - verbose (bool, optional): Indicates whether to display detailed messages. Defaults to False.

    Returns:
    - set: A set containing the words in the CSV file, or an empty set if the file doesn't exist.
    """
    if os.path.exists(file_path):
        # The file exists, process and create the vocabulary list
        vocabulary_list = read_vocabulary_file(file_path)
    else:
        # File does not exist, create an empty list
        vocabulary_list = []

    return set(vocabulary_list)


def number_of_patients_and_files(root_directory):
    """
    Count the number of patient directories and total files within those directories.

    Parameters:
    - root_directory (str): The root directory containing patient subdirectories.

    Returns:
    - tuple: A tuple containing two values:
        - total_directories (int): The total number of patient directories.
        - total_files (int): The total number of files across all patient directories.
    """

    total_files = 0
    total_directories = 0

    # Browse patient directories
    for patient in os.listdir(root_directory):
        patient_directory_path = os.path.join(root_directory, patient)

        # Check if the item in the directory is a folder
        if os.path.isdir(patient_directory_path):
            # Count the total number of files in the patient's subdirectory
            total_directories += 1
            total_files += len \
                ([f for f in os.listdir(patient_directory_path) if
                  os.path.isfile(os.path.join(patient_directory_path, f))])

    return total_directories, total_files
