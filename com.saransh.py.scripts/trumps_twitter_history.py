# Import pandas as pd
import pandas as pd

# Import twitter data
tweets_df = pd.DataFrame(pd.read_excel("../resources/Trump Tweets(2017).xlsx"))

# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Iterate over column names in args
    for col_name in args:

        # Extract column from DataFrame: col
        col = df[col_name]

        # Iterate over the column in DataFrame
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1

            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


# Call count_entries(): result2
result = count_entries(tweets_df, 'Tweet')

# Filter our Retweets
retweets = filter(lambda x: x[0:2] == 'RT', tweets_df['Tweet'])

# Print result

#print(list(result))
for tweet in retweets:
    print(tweet)
