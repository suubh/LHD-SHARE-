try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr(filename):
    
    text = pytesseract.image_to_string(Image.open(filename))  
    return text

print(ocr('images/Share.png'))