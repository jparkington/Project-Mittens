"""
James Parkington
3/22/2023

Growth Rates (g(d) vs. d)
Visualizes the relationship between the depth (d) and the g(d) values using a scatter plot
and a logarithmic fit line.

This script demonstrates how to use curve fitting with a custom factorial function
to model the relationship between growth rates and depth (d) of moves in chess.
"""

from scipy.optimize import curve_fit
import matplotlib.pyplot  as plt
import numpy              as np
import seaborn            as sns

plt.style.use('seaborn-darkgrid')
plt.figure(figsize = (8, 4))

# Prepare the data
colors      = sns.color_palette('pastel')
depths      = np.array(list(range(2, 16)) + [80])
g_values    = np.array([4.322, 2.824, 2.235, 1.992, 1.785, 1.691, 1.578, 1.528, 1.454, 1.422, 1.368, 1.345, 1.304, 1.286, 0.811])

# Define a custom logarithmic function
def custom_log(x, a, b, c, d):
    return a * (x ** b) / (x ** c + d)

# Fit the custom curve
depth_range = np.linspace(2, 100, 1000)
predictions = custom_log(depth_range, *curve_fit(custom_log, 
                                                 depths, 
                                                 g_values, 
                                                 maxfev = 100000, 
                                                 p0 = (1, -1, 1, 0))[0])

# Create the scatter plot
plt.scatter(depths,   
            g_values,   
            color      = colors[0], 
            marker     = 'o', 
            edgecolors = 'white', 
            label      = "Growth Rate")

# Isolate the point for the "Allis Estimate"
plt.scatter(np.array([80]),
            np.array([0.811]),
            color      = colors[2],
            marker     = 'o',
            edgecolors = 'white',
            label      = "Allis Estimate")

# Create the fit line
plt.plot(depth_range, 
         predictions, 
         color     = colors[3], 
         linestyle = ':', 
         linewidth = 2,       
         label     = "Logarithmic Fit")

plt.xlabel("Depth $d$",            fontweight='bold')
plt.ylabel("Growth Rates $g(d)$",  fontweight='bold')

# Customize the plot appearance
ax = plt.gca()
ax.spines[:].set_visible(False)
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

# Update the font family for all text elements
font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label]   + \
                ax.get_xticklabels() + ax.get_yticklabels() + \
                plt.legend(loc = 'best', fontsize = 8).get_texts()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

# Crop the final output to remove whitespace
plt.subplots_adjust(left = 0.08, right = 0.98, top = 0.9, bottom = 0.1)

plt.show()