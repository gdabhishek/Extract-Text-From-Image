import pytesseract

#Python Imaging Library 
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Load Image
img=Image.open('img.jpg')
#Extract text from image
text = pytesseract.image_to_string(img)
#Print extracted text
print(text)




