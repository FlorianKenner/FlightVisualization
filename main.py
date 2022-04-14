import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
import plotly


AlleFluegeURL = "https://gist.githubusercontent.com/florianeichin/cfa1705e12ebd75ff4c321427126ccee/raw/c86301a0e5d0c1757d325424b8deec04cc5c5ca9/flights_all_cleaned.csv "
SubsetURL = "https://gist.githubusercontent.com/florianeichin/b877d354d6bc52e6ce840572e40b0497/raw/19759410471073756a388dada5fcb40109f0d13e/flights_subset_cleaned.csv"
OriginalDatenURL = "https://www.kaggle.com/usdot/flight-delays#flights.csv"

# Loading Data from the URL
df = pd.read_csv(AlleFluegeURL)
df.head()
df.profile_report()
