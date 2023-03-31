"""
James Parkington
3/28/2023

Common Games: Estimated Branching Factors
Visualizes the estimated branching factors for various games using a bar chart.
"""

import matplotlib.pyplot as plt
import numpy             as np
import seaborn           as sns

plt.style.use('seaborn-darkgrid')
plt.figure(figsize = (10, 6))

# Prepare the data
games             = ["Chess", "Tic-tac-toe", "Connect Four", "Checkers", "Scrabble"]
branching_factors = [3.353e123, 19683, 5.5e24, 8.9e37, 5.82e75]
colors            = sns.color_palette('pastel')

# Create the bar chart
bars = plt.bar(games, branching_factors, color = colors[:5], edgecolor = 'white')

plt.xlabel("Games", fontweight = 'bold')
plt.ylabel("Estimated Branching Factors", fontweight = 'bold')

# Customize the plot appearance
ax = plt.gca()
ax.spines[:].set_visible(False)
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)
ax.set_yscale("log")

# Add annotations to the top of each bar
for bar, bf in zip(bars, branching_factors):
    height   = bar.get_height()
    exponent = int(np.floor(np.log10(bf)))
    base     = bf / (10 ** exponent)
    ax.annotate(f'${base:.2f} × 10^{{{exponent}}}$',
                xy         = (bar.get_x() + bar.get_width() / 2, height),
                xytext     = (0, 3),
                textcoords = "offset points",
                ha         = 'center', 
                va         = 'bottom',
                fontsize   = 8,
                fontweight = 'bold',
                fontfamily = 'DejaVu Sans Mono')

# Update the font family for all text elements
font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label] + \
               ax.get_xticklabels() + ax.get_yticklabels()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

# Crop the final output to remove whitespace
plt.subplots_adjust(left = 0.06, right = 0.98, top = 0.94, bottom = 0.06)

plt.show()