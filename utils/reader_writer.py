import os
import csv


def read_vocabulary_file(file_path):
    """
    Reads a CSV file and returns a list of words.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - list: A list containing the words in the CSV file, with no spaces around them.
    """
    vocabulary = []

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            # Remove white space around words
            word = line[0].strip()
            vocabulary.append(word)

    return vocabulary


def read_results_file(file_path):
    """
    Load single-token sets per patient from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file containing patient and token data.

    Returns:
    - dict: A dictionary where keys are patient identifiers and values are sets
            containing existing single tokens for each patient.
            Example: {'patient1': {'token1', 'token2'}, 'patient2': {'token3', 'token4'}, ...}

    Note:
    - The CSV file should have two columns: 'patient' and 'existing_tokens'.
    - 'existing_tokens' should be a comma-separated string of tokens.
    - If the file does not exist, an empty dictionary is returned.
    """
    single_tokens_sets_per_patient = {}
    file_exists = os.path.exists(file_path)
    if file_exists:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                patient, existing_tokens = row
                single_tokens_sets_per_patient[patient] = set(existing_tokens.split(', '))

    return single_tokens_sets_per_patient


def write_results_csv(file_path, single_tokens_sets_per_patient):
    """
    Write results to a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file to be created or overwritten.
    - single_tokens_sets_per_patient (dict): A dictionary where keys are patient identifiers and
                                             values are sets containing unique tokens for each patient.

    Note:
    - The CSV file will have two columns: 'Patient' and 'Tokens Uniques'.
    - 'Tokens Uniques' will be a comma-separated string of unique tokens for each patient.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Patient', 'Tokens Uniques'])
        for patient, single_tokens_set in single_tokens_sets_per_patient.items():
            writer.writerow([patient, ', '.join(single_tokens_set)])


def write_vocabulary_csv(file_path, vocabulary):
    """
    Write a vocabulary to a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file to be created or overwritten.
    - vocabulary (iterable): An iterable containing words to be written to the CSV file.

    Note:
    - Each word in the vocabulary is written as a separate row in the CSV file.
    - The CSV file will contain a single column named 'Word'.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for word in vocabulary:
            writer.writerow([word])
