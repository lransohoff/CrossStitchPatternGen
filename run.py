# Header
# 4/3/21

from Image.image import Image
from Pattern.pattern import Pattern

def run():
    in_path = r'C:\Users\laure\Documents\Lauren Folder\Python Scripts\CrossStitchPatternGen\IMG_9169.JPG'
    n_windows = 40
    i = Image(import_path = in_path,
              num_windows = n_windows)
    img = i.import_image()
    img_new = i.pixelate(img)
    i.display_img(img)
    i.display_img(img_new)
    
    n_colors = 7
    p = Pattern(img = img_new,
                num_colors = n_colors)
    
    
if __name__ == '__main__':
    run()