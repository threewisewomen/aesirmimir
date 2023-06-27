from services.pdf_service import PdfService

def main():
    # Example usage of the tokenization module
    directory = 'C:/Users/john/OneDrive/Documents/FORBIDDEN KNOWLEDGE'

    # Create an instance of PdfService
    pdf_service = PdfService(directory)

    # Process the PDFs using PdfService
    pdf_service.process_pdfs()

    # Example usage of the training module
    # data = pdf_service.get_tokens()  # Assuming you have a method to retrieve the tokens
    # model = train(data)
    # Use the trained model for further processing

if __name__ == "__main__":
    main()
