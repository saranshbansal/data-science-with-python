# Listing sheets in Excel files
#
# Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in
# time. You won't always want to do so in Excel, however!
#
# Here, you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any
# loaded .xlsx file.
#
# Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of
# the sheet names using the attribute spreadsheet.sheet_names.
#
# Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace
# Research Institute Oslo's (PRIO) dataset. This data contains age-adjusted mortality rates due to war in various
# countries over several years.

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
