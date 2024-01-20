# 🧠 Preparation of the Hackathon

**Python: 3.11.4**

- git clone https://github.com/Smartappli/hackathon.git
- cd hackathon
- python -m pip install --upgrade pip
- pip install -r requirements.txt
- python -m spacy download fr_core_news_sm
- python main.py

# ⚙️ Data organization:

⚡️ **Input:**
```bash
[Program Root]
|--- vocabulary.csv (optional)
|--- [parents]
         |--- [patient_1]
                   |--- text_file_1.txt
                   |--- text_file_2.txt
                   |--- ...
              [patient_2]
                   |--- ...
                   .
                   .
                   .
```

💾 **Output:**
```bash
[Program Root]
|--- vocabulary.csv
|--- results.csv
|--- matrix.csv
|--- hits.csv
```

# ⚠️ Note: 

- Directory patients contains other directories (one by patient)
- vocabulary.csv contains global token dictionnary
- results.csv contains unique tokens by patients (one line by patient)
- matrix.csv contains the matching between pabients and vocabulary
- hits.csv contains vocabulary order by desc hits 

