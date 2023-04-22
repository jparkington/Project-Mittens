<!-- omit in toc -->
# Project Mittens
<!-- omit in toc -->
## Analyzing the Impact of Chess Bots on Player Performance and Elo Ratings

This repository contains an academic paper, visualizations, and supporting data for a project that investigates the impact of chess bots on player performance and Elo ratings. The paper analyzes various aspects of chess, including move sequences, complexity, and skill level, and concludes that the increased accessibility of chess bots has had a significant influence on players' skill levels, both naturally and artificially.

<!-- omit in toc -->
## Table of Contents

- [Introduction](#introduction)
- [Paper Overview](#paper-overview)
- [Visualizations](#visualizations)
  - [List of Visualizations](#list-of-visualizations)
- [Data](#data)
- [Setup and Usage](#setup-and-usage)
- [Authors and Acknowledgements](#authors-and-acknowledgements)
- [License](#license)

## Introduction

The game of chess has experienced a surge in popularity in recent years, driven by factors such as accessible online platforms, popular chess streamers, and mainstream television shows like "The Queen's Gambit." This increased attention has been accompanied by the rapid development of advanced chess bots, which have not only attracted new players but have also raised questions about the impact of these bots on player performance and the Elo rating system.

The paper in this repository, titled "Project Mittens," explores these questions and seeks to substantiate the following hypotheses:

1. Elo as a mathematical construct is positioned to scale with the introduction of a new “population” of players as bots, which can compute depths of move sequences too large for humans to comprehend.
2. Experienced players have an intrinsic understanding of Elo and its variations from platform to platform, and therefore can make educated guesses about a competitor’s strength based on their opening choices, demonstration of known winning variations, and overall ability to generate creative patterns of move sequences.
3. The algorithms chess bots use to play at previously unreached levels of precision and accuracy have become increasingly more efficient than humans at processing move sequences over time, resulting in their accessibility for a wider audience.
4. Humans have shifted their perception of “good” chess and their ability to recreate it in large part to the increased accessibility of bots, positively impacting their skill levels, both naturally and artificially (via cheating).

## Paper Overview

The academic paper, "Project Mittens," is available [here](https://github.com/jparkington/Project-Mittens/blob/main/Project%20Mittens.pdf). It discusses various aspects of chess, including:

- Estimating the number of possible games
- Comparing chess with other games
- Analyzing Perft results to calculate branching factors
- Measuring the growth of complexity
- Contextualizing acumen for move sequences
- Quantifying chess acumen
- Past & present Elo values
- Projecting a test case's ratings
- The bot bump
- Bots and their algorithms

## Visualizations

This repository contains a series of pyplot visualizations that range from simple bar charts to custom logarithmic regressions, showcasing various aspects of the analysis conducted in the paper. These visualizations were created using Python and Jupyter Notebooks in Visual Studio Code.

### List of Visualizations

1. Branching Factors (b(d) vs. d)
2. Growth Rates (g(d) vs. d)
3. Delta Rating vs. Game Number
4. Common Games: Estimated Branching Factors
5. Possible Games (p(d) vs. d)
6. Actual vs. Projected Rating
7. Average FIDE Rating by Year of Each Year's Top N% Players
8. Bot Ratings vs. Delta Ratings of Top 1% Players and 10% Players

For more details on each visualization, please refer to the comments in the corresponding Jupyter Notebook.

## Data

The data used in this project consists of FIDE ratings from 1971 to 2023. The data is sourced from two locations:

- Files from 2000 and earlier are provided by Mark Weeks (https://www.mark-weeks.com/chess/ratings/)
- Files after 2000 are obtained from the official FIDE website (https://ratings.fide.com/download.phtml)

All files from these sources have been converted into CSV format with the Player, Country, and Ratings fields extracted from their various schemas.

## Setup and Usage

This project uses Python and Jupyter Notebooks in Visual Studio Code to render the visualizations and dataframes. To set up the project and reproduce the visualizations, follow these steps:

1. Install [Python](https://www.python.org/downloads/) and [Visual Studio Code](https://code.visualstudio.com/download).
2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code.
3. Install the required packages: matplotlib, numpy, pandas, seaborn, scipy, scikit-learn
4. Clone this repository and open the Jupyter Notebook files in Visual Studio Code.
5. Run the cells in each Jupyter Notebook to generate the visualizations.

## Authors and Acknowledgements

This project was developed by:

- [James Parkington](https://github.com/jparkington)
- Dan Hayes
- Kate Brown

Their work was shaped under the supervision of [Professor Weston Viles](https://roux.northeastern.edu/people/weston-viles/) during class *5002 - Discrete Mathematics* at the **Roux Institute of Northeastern University**.

We would like to express our gratitude to Professor Viles for his guidance and support throughout this project, as well as our classmates for their valuable input and collaboration.

## License

This project is not subject to any specific licensing. The data sources (Mark Weeks and FIDE) have their respective terms of use, which can be found on their websites.