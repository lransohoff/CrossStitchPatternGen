# Header
# 4/3/21

from Image.image import Image
from Pattern.pattern import Pattern

def run():
    in_path = r'C:\Users\laure\Documents\Lauren Folder\Python Scripts\CrossStitchPatternGen\rect3539_2.jpg'
    n_windows = 50
    i = Image(import_path = in_path,
              num_windows = n_windows)
    img = i.import_image()
    img_new = i.pixelate(img)
    i.display_img(img)
    i.display_img(img_new)
    
    n_colors = 20
    p = Pattern(img = img_new,
                num_colors = n_colors)
    p.import_colormap()
    dmc_rgb = p.assign_colors(img_new)
    p.display_pattern_img(dmc_rgb)
    dmc_new = p.reduce_colors(dmc_rgb)
    p.display_pattern_img(dmc_new)
    
if __name__ == '__main__':
    run()