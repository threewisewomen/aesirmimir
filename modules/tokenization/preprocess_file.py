import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.data.load('tokenizers/punkt/english.pickle')

def tokenize_file(text, file_path, encoding='utf-8'):
    try:
        tokens = word_tokenize(text)
        
        # Cleaning steps
        cleaned_tokens = remove_punctuation(tokens)
        cleaned_tokens = convert_to_lowercase(cleaned_tokens)
        cleaned_tokens = remove_special_characters(cleaned_tokens)
        cleaned_tokens = remove_stopwords(cleaned_tokens)
        cleaned_tokens = apply_stemming(cleaned_tokens)
        
        # Extract the file name from the input file path
        file_name = os.path.basename(file_path)
        
        # Generate the output file path using the input file name
        output_file_path = f"{os.path.splitext(file_name)[0]}_preprocessed.txt"
        
        with open(output_file_path, 'w', encoding=encoding) as output_file:
            for token in cleaned_tokens:
                output_file.write(token + '\n')
        
        print(f"Preprocessed tokens written to file: {output_file_path}")
        return cleaned_tokens
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except UnicodeDecodeError:
        print(f"Unable to decode file: {file_path}")
    except Exception as e:
        print(f"Error occurred while tokenizing file: {file_path}")
        print(str(e))
    return []
def remove_punctuation(tokens):
    # Remove punctuation from tokens
    cleaned_tokens = [token for token in tokens if token.isalpha()]
    return cleaned_tokens

def convert_to_lowercase(tokens):
    # Convert tokens to lowercase
    cleaned_tokens = [token.lower() for token in tokens]
    return cleaned_tokens

def remove_special_characters(tokens):
    # Remove special characters from tokens
    cleaned_tokens = [token for token in tokens if token.isalnum()]
    return cleaned_tokens

def remove_stopwords(tokens):
    # Remove stopwords from tokens
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [token for token in tokens if token not in stop_words]
    return cleaned_tokens

def apply_stemming(tokens):
    # Apply stemming to tokens
    stemmer = PorterStemmer()
    cleaned_tokens = [stemmer.stem(token) for token in tokens]
    return cleaned_tokens
