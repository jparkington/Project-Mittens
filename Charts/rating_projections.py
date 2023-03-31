"""
James Parkington
3/28/2023

Actual vs. Projected Rating
Visualizes Player A's actual rating change in the first 30 games on a new chess account,
and projects their rating after playing 50, 75, 100, 150, 200, 250, and 500 games using a scatter plot.
"""

import matplotlib.pyplot as plt
import seaborn           as sns

plt.style.use('seaborn-darkgrid')
plt.figure(figsize = (10, 3))

colors        = sns.color_palette('pastel')
game_numbers  = list(range(1, 31))
win_loss      = [2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 2, 2, 3]
ratings       = [945, 1057, 1145, 1198, 1267, 1217, 1263, 1300, 1335, 1309, 1332, 1358, 1388, 1358, 1379, 1397, 1421, 1439, 1455, 1480, 1495, 1478, 1490, 1509, 1494, 1509, 1501, 1511, 1528, 1514]

milestones          = [50, 75, 100, 150, 200, 250, 500]
milestone_ratings   = [1575, 1622, 1660, 1730, 1810, 1910, 2050]

# Plot ratings
plt.scatter(game_numbers, 
            ratings, 
            color      = colors[0], 
            marker     = 'o', 
            edgecolors = 'white', 
            label      = 'Actual Rating')

plt.scatter(milestones, 
            milestone_ratings, 
            color      = colors[4], 
            marker     = 'o', 
            edgecolors = 'white', 
            label      = 'Projected Rating')

# Add annotations for Projected Ratings
for idx, (ms, rt) in enumerate(zip(milestones, milestone_ratings)):
    plt.annotate("{:.0f}".format(rt),
                 (ms, rt),
                 xytext   = (ms, rt - 100),
                 ha       = "center",
                 fontsize = 8,
                 bbox     = dict(boxstyle  = "round,pad=0.2",
                                 edgecolor = "none",
                                 facecolor = colors[4],
                                 alpha     = 0.5))

plt.xlabel("Game Number",  fontweight = 'bold')
plt.ylabel("Rating",       fontweight = 'bold')

plt.legend(loc = 'best', fontsize = 8)

ax = plt.gca()
ax.spines[:].set_visible(False)
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label] + \
                ax.get_xticklabels() + ax.get_yticklabels() + \
                plt.legend(loc = 'best', fontsize = 8).get_texts()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

# Crop the final output to remove whitespace
plt.subplots_adjust(left = 0.06, right = 0.98, top = 0.9, bottom = 0.12)

plt.show()