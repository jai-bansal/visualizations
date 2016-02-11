# This script creates a choropleth map of the contiguous United States using (a subset of) 'census_data.csv'.

# A description of 'census_data.csv' can be found in 'census_data_scrape_and_process.R'.
# To avoid an overwhelming plot, I will be using a subset of 'census_data.csv' consisting of
# all observations for the year 2010.

# Import modules.
import pandas as pd
import plotly

# Load data.
census_data = pd.read_csv('census_data.csv',
                          encoding = 'latin-1')

# SUBSET/PROCESS DATA.

# Restrict 'census_subset' to '2010' observations only.
census_subset = census_data[['Name', '2010']]

# Remove aggregate 'United States' population row.
census_subset = census_subset[census_subset['Name'] != 'United States']

# Divide '2010' population value by 1000 for easier graph viewing.
census_subset['2010'] = census_subset['2010'] / 1000

# Add state abbreviations. This is necessary for plotting.
census_subset['abbreviations'] = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
                                                'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
                                               'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

# PLOT DATA.

# Specify color scale using 'red, green, blue' coordinates.
color_scale = [[0.0, 'rgb(255, 255, 255)'],
               [0.2, 'rgb(102, 102, 255)'],
               [0.4, 'rgb(51, 51, 255)'],
               [0.6, 'rgb(0, 0, 255)'],
               [0.8, 'rgb(0, 0, 204)'],
               [1.0, 'rgb(0, 0, 102)']]

# Create choropleth.
choropleth = [dict(
                            type = 'choropleth',
                            colorscale = color_scale,
                            locations = census_subset['abbreviations'],
                            z = census_subset['2010'].round(1),
                            locationmode = 'USA-states',
              colorbar = dict(
                                  title = 'Population (in thousands)'))]

# Create layout.
layout = dict(
                    title = '2010 United States Population (in thousands) by State',
                    geo = dict(
                                    scope = 'usa',
                                    showlakes = False),
                    font = dict(size = 35))

# Plot figure.
# Figure opens in a browser tab.
plotly.offline.plot(dict(data = choropleth,
                         layout = layout))
