# Lightning Risk Predictor
A small app to detect risk of lightning using a machine learning model trained on environmental factors.

## Approach
The initial steps will include gathering the lightning, weather, and climate data via API calls or manually downloading legacy NOAA data. We will divide the larger corpus into a subset to explore through via Jupyter notebooks with the goal of understanding the data.
We will then automate the process of extracting relevant data to define as the input nodes. Once we understand the input process, we can start to figure out the architecture for the model we want to use or build. 

# Data Pipeline
Lightning Data Time and Date -> Weather data

# References
[Earth Data Search Engine](https://search.earthdata.nasa.gov/search?portal=ghrc&lat=41.52764855906194&long=-155.53125)  
[NCEI Severe Weather Data Inventory](https://www.ncei.noaa.gov/maps/swdi/)  
[Actual Lightning and Storm Data](https://www1.ncdc.noaa.gov/pub/data/swdi/)  
[Next Gen Weather Data](https://www.ncei.noaa.gov/products/radar/next-generation-weather-radar)  
[Lightning Products](https://www.ncei.noaa.gov/products/lightning-products#:~:text=NCEI%20provides%20access%20to%20lightning,allow%20spatial%20and%20temporal%20subsetting.)  