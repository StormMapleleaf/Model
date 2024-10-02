import fitz  # PyMuPDF

def caj_to_pdf(caj_file, pdf_file):
    # 打开CAJ文件（假设它能被PyMuPDF支持）
    doc = fitz.open(caj_file)
    # 保存为PDF
    doc.save(pdf_file)
    doc.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python caj.py <caj_file>")
        sys.exit(1)

    caj_file = sys.argv[1]
    pdf_file = caj_file.replace('.caj', '.pdf')
    caj_to_pdf(caj_file, pdf_file)
    print(f"Converted {caj_file} to {pdf_file}")
