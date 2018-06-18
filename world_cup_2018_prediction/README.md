Reference:
https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017

The dataset is from kaggle.
This dataset includes 39,054 results of international football matches starting from the very first official match in 1972 up to 2018. 
The matches range from World Cup to Baltic Cup to regular friendly matches.

The matches are strictly men's full internationals and the data does not include Olympic Games or matches,
where at least one of the teams was the nation's B-team, U-23 or a league select team.

results.csv includes the following columns:

date - date of the match
home_team - name of the home team
away_team - name of the away team
home_score - full time home team score including extra time, not including penalty-shootouts
away_score - full time away team score including extra time, not including penalty-shootouts
tournament - name of the tournament
city - name of the city/town/administrative unit where the match was played
country - name of the country where the match was played
neutral - TRUE/FALSE column indicating whether the match was played at a neutral venue

Note on team and country names: For home and away teams the current name of the team has been used. 
For example when in 1882 a team who called themselves Ireland played against England, 
in this dataset it is called Northern Ireland because the current team of Northern Ireland is the successor of the 1882 Ireland team. 
This is done so it is easier to track the history and statistics of teams.

For country names the name of the country at the time of the match is used. 
So when Ghana played in Accra, Gold Coast in the 1950s, even though the names of the home team and the country don't match, it was a home match for Ghana. 
This is indicated by the neutral column, which says FALSE for those matches, meaning it was not at a neutral venue.



