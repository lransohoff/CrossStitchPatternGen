import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt4Agg',warn=False)

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
        n_new = int(n/window)
        m_new = int(m/window)
        img_new = np.uint8(np.zeros((n_new, m_new, 3)))
        for i in range(0, n_new):
            for j in range(0, m_new):
                img_new[i,j] = np.uint8(img[i*window:(i+1)*window,j*window:(j+1)*window].mean(axis=(0,1)))
        return img_new
    
    def display_img(self, img):
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        ext = (0, img.shape[1], img.shape[0], 0)
        axs.imshow(img, extent=ext)
        axs.grid(color='k',linewidth=1)
        
    