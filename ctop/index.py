from docx import Document
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def docx_to_pdf(input_docx, output_pdf):
    # Load the DOCX file
    doc = Document(input_docx)
    
    # Create a PDF canvas
    c = canvas.Canvas(output_pdf, pagesize=LETTER)
    width, height = LETTER
    
    # Starting y position on the page (from bottom)
    y = height - 50
    left_margin = 50
    
    line_height = 14  # spacing between lines
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if text == '':
            # add blank line spacing for empty paragraph
            y -= line_height
        else:
            # If text too long, split it into multiple lines for the page width
            lines = split_text_to_lines(text, c, width - 2*left_margin)
            for line in lines:
                if y < 50:  # Start new page if near bottom
                    c.showPage()
                    y = height - 50
                c.drawString(left_margin, y, line)
                y -= line_height
    
    c.save()
    print(f"Converted '{input_docx}' to '{output_pdf}'")

def split_text_to_lines(text, canvas, max_width):
    """
    Helper to split a long text into lines that fit within max_width.
    """
    words = text.split()
    lines = []
    current_line = ''
    
    for word in words:
        # Test if adding this word exceeds width
        test_line = current_line + (' ' if current_line else '') + word
        if canvas.stringWidth(test_line) <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

if __name__ == "__main__":
    input_docx = "test.docx"   # your input docx path
    output_pdf = "output.pdf"    # output pdf path
    docx_to_pdf(input_docx, output_pdf)
