"""
James Parkington
3/28/2023

Delta Rating vs. Game Number
Visualizes Player A's rating change, win/loss status, and opponent rating
in the first 30 games on a new chess account using a scatter plot.
"""

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn           as sns
import numpy             as np

plt.style.use('seaborn-darkgrid')
plt.figure(figsize = (10, 6))

colors        = sns.color_palette('pastel')
game_numbers  = list(range(1, 31))
delta_ratings = [0, 112, 88, 53, 69, -50, 46, 37, 35, -26, 23, 26, 30, -30, 21, 18, 24, 18, 16, 25, 15, -17, 12, 19, -15, 15, -8, 10, 17, -14]
win_loss      = [2, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3, 2, 3, 2, 2, 3]
ratings       = [945, 1057, 1145, 1198, 1267, 1217, 1263, 1300, 1335, 1309, 1332, 1358, 1388, 1358, 1379, 1397, 1421, 1439, 1455, 1480, 1495, 1478, 1490, 1509, 1494, 1509, 1501, 1511, 1528, 1514]

def custom_log(x, a, b, c, d):
    return a * np.log(x - c) ** b + d

# Fit the custom curve
game_range  = np.linspace(1, 30, 1000)
predictions = custom_log(game_range, *curve_fit(custom_log, 
                                                game_numbers, 
                                                delta_ratings,
                                                maxfev = 100000,
                                                p0     = (20, 1, 0, 0))[0])

# Create the fit line
plt.plot(game_range,
         predictions,
         color     = colors[5],
         linestyle = ':',
         linewidth = 2)

for idx, (gn, dr, wl, rt) in enumerate(zip(game_numbers, delta_ratings, win_loss, ratings)):
    plt.scatter(gn,
                dr,
                color      = colors[wl],
                marker     = 'o',
                edgecolors = 'white')
    
    if idx % 5 == 0:
        plt.annotate(rt,
                     (gn, dr),
                     (gn - 0.5, dr + 2),
                     fontsize = 8,
                     bbox = dict(boxstyle  = "round,pad=0.2",
                                 edgecolor = "none",
                                 facecolor = colors[wl],
                                 alpha     = 0.5))

plt.xlabel("Game Number",  fontweight = 'bold')
plt.ylabel("Delta Rating", fontweight = 'bold')

# Create the legend
win_marker  = plt.scatter([], [], color = colors[2], marker    = 'o', edgecolors = 'white', label = 'Win')
loss_marker = plt.scatter([], [], color = colors[3], marker    = 'o', edgecolors = 'white', label = 'Loss')
fit_line    = plt.plot([],    [], color = colors[5], linestyle = ':', linewidth  = 2,       label = 'Logarithmic Fit')[0]

plt.legend(handles = [win_marker, 
                      loss_marker, 
                      fit_line], 
                      loc      = 'best', 
                      fontsize = 8)

ax = plt.gca()
ax.spines[:].set_visible(False)
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

font_updates = [ax.title, ax.xaxis.label, ax.yaxis.label] + \
                ax.get_xticklabels() + ax.get_yticklabels() + \
                plt.legend(loc = 'best', fontsize = 8).get_texts()
for i in font_updates:
    i.set_fontfamily('DejaVu Sans Mono')

# Crop the final output to remove whitespace
plt.subplots_adjust(left = 0.05, right = 0.98, top = 0.94, bottom = 0.06)

plt.show()