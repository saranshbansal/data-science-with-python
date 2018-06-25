# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.DataFrame(pd.read_csv("../_datasets/cars.csv"))
tweets = pd.DataFrame(pd.read_csv("../_datasets/tweets.csv"))
jobs = pd.DataFrame(pd.read_csv("../_datasets/Information_gain_job_advertisements.csv"))
industries = pd.DataFrame(pd.read_json("../_datasets/industries.json"))

# Print out cars
print(cars.describe())

# Print out tweets
print(tweets.keys())

# Print all columns of industries
print(list(industries.resultList))
