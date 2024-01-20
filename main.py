# medHackathon
# Proof of Concept
# 20 January 2024
# Repository: https://github.com/Smartappli/hackathon.git
# Discord:

import os

from utils.file_operation import create_or_recover_vocabulary, number_of_patients_and_files

# Parameters

verbose = True

vocabulary_file = "vocabulary.csv"
vocabulary_file_path = os.path.join(os.getcwd(), vocabulary_file)
patients_directory_name = 'patients' #  Répertoire contenant l'ensemble des répertoires patient
repertoire_patients = os.path.join(os.getcwd(), patients_directory_name)

# Functions Definition



if verbose == True:
    print("Step 1 - Vocabulary File Reading or Creation.")
    print(f"-----> Vocabulary file path: {vocabulary_file_path}")
    vocabulary = create_or_recover_vocabulary(vocabulary_file_path)
    if len(vocabulary) > 0:
        print("-----> The vocabulary file has been found.")
        print(f"-----> Vocabulary Set: {vocabulary}")
    else:
        print(" -----> The dictionary file does not exist.")

    print("\nStep 2 - Counting the number of files to be processed.")
    print(f"-----> Patients Directory: {repertoire_patients}")
    total_directories, total_files = number_of_patients_and_files(repertoire_patients)
    print(f"-----> The number of patients to be treated: {total_directories}")
    print(f"-----> The number of files to be processed: {total_files}")

    print("\nStep 3 - Traitement des fichiers des patients.")

