"""
James Parkington
3/20/2023

Branching Factors (b(d) vs. d)
Visualizes the relationship between the depth (number of half-moves) in a game of chess
and the branching factor using a scatter plot and a custom curve fit line.

The script captures the diminishing returns of exploring deeper into the game tree due to 
the increasing number of possible moves, resulting in a logarithmic relationship between 
depth and branching factor.
"""

from scipy.optimize import curve_fit
import matplotlib.pyplot  as plt
import numpy              as np
import seaborn            as sns

plt.style.use('seaborn-darkgrid')
plt.figure(figsize = (8, 4))

# Prepare the data
colors    = sns.color_palette('pastel')
depths    = np.array(list(range(1, 16)) + [80])
branching = np.array([20, 20, 22.255, 22.161, 24.663, 24.470, 26.843, 26.596, 28.701, 28.429, 30.246, 29.964, 31.518, 31.238, 32.562, 42.5], dtype = float)

# Define a custom logarithmic function
def custom_logarithmic(x, a, b, c, d):
    return a * np.log(x - c) ** b + d

# Fit the custom curve
depth_range = np.linspace(1, 100, 1000)
predictions = custom_logarithmic(depth_range, *curve_fit(custom_logarithmic, 
                                                         depths, 
                                                         branching,
                                                         maxfev = 100000,
                                                         p0 = (20, 1, 0, 0))[0])

# Create the scatter plot
plt.scatter(depths[:-1],    # Ignore the data pad at the end of the series
            branching[:-1], # Ignore the data pad at the end of the series
            color      = colors[0],
            marker     = 'o',
            edgecolors = 'white',
            label      = "Branching Factor")

# Isolate the point for the "Allis Estimate"
plt.scatter(np.array([80]),
            np.array([35]),
            color      = colors[2],  # Choose any color you prefer
            marker     = 'o',
            edgecolors = 'white',
            label      = "Allis Estimate")

# Create the fit line
plt.plot(depth_range,
         predictions,
         color     = colors[4],
         linestyle = ':',
         linewidth = 2,
         label     = "Logarithmic Fit")

plt.xlabel("Depth $d$",               fontweight = 'bold')
plt.ylabel("Branching Factor $b(d)$", fontweight = 'bold')

# Customize the plot appearance
ax = plt.gca()
ax.spines[:].set_visible(False)
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

# Update the font family for all text elements
font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label] + \
                ax.get_xticklabels() + ax.get_yticklabels() + \
                plt.legend(loc = 'best', fontsize = 8).get_texts()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

# Crop the final output to remove whitespace
plt.subplots_adjust(left = 0.08, right = 0.98, top = 0.9, bottom = 0.1)

plt.show()