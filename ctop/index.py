import pypandoc

def convert_docx_to_pdf(input_docx, output_pdf):
    try:
        # Convert DOCX to PDF using Pandoc
        output = pypandoc.convert_file(input_docx, 'pdf', outputfile=output_pdf)
        assert output == ""  # If output isn't empty, something went wrong.
        print(f"Successfully converted {input_docx} to {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
input_docx = "test.docx"  # Path to your DOCX file
output_pdf = "output_document.pdf"  # Path to save the PDF

convert_docx_to_pdf(input_docx, output_pdf)
