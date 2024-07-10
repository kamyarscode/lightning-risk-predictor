# Lightning Risk Predictor
A dockerized Python app to detect risk of lightning using a machine learning model trained on environmental factors.

## Approach
The initial phase will predominantly be a lot of research that needs to go into gathering the lightning, weather, and climate data via API calls or manually downloading legacy NOAA data. We will divide the larger corpus into a subset to explore through via Jupyter notebooks with the goal of understanding the data.  

We will then automate the process of extracting relevant data to define as the input nodes. Once we understand the input process, we can start to figure out the architecture for the model we want to use or build.  

The initial phase will also include a good amount of data cleaning to prep for model input. 

## Install Procedure

#### Running or debugging without Docker:
You will first need to install the repository. You can do this with:
`python -m pip install --editable .`

## Data Pipeline

The current approach will take occurrences of lightning and fetch the coordinates for them. Once we have the coordinates and time, we can cross check this with weather and climate data for the same time and coordinates to see the conditions. We will need to average the times and add tolerances for coordinates and time as well since it will be tedious to get the _exact_ data. Close estimates will be good enough for intial testing purposes. Once we extract this data, a larger corpus will be created and that will be the majority of the data we use.
## Model
At this time there is no plan to upload the model, but the dataset will be made available on Kaggle or another archive/respository.

## References
[Earth Data Search Engine](https://search.earthdata.nasa.gov/search?portal=ghrc&lat=41.52764855906194&long=-155.53125)  
[NCEI Severe Weather Data Inventory](https://www.ncei.noaa.gov/maps/swdi/)  
[Actual Lightning and Storm Data](https://www1.ncdc.noaa.gov/pub/data/swdi/)  
[Next Gen Weather Data](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar)  
[Lightning Products](https://www.ncei.noaa.gov/products/lightning-products#:~:text=NCEI%20provides%20access%20to%20lightning,allow%20spatial%20and%20temporal%20subsetting.)  
[NOAA Token Request Page](https://www.ncdc.noaa.gov/cdo-web/token)  