# medHackathon
# Proof of Concept
# 20 January 2024
# Repository: https://github.com/Smartappli/hackathon.git
# Discord:

import os
from utils.reader_writer import read_vocabulary_file
from utils.file_operation import number_of_patients_and_files

# Parameters

verbose = True

vocabulary_file = "vocabulary.csv"
vocabulary_file_path = os.path.join(os.getcwd(), vocabulary_file)
patients_directory_name = 'patients' #  Répertoire contenant l'ensemble des répertoires patient
repertoire_patients = os.path.join(os.getcwd(), patients_directory_name)

# Functions Definition
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
        if verbose:
            print("-----> The vocabulary file has been found.")

        vocabulary_list = read_vocabulary_file(file_path)
    else:
        # File does not exist, create an empty list
        if verbose:
            print(" -----> The dictionary file does not exist.")

        vocabulary_list = []

    return set(vocabulary_list)


if verbose == True:
    print("Step 1 - Vocabulary File Reading or Creation.")
    print(f"-----> Vocabulary file path: {vocabulary_file_path}")
    vocabulary = create_or_recover_vocabulary(vocabulary_file_path)
    print(f"-----> Vocabulary Set: {vocabulary}")

    print ("Step 2 - Counting the number of files to be processed.")
    print(f"-----> Patients Directory: {repertoire_patients}")
    total_directories, total_files = number_of_patients_and_files(repertoire_patients)
    print(f"-----> The number of patients to be treated: {total_directories}")
    print(f"-----> The number of files to be processed: {total_files}")

