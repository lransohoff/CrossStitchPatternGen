import numpy as np
import matplotlib.pyplot as plt

class Image:
    def __init__(self, import_path, num_windows):
        self.path_in = import_path
        self.num_win = num_windows
        
    def import_image(self):
        img = plt.imread(self.path_in)
        return img
    
    def pixelate(self, img):
        n, m, _ = img.shape
        window = int(np.floor(n/self.num_win))
        n = n - n % window
        m = m - m % window
        img_new = np.uint8(np.zeros((n, m, 3)))
        for i in range(0, n, window):
            for j in range(0, m, window):
                img_new[i:i+window,j:j+window] = np.uint8(img[i:i+window,j:j+window].mean(axis=(0,1)))
        return img_new
    
    def display_img(self, img):
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        axs.imshow(img)
        
    