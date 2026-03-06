import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue
from io import BytesIO

def create_overlay(text, page_width, page_height):
    """
    左上に青字フォントサイズ20でテキストを書いた
    PDFオーバーレイをメモリ上に作成する
    """
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))

    c.setFillColor(blue)
    c.setFont("Helvetica", 20)

    # 左上マージン（少し余白を取る）
    margin_x = 40
    margin_y = 40

    c.drawString(margin_x, page_height - margin_y, text)
    c.save()

    packet.seek(0)
    return PdfReader(packet)

def merge_pdfs_with_filename(input_dir, output_pdf):
    input_path = Path(input_dir)
    pdf_files = sorted(input_path.glob("*.pdf"))

    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(str(pdf_file))
        page = reader.pages[0]  # 1ページPDF想定

        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)

        # オーバーレイ作成（ファイル名のみ）
        overlay_pdf = create_overlay(pdf_file.stem, page_width, page_height)
        overlay_page = overlay_pdf.pages[0]

        # 元ページに重ねる
        page.merge_page(overlay_page)

        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_pdfs.py <input_directory> <output_pdf>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]

    merge_pdfs_with_filename(input_directory, output_file)

    print("Merge finished", output_file)
