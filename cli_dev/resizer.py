from pypdf import PdfReader as pdfr
from pypdf import PdfWriter as pdwr

def resize_without_loss(file):
    writer=pdwr()
    reader=pdfr(file)
    for page in reader.pages:
        writer.add_page(page)
    for page in writer.pages:
        page.compress_content_streams()
    return writer
def resize_with_loss_of_qimage(file):
    reader = pdfr(file)
    writer = pdwr()
    for pages in reader.pages:
        writer.add_page(pages)
    for pages in writer.pages:
        for img in pages.images:
            img.__reduce__
    return writer

