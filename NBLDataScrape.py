#import pandas
import pandas as pd
#scrape team total data 
tt = pd.read_html("https://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Totals/Team_Totals")
for df in tt:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Team_Total_12.csv', index = False)
print("Team total data complete")
#scrape team average data 
ta =pd.read_html('https://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Averages/Team_Totals')
for df in ta:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv("Team_Avg_12.csv", index = False)
#scrape team metrics data 
print("Team average data complete")
tm = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Advanced_Stats/Team_Totals")
for df in tm :
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv("Team_Metrics_12.csv", index = False)
print("Team metrics complete")
#scrape opponent total data 
ot = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Totals/Opponent_Totals")
for df in ot:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Opp_Total_12.csv', index = False)
print("Opponent total data complete")
#scrape opponent average data
oa = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Averages/Opponent_Totals")
for df in oa:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Opp_Avg_12.csv', index = False)
print("Opponent Average data complete")
#scrape opponent metric data
om = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2012/Advanced_Stats/Opponent_Totals")
for df in om:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Opp_Metrics_12.csv', index = False)
print("Opponent Metrics complete")
#scrape player total data
pt = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2012/Totals/All/All/points/All/desc/1/Regular_Season")
for df in pt:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Player_Total_12.csv', index = False)
print("Player Totals complete")
#scrape player average data
pa = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2012/Averages/All/All/points/All/desc/1/Regular_Season")
for df in pa:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Player_Avg_12.csv', index = False)
print("Player Averages complete")
#scrape player metrics data 
pm = pd.read_html("http://basketball.realgm.com/international/league/5/Australian-NBL/stats/2012/Advanced_Stats/All/All/points/All/desc/1/Regular_Season")
for df in pm:
    df.drop( ['#'], axis=1, inplace = True)
    df.to_csv('Player_Metrics_12.csv', index = False)
print("Player Metrics complete")
#complete
print("All data has been collected")

