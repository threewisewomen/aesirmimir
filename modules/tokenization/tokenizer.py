import nltk
from nltk.tokenize import word_tokenize

nltk.data.load('tokenizers/punkt/english.pickle')

def tokenize_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            text = file.read()
        tokens = word_tokenize(text)
        return tokens
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except UnicodeDecodeError:
        print(f"Unable to decode file: {file_path}")
    except Exception as e:
        print(f"Error occurred while tokenizing file: {file_path}")
        print(str(e))
    return []