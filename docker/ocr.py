from PIL import Image
import pytesseract

def ocr(path):
    img = Image.open(path).convert('L')

    table = []
    threshold= 150
    for i in range(256):
        table.append(1 if i > threshold else 0)

    img_bin = img.point(table, '1')

    text = pytesseract.image_to_string(img_bin, config='-c tessedit_char_whitelist=0123456789').strip()

    #print (text)

    return text