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
