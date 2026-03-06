import sys
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    writer = PdfWriter()

    # 1つ目のPDF
    reader1 = PdfReader(pdf1_path)
    for page in reader1.pages:
        writer.add_page(page)

    # 2つ目のPDF
    reader2 = PdfReader(pdf2_path)
    for page in reader2.pages:
        writer.add_page(page)

    # 保存
    with open(output_path, "wb") as f:
        writer.write(f)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_pdf.py input1.pdf input2.pdf output.pdf")
        sys.exit(1)

    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    merge_pdfs(input1, input2, output)
    print(f"Merge finished {output}")
