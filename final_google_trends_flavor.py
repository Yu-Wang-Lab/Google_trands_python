from pytrends.request import TrendReq
import pytrends
import time
import pandas as pd
from random import randint

# Importing the data from a CSV file.

df = pd.read_csv(r"List_of_flavors_final.csv", encoding = 'unicode_escape')

# It is imported as a nested list so I need to flatten it.

nested_list = df.values.tolist()

# Creating a Keyword list from the flattened list.

kw_list = []
for xs in nested_list:
    for x in xs:
        kw_list.append(x)

# connect to google
pytrends = TrendReq(hl='en-US', tz=360)

# Creating dictionary to store the data.

trends_2 = dict()

# Using a for loop to compare google trends of the word against the word France.
# There is a sleep time in the loop that will randomly wait between 45 and 75 seconds.
# This is to prevent google's DDOS defense from triggering. I think less time is required but I 
# was uncertain what the minimum time would be. About 1 min felt right and was able to work.
###### When time was lowered Google shut me out. Keep minimum of ~ 1 minute.


# After running for so long the function stopped working. The data that was collected was saved.
# Re-running again from previous stop point (in this case 600).

for i in kw_list[600:]:

   ##build out query
   ##timeframe will start 5 years ago and will be collected weekly until the day it is run.
   ## Orange flavor was found to be the highest flavor when compared to France. This search 
   ## term was chosen as france was so high in count that it made many flavors appear 
   ## as 0.

    pytrends.build_payload([i,'orange flavor'], cat=0, timeframe = 'today 5-y')
   
   ##save trend to dictionary

    trends_2[i] = pytrends.interest_over_time()[i]
    time.sleep(randint(45,75))

# Converting the dictionary into a data frame.

orange_flavor_comparison_data = pd.DataFrame(trends_2)

# Converting the data frame to a CSV file. 
# Might change name of file later.....

orange_flavor_comparison_data.to_csv(r'Google_trends_flavor.csv', index = True)