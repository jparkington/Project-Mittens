"""
James Parkington
3/20/2023

Possible Games (P(d) vs. d)
Visualizes the relationship between the depth (number of half-moves) in a game of chess
and the number of possible unique games using a scatter plot and an exponential fit line.

This script demonstrates how to use linear regression with a logarithmic transformation
to model the exponential growth of possible games in chess as the depth increases.
"""

from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot  as plt
import numpy              as np
import seaborn            as sns

plt.style.use('seaborn-darkgrid')

# Prepare the data
depths      = np.array(list(range(0, 16)) + [80])
positions   = np.array([1, 20, 400, 8902, 197281, 4865609, 119060324, 3195901860, 84998978956, 2439530234167, 69352859712417, 2097651003696806, 62854969236701747, 1981066775000396239, 61885021521585529237, 2015099950053364471960, 3.353e123], dtype = float)
annotations = [((15, 2.015e21), r'$2.015 \cdot 10^{21}$'), ((80, 3.353e123), r'$3.353 \cdot 10^{123}$')]

# Fit the linear regression model and generate predictions for the fit line
model       = lr().fit(depths[:, None], np.log(positions))
colors      = sns.color_palette('pastel')
depth_range = np.linspace(1, 100, 1000)
predictions = np.exp(model.predict(depth_range[:, None]))

# Create the scatter plot
plt.scatter(depths,   
            positions,   
            color      = colors[0], 
            marker     = 'o', 
            edgecolors = 'white', 
            label      = "Perft Value")

# Create the fit line
plt.plot(depth_range, 
         predictions, 
         color     = colors[1], 
         linestyle = ':', 
         linewidth = 2,       
         label     = "Exponential Fit")

# Add annotations as defined above to the plot
for pos, text in annotations:
    plt.annotate(text, pos, (pos[0] + 2, pos[1] * 1.5), fontsize = 8,
                 bbox = dict(boxstyle  = "round,pad = 0.2", 
                             edgecolor = "none", 
                             facecolor = "white", 
                             alpha     = 0.5))

plt.xlabel("Depth $d$",             fontweight='bold')
plt.ylabel("Possible Games $P(d)$", fontweight='bold')

# Customize the plot appearance
ax = plt.gca()
ax.spines[:].set_visible(False)
ax.set(yscale = 'log')
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

# Update the font family for all text elements
font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label]   + \
                ax.get_xticklabels() + ax.get_yticklabels() + \
                plt.legend(loc = 'best', fontsize = 8).get_texts()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

plt.show()

# Make p(80) say Allis estimate with a different circle color (green)