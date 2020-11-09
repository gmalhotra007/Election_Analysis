# Election_Analysis

### Overview of Election Audit
---
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local ongressional election.

- Calculate the total number of votes cast
- Get a complete list of candidates who received votes
- Calculate the total number of votes each candidate recived.
- Calculate the percentage of votes each candidate won.
- Determine the winner of the election based on popular vote.
- Calculate county votes
- Calculate largest county turnout 

### Election-Audit Results
---
1. How many votes were cast in this congressional election?
    - Total number of votes: 369,711

2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    #### *Number of votes for each county:*
    - Jefferson: `38,855`
    - Denver: `306,055`
    - Arapahoe: `24,801`\
     *for county_name in county_list:\
    votes = county_votes.get(county_name)*

    #### *Percentage of total votes for each county:*
    - Jefferson: `10.5%` 
    - Denver: `82.8%` 
    - Arapahoe: `6.7%` \
    *votes_percentage = float(votes) / float(total_votes) * 100*   

3. Which county had the largest number of votes?
    - `Denver` has the largest number of votes\
    *largest_county = ""\
    county_voter_turnout = 0\
    if (votes > county_voter_turnout):\
    county_voter_turnout = votes\
    largest_county = county_name*

4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    #### *Number of Votes each candidate recieved:*
    - Charles Casper Stockham: `85,213`
    - Diana DeGette: `272,892`
    - Raymon Anthony Doane: `11,606`\
    *for candidate_name in candidate_votes:\
    votes = candidate_votes.get(candidate_name)*
        
    #### *Percentage of the Votes each candidate recieved:*
    - Charles Casper Stockham: `23.0%`
    - Diana DeGette: `73.8%` 
    - Raymon Anthony Doane: `3.1% `\
    *vote_percentage = float(votes) / float(total_votes) * 100\
    candidate_results = (f"{candidate_name}{vote_percentage:.1f}% ({votes:,})\n")*


5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    - Diana DeGette won the election with `vote count of 272,892` and `percentage of total votes 73.8%` 

### Election-Audit Summary
---
The analysis of the election shows that:
- There were 'x' votes cast in the election
- The candidates were:
    - Candidate 1
    - Candidate 2
    - Candidate 3
- The candidate results were:
    - Candidate 1 recieved "x%" of the vote and "y" number of votes.
    - Candidate 2 recieved "x%" of the vote and "y" number of votes.
    - Candidate 3 recieved "x%" of the vote and "y" number of votes.
- The winner of election was:
    - Candidate (1,2,or3), who recieved "x%" of the vote and "y" number of votes.
- The number of counties:
    - County 1
    - County 2
    - County 3
- The County results were:
    - County 1 recieved "x%" of the vote and "y" number of votes
    - County 2 recieved "x%" of the vote and "y" number of votes
    - County 3 recieved "x%" of the vote and "y" number of votes
- The largest county turnover:
    - largest_county = ""\
county_voter_turnout = 0
    - if (votes > county_voter_turnout):\
            county_voter_turnout = votes\
            largest_county = county_name
