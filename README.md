# Google_trends_python
Using python to make google trends comparison.
This code uses pytrends, a package available online, to access google trends. Google Trends provides access to a largely unfiltered sample of actual search requests made to Google. It’s anonymized (no one is personally identified), categorized (determining the topic for a search query) and aggregated (grouped together). This allows us to display interest in a particular topic from around the globe or down to city-level geography. There are two samples of Google Trends data that can be accessed:

Real-time data is a sample covering the last seven days.

Non-realtime data is a separate sample from real-time data and goes as far back as 2004 and up to 36 hours before your search.

Google Trends normalizes search data to make comparisons between terms easier. Search results are normalized to the time and location of a query by the following process:

Each data point is divided by the total searches of the geography and time range it represents to compare relative popularity. Otherwise, places with the most search volume would always be ranked highest.

The resulting numbers are then scaled on a range of 0 to 100 based on a topic’s proportion to all searches on all topics.

Different regions that show the same search interest for a term don't always have the same total search volumes.

This is important, as it does not show the absolute volume, it only shows the relative volume. There is another limitation to google trends as well. It will only allow up to 5 search terms to be compared at one time, and each term is limited to 100 characters. This immediately creates a bottleneck. With this in mind the following methodology was developed.

One search term with a large volume was selected as a baseline. In this case the country of “France” was used as a search term. This means that all terms show a relative search volume in comparison to the searches for France. This data was then saved to a dictionary -> data frame -> to a CSV file.

If an error code of 400 is returned then there is something wrong on googles end. Either there was a timeout, the term was invalid, or there where too many terms entered in one query.
