import os
import openai
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from googletrans import Translator


def summarize_text_gguf(raw_text):
    # Initialisez le tokenizer LLM avec votre propre chemin vers les fichiers de vocabulaire quantifiés (gguf) et la configuration du modèle.
    tokenizer = AutoTokenizer.from_pretrained("bigscience/moss-mixtral", use_fast=False, trust_remote_code=True)
    
    # Initialisez le pipeline LLM avec votre propre chemin vers les fichiers de poids quantifiés (gguf).
    summarization_pipeline = pipeline("summarization", model="bigscience/moss-mixtral", tokenizer=tokenizer)
    
    # Remplacez row_text par votre propre variable contenant le texte à résumer.
    summary = summarization_pipeline(row_text)["summary_text"]

    return summary
    
def summarize_text(raw_text):
    model_id = "mistralai/Mixtral-8x7B-v0.1"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)

    text = 'Résume ce texte: "' + raw_text + '"'
    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(**inputs, max_length=2048)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

def summarize_text_with_gpt3(raw_text):
    openai.api_key = 'YOUR_API_KEY'  # Remplacez 'YOUR_API_KEY' par votre clé API GPT-3

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Résume le texte suivant : '{raw_text}'",
      max_tokens=100
    )

    summary = response.choices[0].text.strip()
    return summary


def clean_and_translate(raw_text, nlp):
    """
    Summarize a given raw text using extractive summarization.

    Parameters:
    - raw_text (str): The raw text to be summarized.
    - nlp: A spaCy language model for text processing.
    - ratio (float): The ratio of sentences to include in the summary (default is 0.2).

    Returns:
    - str: The summarized text.

    Note:
    - The function uses extractive summarization, selecting the most important sentences
      based on the calculated scores of words in the text.
    - Stop words and words with less than 3 characters are excluded from the analysis.
    """
    # Tokenize and clean text with spaCy, exclude line breaks and tabs
    doc = nlp(raw_text)
    cleaned_tokens = {token.text.lower() for token in doc if not token.is_space and token.text not in {'\n', '\t'}}

    # Translate tokens into English with Google Translate
    translator = Translator()
    translated_text = translator.translate(" ".join(cleaned_tokens), src='fr', dest='en').text

    # Return the list of tokens translated into English
    return translated_text.split()


def token_extraction(patient_path, nlp):
    """
    Extract unique tokens from text files within a patient's directory.

    Parameters:
    - patient_path (str): The path to the directory containing text files for a patient.
    - nlp: A spaCy language model for text processing.

    Returns:
    - set: A set containing unique tokens extracted from the patient's text files.

    Note:
    - The function iterates through text files in the patient's directory, summarizes the content,
      and extracts unique tokens after cleaning and translation.
    - Only text files with a '.txt' extension are considered.
    - In case of an error reading a file, an error message is printed, and processing continues.
    """
    patient_unique_tokens_set = set()

    for file in os.listdir(patient_path):
        filepath = os.path.join(patient_path, file)
        print(f"------> Processing {filepath}")

        # Check if the file is a text file
        if os.path.isfile(filepath) and filepath.lower().endswith('.txt'):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"----------> File Content Readed")

            except Exception as e:
                print(f"<----- Error reading file '{filepath}': {e}")

            # Text summary
            summary = summarize_text_with_gguf(content)
            print(f"----------> Summary: {summary}")

            # Cleaning and translation
            translated_text = clean_and_translate(summary, nlp)
            print(f"----------> Translated Tokens")

            patient_unique_tokens_set.update(translated_text)

    return patient_unique_tokens_set
