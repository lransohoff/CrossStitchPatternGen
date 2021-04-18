import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Pattern:
    def __init__(self, img, num_colors):
        self.img = img
        self.num_colors = num_colors
        
    def import_colormap(self):
        clr_df = pd.read_csv(r'C:\Users\laure\Documents\Lauren Folder\Python Scripts\CrossStitchPatternGen\DMCColorMap.csv')
        self.color_map = clr_df
        
    def assign_colors(self):
        n, m, _ = self.img.shape
        dmc_rgb = np.uint8(np.zeros((n, m, 3)))
        dmc_colors = np.zeros((n, m))
        r, c = self.color_map.shape
        for i in range(0, n):
            print(i)
            for j in range(0, m):
                temp_rgb = self.img[i,j]
                min_dist = 255
                ind_best = -1
                for k in range(0, r):
                    cm_temp = [self.color_map.Red[k], self.color_map.Green[k], self.color_map.Blue[k]]
                    if np.sqrt(np.sum((temp_rgb - cm_temp)**2, axis=0)) < min_dist:
                        min_dist = np.sqrt(np.sum((temp_rgb - cm_temp)**2, axis=0))
                        ind_best = k
                dmc_rgb[i, j, :] = [self.color_map.Red[ind_best], 
                        self.color_map.Green[ind_best], 
                        self.color_map.Blue[ind_best]]
                dmc_colors[i,j] = self.color_map.Floss[ind_best]
        return dmc_rgb
    
    def display_img(self, img):
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        axs.imshow(img)
                