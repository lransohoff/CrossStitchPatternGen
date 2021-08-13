import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.spatial import distance
from sklearn.cluster import KMeans

class Pattern:
    def __init__(self, img, num_colors):
        self.img = img
        self.num_colors = num_colors
        
    def import_colormap(self):
        clr_df = pd.read_csv(r'C:\Users\laure\Documents\Lauren Folder\Python Scripts\CrossStitchPatternGen\DMCColorMap.csv')
        self.color_map = clr_df
        
    def assign_colors(self, img):
        n, m, _ = img.shape
        dmc_rgb = np.uint8(np.zeros((n, m, 3)))
        dmc_colors = []
        r, c = self.color_map.shape
        rbg_cm_array = self.color_map[['Red','Green','Blue']].to_numpy()
        for i in range(0, n):
            for j in range(0, m):
                temp_rgb = img[i,j]
                d_cell = distance.cdist([temp_rgb],rbg_cm_array,'euclidean')
                ind_best = np.argmin(d_cell)
                dmc_rgb[i, j, :] = [self.color_map.Red[ind_best], 
                        self.color_map.Green[ind_best], 
                        self.color_map.Blue[ind_best]]
                dmc_colors.append(self.color_map.Floss[ind_best])
#        print(dmc_colors)
        return dmc_rgb
    
    def reduce_colors(self, img):
        # Get starting shape of image
        n, m, q = self.img.shape
        # Reshape dmc colors image map to an x by 3 (q=3) 2d array
        dmc_colors_array = img.reshape(-1,q)
        # Use numpy unique to find list of unique colors (each color is a 1x3 
        #  row of the dmc_colors_array, so do axis=0 to get unique rows instead of single values)
        [unique_dmc_colors, inv] = np.unique(dmc_colors_array, return_inverse=True ,axis=0)
        # Now we need to reduce the number of unique colors
        # How to do this....
        # Try using k means clustering! Fun!
        # Thanks Jeremy -https://www.jeremyjordan.me/grouping-data-points-with-k-means-clustering/
        k = self.num_colors
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(unique_dmc_colors)
        kmeans.labels_
        # Now we have our k groups - time to find k colors
        # Take centroid of each group and then find closest dmc color to the centroid?
        # Let's try it!
        color_assignment = dict()
        color_assignment["first_dmc_color"] = unique_dmc_colors
        color_assignment["kmeans_group"] = kmeans.labels_
        color_assignment["new_rgb_color"] = kmeans.cluster_centers_[kmeans.labels_]
        
        new_rgb_flat = color_assignment["new_rgb_color"][inv]
        
        new_rgb_img = new_rgb_flat.reshape(n, m, q)
        
        new_dmc = self.assign_colors(new_rgb_img)
        return new_dmc
        
    def display_img(self, img):
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        axs.imshow(img)
                