# Election_Analysis

## Overview of Election Audit
This election audit was conducted for a Colorado Board of Elections employee for a recent local congressional election. I accomplished this by creating a Python script to conduct the following steps:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county
7. Calculate the percentage of votes from each county out of the total count
8. Determine the county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.52.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 total votes cast in the election.
- The counties that voted in the election were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results:
    - Jefferson county casted 10.5% of the total votes and a total of 38,855 number of votes.
    - Denver county casted 82.8% of the total votes and a total of 306,055 number of votes.
    - Arapahoe county casted 6.7% of the total votes and a total of 24,801 number of votes.
- The largest county voter turnout was seen in:
    - Denver
- The candidates were: 
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election Audit Summary
This election audit script can be used for any election as long as the data source .csv file follows a similar format where the county is in the second column and the candidate name is in the third column. However, if the data were not to follow this order, the code can be modified to cater to this. If the county was in the fourth column instead, the script (line 52) would be modified to county_name = row[3] rather than the existing row[1] to accomodate this change. Similarly, if the candidate name was in the first column rather than the third column, the script (line 49) would be modified to candidate_name = row[0] rather than the existing candidate_name = row[2] to reference the correct column in the file. 

Another changepoint in the script would be required if there was a request to track the results of other features too other than the county and candidate. For instance, there could be a request to track the country, municipality, and/or state as well. The script would have to be modified to store the list of countries/municipalities/states and would have to calculate the total number of votes per country/municipality/state. This would follow the same format as the county and candidate, but new variables would need to be created and additional code to accomodate this would have to be added to the existing Python script. 
