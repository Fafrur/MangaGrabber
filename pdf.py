# import img2pdf
from PIL import Image
import os

def pdf(DEL, chapter_path, i, chapter_number):
    image = []
    pdf_filename = chapter_path + '/pdf_' + str(chapter_number) + '.pdf'
    img1_filename = chapter_path + '/img0.jpg'
    if os.path.exists(img1_filename) == True:
        image1 = Image.open(img1_filename)
        if DEL == 'on': os.remove(img1_filename)
    for j in range(1, i):
        img_filename = chapter_path + '/img' + str(j) + '.jpg'
        if os.path.exists(img_filename) == True:
            image.append(Image.open(img_filename))
            if DEL == 'on': os.remove(img_filename)
    image1.save(pdf_filename, "PDF" ,resolution=100.0, save_all=True, append_images=image)
    
    return