# Predicting StepMania Song Difficulty Using Regression  

## Introduction  
### About StepMania  
Stepmania is an open-source software designed to support many styles of rhythm game play, but one of its most widely-used formats is for 4-panel “dance games” (like Dance Dance Revolution or In The Groove, but not licensed). The software was released in 2001 and has since been updated through version 5.3 - the concept behind this software is to allow players to play a “DDR-like” game with virtually boundless customizations, including custom themes, statistics, and charts (arrow patterns for songs).  

### Problem  
There is not currently a standardized scale or model for determining chart difficulty being used within the community, leaving the determination up to step-artist and community input. While extensive domain experience means that chart ratings are relatively consistent, there is variance that can be addressed.

### Proposal  
The problem that I aim to solve is using exploratory data analysis and predictive modeling to help establish a standardization for song chart difficulty ratings based on various features of the chart, such as BPM, number of steps, and counts of technical elements.

### Motivation  
Creating a method of standardization will help examine which features are the most important in determining difficulty and help
step-artists remove the intuitive/guesswork element from rating their own charts. 

## Data  
### Collection  

[itgpacks.com](www.itgpacks.com) is a community-maintained spreadsheet containing the majority of song packs released in the last five years. The majority of this data came from here, with the exception of a few packs downloaded from other sources.   

The data is extracted from each individual song file using a parser written in Python to collect the features used for EDA and predictive modeling. A huge, huge, huge thank you to Tim Murphy, a friend and dance game player, for writing the code for this parser. You can check out their [GitHub] and [another link to something of theirs].  


### Folder Structure    
The data is stored in `data` in two folders: `stam.csv` and `not_stam.csv`. Please keep the folder structure the same way for this notebook to work. If you would like to include your own song files, it is recommended to have them in a folder inside of `data`, then using the parser to generate a csv file like so:

```
!python chart_parser.py data/your_song_folder data/your_songs.csv
```

Then, when reading into a DataFrame, replace the 'not_stam' variable and delete the 'stam' variable:  

```
stam = pd.read_csv('data/your_songs.csv')
``` 


### Song Features  
[Here]('data/feature_dictionary.txt') you can find a full list of each generated feature and a a brief description.  

## Methods  
### EDA / Visualizations  

### First Simple Model  

### Iterative Model Building

## Final Model  

## Results  

## Conclusions / Next Steps  

### Repo Structure  

### Acknowledgements / Thank Yous
