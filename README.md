# pdfmerge
In the SGMJ annual meeting, the organizers need to merge multiple PDF files. The programs in this repository can be used for this purpose.

## merge_pdfs.py
`Usage: python merge_pdfs.py <input_directory> <output_pdf>`

merge_pdfs.pyは、指定したディレクトリ中にある全てのPDFファイルを、ファイル名順にmergeするPythonプログラムです。mergeする際に、ファイル名をPDFの左上に青字で挿入します。
A4 1枚のポスターや口頭発表要旨にポスター番号や口頭発表の番号を振りつつmergeしたい場合に、有用です。プログラム実行前に各PDFのファイル名を、ポスター番号や口頭発表番号にしておく必要があります。

## merge_pdf.py
`Usage: python merge_pdf.py <input1.pdf> <input2.pdf> <output.pdf>`

merge_pdf.pyは、2つのPDFファイルをmergeするPythonプログラムです。シンプルに2つのPDFを統合したい時に有用です。
