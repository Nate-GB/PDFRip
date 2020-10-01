from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os

#Path of the PDF
PDF_file = "Walker Irene Cancel.pdf"

# Store all the pages of teh PDF in a variable
pages = convert_from_path(PDF_file, 500)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:

    """

      Declaring filename for each page of PDF as JPG
      For each page, filename will be:
      PDF page 1 -> page_1.jpg
      PDF page 2 -> page_2.jpg
      ...
      PDF page n -> page_n.jpg

    """
    filename = "page_"+str(image_counter) +".jpg"

    #Save the image of the page in system
    page.save(filename, 'JPEG')

    # Increment the counter to update filename
    image_counter += 1

# Variable to get count of total number of pages
filelimit = image_counter-1

# Creating a text file to write the output
outfile = "out_text.txt"

# Open the file in append mode to that
# All contents of all images are added to the same file
f = open(outfile, "a")

# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
   # Set filename to recognize text from pdf
   
    filename = "page_"+str(i)+".jpg" 

    # Recognize the text as string in image using pytesseract
    text = str(((pytesseract.image_to_string(Image.open(filename)))))

    # The recognized text is stored in variable text
    # Replaces hyphenated words to make them one word
    text = text.replace('-\n', '')

    # Write the processed text to the file
    f.write(text)

    # Close the file after writing the text
f.close()