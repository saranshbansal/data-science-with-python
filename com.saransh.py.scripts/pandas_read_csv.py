# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.DataFrame(pd.read_csv("../resources/cars.csv"))
tweets = pd.DataFrame(pd.read_csv("../resources/tweets.csv"))
jobs = pd.DataFrame(pd.read_csv("../resources/Information_gain_job_advertisements.csv"))
industries = pd.DataFrame(pd.read_json("../resources/industries.json"))

# Print out cars
print(cars.describe())

# Print out tweets
print(tweets.keys())

# Print all columns of industries
print(list(industries.resultList))
