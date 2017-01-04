#### Synopsis:
This project creates visualizations in R and Python, contained in the R and Python branches, respectively. 
For each visualization, there is a creation script and an image of the output
(except for the R branch motion chart; an image of this would defeat the purpose of the plot but running the script launches a browser
containing the motion plot).
There is an image for the 3D scatter plot in the Python branch, but running the script is preferable as it generates a figure which can be rotated and adjusted in real time.
Most R [Python] plots are created using ggplot2 [matplotlib].
Here are the visualizations in each branch listed alphabetically.

R:
- 3D scatter plot
- bar graph
- choropleth
- correlation plot
- histogram
- line graph
- motion chart
- multi plot grouped bar graph
- pie chart
- scatter plot
- stacked bar graph

Python:
- 3D scatter plot
- bar graph
- choropleth
- correlation plot
- histogram
- line graph
- multi plot grouped bar graph
- pie chart
- scatter plot
- stacked bar graph

#### Motivation:
I created this project to explore various visualizations.

#### Dataset Details:
The data consists of the population of each US state for 1960, 1970, 1980, 1990, 2000, and 2010.
This data comes from the United States Census and can be viewed at:
*https://en.wikipedia.org/wiki/List_of_U.S._states_by_historical_population*

Added to this is the area of each state. This data comes from Wikipedia and can be viewed at:
*https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area*

Each branch contains 'census_data_scrape_and_process' (.R or .py depending on the branch).
This script scrapes the data from the web. 
Each branch also contains 'census_data.csv', which is the data file used in all visualizations.

#### License:
GNU General Public License
