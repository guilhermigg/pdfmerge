# title = PDFMerger
# by = ['guilhermigg']
# int year = 2020

import PyPDF2
import os
from glob import glob  

# Merge PDF's
def merge(pdfs):
    for x in pdfs:
        pdf1File = open(x[0], 'rb')
        pdf2File = open(x[1], 'rb')

        pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
        pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

        pdfWriter = PyPDF2.PdfFileWriter()
        
        for pageNum in range(pdf1Reader.numPages):
            pageObj = pdf1Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
        for pageNum in range(pdf2Reader.numPages):
            pageObj = pdf2Reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        
        pdfOutputFile = open(x[0]+'.pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
        
        pdfOutputFile.close()

        pdf1File.close()
        pdf2File.close()

# Sort files
def filterList(files, sortType):
    counter = 0
    matches = []

    for n in range(len(files)):
        print(n)
        match = []

        for file in files:
            if(n+'.pdf' in file):
                match.append()

    print(matches)
    return 0

# Search for PDF files into the directory
def scanDir(pdfDir):
    files = os.listdir(pdfDir)
    pdFiles = []

    for f in files:
        if(f.endswith('.pdf')):
            pdFiles.append(f)
    
    return pdFiles

# Main Factory
def main():
    pdfDir = input('Where\'s located all the files? -> ')
    sortType = int(input('SORT TYPE\n(1) A-1\n (2) A-B\n  (3) 1-2\n -> '))

    pdfList = scanDir(pdfDir)
    filteredPdfList = filterList(pdfDir, sort)

main()