import os
import numpy as np
import pandas as pd
import csv
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


def matrix_of_occurrence(vocabulary, results_file_path, matrix_path, hits_path):
    """
    Generates a matrix of occurrence based on a given vocabulary and patient results.

    Args:
        vocabulary (list): List of words to be considered in the occurrence matrix.
        results_file_path (str): Path to the CSV file containing patient results.
        matrix_path (str): Path to save the generated occurrence matrix as a CSV file.
        hits_path (str): Path to save the ordered list of vocabulary words based on hits.

    Returns:
        None
    """
    patients_results = []

    with open(results_file_path, 'r', encoding='utf-8') as csv_file:
        csv_writer = csv.reader(csv_file)
        for line in csv_writer:
            patient_name = line[0].strip()
            patient_tokens = line[1].strip().split(', ')
            patients_results.append({'nom': patient_name, 'tokens': patient_tokens})

    # Initialize the matrix with zeros
    occurrence_matrix = np.zeros((len(patients_results), len(vocabulary)), dtype=int)

    columns = []
    for k in vocabulary:
        columns.append(k)

    columns.append('Tokens')

    rows = []
    # Browse patients
    for i, patient in enumerate(patients_results):
        # Browse patient tokens
        rows.append(patient['nom'])
        for j, word in enumerate(vocabulary):
            # Count occurrences of the word in the patient's token list
            occurrence_matrix[i, j] += patient['tokens'].count(word)

    rows.append("Total")

    # Add an additional column containing the number of tokens per patient
    occurrence_matrix = np.column_stack((occurrence_matrix, np.sum(occurrence_matrix, axis=1)))

    # Add an extra line containing the number of occurrences per vocabulary word
    occurrence_matrix = np.vstack((occurrence_matrix, np.sum(occurrence_matrix, axis=0)))

    # Create an ordered list of vocabulary words sorted by descending hits
    hits_by_word = dict(zip(vocabulary, occurrence_matrix[-1, :-1]))
    words_ordered_by_hits = [word for word, hits in
                            sorted(hits_by_word.items(), key=lambda item: item[1], reverse=True)]

    # Save the matrix as a CSV file
    # np.savetxt(matrix_path, occurrence_matrix, delimiter=',', fmt='%d')
    df = pd.DataFrame(occurrence_matrix, index=rows, columns=columns)
    df.to_csv(matrix_path, index=True, header=True, sep=',', encoding='utf-8')

    # Save the ordered list of vocabulary words as a CSV file
    with open(hits_path, 'w', newline='', encoding='utf-8') as hits_csv_file:
        writer_hits = csv.writer(hits_csv_file)
        for word in words_ordered_by_hits:
            writer_hits.writerow([word])
