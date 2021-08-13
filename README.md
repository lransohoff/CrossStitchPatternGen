# CrossStitchPatternGen
Generates cross stitch pattern from an image

8/13
Added capability to pick number of colors in the pattern.
This uses k-means clustering to group all the colors into k groups. Then I find the centroid of each group and make that the new color. Then reassign the colors in the image with the k colors and re-run assign_colors to map them to dmc thread colors. Works pretty well!
