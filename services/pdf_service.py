import os
import glob
from pdfminer.high_level import extract_text
from modules.tokenization.preprocess_file import tokenize_file
from repo.bookcheck import BookRepository

class PdfService:
    def __init__(self, directory):
        self.directory = directory
        self.book_repository = BookRepository()

    def process_pdfs(self):
        pdf_files = glob.glob(os.path.join(self.directory, '*.pdf'))

        for file_path in pdf_files:
            if self.book_repository.check_book_exists(file_path):
                print(f"Book already processed: {file_path}")
                continue

            text = self.read_pdf(file_path)
            if text:
                file_tokens = self.tokenize_pdf(text, file_path)
                # print(f"File: {file_path}, Token Count: {len(file_tokens)}")
                self.book_repository.add_book(file_path)

    def read_pdf(self, file_path):
        try:
            text = extract_text(file_path)
            return text
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return ""

    def tokenize_pdf(self, text, file_path):
        return tokenize_file(text, file_path)
