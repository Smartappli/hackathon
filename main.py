# medHackathon
# Proof of Concept
# 20 January 2024
# Repository: https://github.com/Smartappli/hackathon.git
# Discord:

import os
import spacy
from utils.reader_writer import read_results_file
from utils.file_operation import create_or_recover_vocabulary, number_of_patients_and_files

# Parameters

verbose = True

vocabulary_file = "vocabulary.csv"
vocabulary_file_path = os.path.join(os.getcwd(), vocabulary_file)
results_file = "results.csv"
results_file_path = os.path.join(os.getcwd(), results_file)
patients_directory_name = 'patients'
patients_root_directory = os.path.join(os.getcwd(), patients_directory_name)

# Functions Definition
nlp = spacy.load('fr_core_news_sm', disable=['ner', 'textcat'])

# Main
print("Step 1 - Vocabulary File Reading or Creation.")

if verbose:
    print(f"-----> Vocabulary file path: {vocabulary_file_path}")

vocabulary = create_or_recover_vocabulary(vocabulary_file_path)

if verbose:
    if len(vocabulary) > 0:
        print("-----> The vocabulary file has been found.")
        print(f"-----> Vocabulary Set: {vocabulary}")
    else:
        print(" -----> The dictionary file does not exist.")

print("\nStep 2 - Counting the number of files to be processed.")

if verbose:
    print(f"-----> Patients Directory: {patients_root_directory}")

total_directories, total_files = number_of_patients_and_files(patients_root_directory)

if verbose:
    print(f"-----> The number of patients to be treated: {total_directories}")
    print(f"-----> The number of files to be processed: {total_files}")

print("\nStep 3 - Step 1 - Results File Reading or Creation.")

if verbose:
    print(f"-----> Results file path: {results_file_path}")

    results = read_results_file(results_file_path)

if verbose:
    if len(results) > 0:
        print("-----> The vocabulary file has been found.")
        print(f"-----> Results Set: {results}")
    else:
        print("-----> The dictionary file does not exist.")

print("\nStep 4 - Identification of patient directories to be processed")
patients_path = [os.path.join(patients_root_directory, patient) for patient in os.listdir(patients_root_directory) if os.path.isdir(os.path.join(patients_root_directory, patient))]
if verbose:
    print (f"-----> Patient directories to be processed: {patients_path}")

print("\nStep 5 - Patients Processing")

