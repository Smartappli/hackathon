import os


def number_of_patients_and_files(root_directory):

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
                ([f for f in os.listdir(patient_directory_path) if os.path.isfile(os.path.join(patient_directory_path, f))])

    return total_directories, total_files
