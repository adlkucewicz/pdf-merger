#PDF Manipulation Program

import PyPDF2
import sys

def help_file():
    print("""
    This is a PDF manipulation program. There are 2 functions available:
        -PDF merge, 
        -PDF page rotate.

    For PDF merger use the following syntax:
        
        pdf_merger.py merge [PDF1 FILE NAME] [PDF2 FILE NAME]

    For PDF page rotation use the following syntax:

        pdf_merger C [PDF FILE NAME] [PAGE NUMBER FOR ROTATION] [ANGLE OF ROTATION]
        pdf_merger AC [PDF FILE NAME] [PAGE NUMBER FOR ROTATION] [ANGLE OF ROTATION]
        
        """)

def merge():
    """
    Function to merge
    """
    try:
        pdf_list = sys.argv[2:]
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write('merged.pdf')
        
        print(f"Success: merged.pdf created.")
    except AssertionError as error:
        print("Failed: Check you have provided valid arguments.")
        print(error)

def rotate_anticlockwise():
    """
    Function to rotate page anticlockwise
    """
    try:
        with open(sys.argv[2], 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            writer = PyPDF2.PdfFileWriter()
            num_pages = reader.getNumPages()

            for num in range(0,num_pages):
                page = reader.getPage(num)
                if num == int(sys.argv[3]) - 1:
                    page.rotateCounterClockwise(int(sys.argv[4]))
                writer.addPage(page)
            new_filename = "rotated_" + sys.argv[2]
            with open(new_filename, 'wb') as new_file:
                writer.write(new_file)
        
        print(f"Success: {new_filename} created.")
    except AssertionError as error:
        print("Failed: Check you have provided valid arguments.")
        print(error)

    


def rotate_clockwise():
    """
    Function to rotate page clockwise
    """
    try:
        with open(sys.argv[2], 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            writer = PyPDF2.PdfFileWriter()
            num_pages = reader.getNumPages()

            for num in range(0,num_pages):
                page = reader.getPage(num)
                if num == int(sys.argv[3]) - 1:
                    page.rotateClockwise(int(sys.argv[4]))
                writer.addPage(page)
            new_filename = "rotated_" + sys.argv[2]
            with open(new_filename, 'wb') as new_file:
                writer.write(new_file)
            
        print(f"Success: {new_filename} created.")
    except AssertionError as error:
        print("Failed: Check you have provided valid arguments.")
        print(error)

if __name__ == "__main__":

    if len(sys.argv) < 2 or sys.argv[1].upper() == 'HELP':
        help_file()
    elif sys.argv[1].upper() == 'MERGE':
        merge()
    elif sys.argv[1].upper() == 'AC':
        rotate_anticlockwise()
    elif sys.argv[1].upper() == 'C':
        rotate_clockwise()
    else:
        print("Not a valid function name. See the help file below.\n\n")
        help_file()