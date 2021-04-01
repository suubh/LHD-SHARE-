try:
    from PIL import Image
except ImportError:
    import Image 

import pytesseract as pyt

def ocr_try(filename):
    text=pyt.image_to_string(Image.open(filename))
    return text

#print(ocr_try('firstpage.jpg'))
