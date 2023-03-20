"""
James Parkington
3/20/2023

Branching Factors (b(d) vs. d)
Visualizes the relationship between the depth (number of half-moves) in a game of chess
and the branching factor using a scatter plot and an exponential fit line.

This script demonstrates how to use linear regression with a logarithmic transformation
to model the exponential growth of the branching factor in chess as the depth increases.
"""

from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot  as plt
import numpy              as np
import seaborn            as sns

plt.style.use('seaborn-darkgrid')

# Prepare the data
depths    = np.array(list(range(1, 16)) + [80])
branching = np.array([20, 20, 22.255, 22.161, 24.663, 24.470, 26.843, 26.596, 28.701, 28.429, 30.246, 29.964, 31.518, 31.238, 32.562, 35], dtype = float)

# Fit the linear regression model and generate predictions for the fit line
model       = lr().fit(depths[:, None], np.log(branching))
colors      = sns.color_palette('pastel')
depth_range = np.linspace(1, 100, 1000)
predictions = np.exp(model.predict(depth_range[:, None]))

# Create the scatter plot
plt.scatter(depths,
            branching,
            color      = colors[0],
            marker     = 'o',
            edgecolors = 'white',
            label      = "Branching Factor")

# Create the fit line
plt.plot(depth_range,
         predictions,
         color     = colors[2],
         linestyle = ':',
         linewidth = 2,
         label     = "Exponential Fit")

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

plt.show()
