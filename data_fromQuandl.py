# get stock price data from Quandl

quandl.ApiConfig.api_key = "YOUR_KEY_HERE"
mydata = quandl.get("FRED/GDP")

# Turn on pagination
# Pagination returns data page by page and helps to avoid exceeding call limits
data = quandl.get_table('ZACKS/FC', paginate=True)

# Preprocess the data
# To change the sampling frequency-
mydata = quandl.get("EIA/PET_RWTC_D", collapse="monthly")
# To perform elementary calculations on the data-
mydata = quandl.get("FRED/GDP", transformation="rdiff")

# Change data formats
# To put the same data in a NumPy array-
mydata = quandl.get("EIA/PET_RWTC_D", returns="numpy")