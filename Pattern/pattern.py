import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance

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
        dmc_colors = []
        r, c = self.color_map.shape
        rbg_cm_array = self.color_map[['Red','Green','Blue']].to_numpy()
        for i in range(0, n):
            for j in range(0, m):
                temp_rgb = self.img[i,j]
                d_cell = distance.cdist([temp_rgb],rbg_cm_array,'euclidean')
                ind_best = np.argmin(d_cell)
#                min_dist = 255
#                ind_best = -1
#                for k in range(0, r):
#                    cm_temp = [self.color_map.Red[k], self.color_map.Green[k], self.color_map.Blue[k]]
#                    if np.sqrt(np.sum((temp_rgb - cm_temp)**2, axis=0)) < min_dist:
#                        min_dist = np.sqrt(np.sum((temp_rgb - cm_temp)**2, axis=0))
#                        ind_best = k
                dmc_rgb[i, j, :] = [self.color_map.Red[ind_best], 
                        self.color_map.Green[ind_best], 
                        self.color_map.Blue[ind_best]]
                dmc_colors.append(self.color_map.Floss[ind_best])
#        print(dmc_colors)
        return dmc_rgb
    
    def display_img(self, img):
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        axs.imshow(img)
                