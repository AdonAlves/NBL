# NBL Win Percentage Estimator: Project Overview
- This project is designed to develop my own skills within sport analytics. The specific skills I am looking to develop in coding are improved efficiency with python and libraries such as Pandas and matplotlib, seaborn, and Sci Kit learn. 
- Scraped All data from the RealGM BasketBall webstie for the NBL. Unfortunatlely it only contained data from 2012- 2020 seasons. 
- Utilised Exhaustive Feature selection, lineear regression, and normalization of data from the Sci Kit learn Library 
- The features the Exhaustive Feature Selection suggested were effective Field Goal% for both teams, opponent Personal Fouls, Team Offensive and Defensive Rebound %,  both the Team and opponents  Turnover Percentage, and the opponents number of personal fouls. 
- This project has the potential to assist coaches and players in improving their win percentage, through the modification of play style.  It appears that having a significant number of personal fouls can increase the overall win% of the opposing team, it is currently hypothesised that due to the free-throw% being quite high over the two Free throws awarded on a foul that you are giving away ~1.5 points. 
- eFG%,turnovers and rebounds are self explanatory as most coaches are already looking at this stats 
## Code and Resources Used
Python Version : 3.7 

Packages: Pandas, numpy, sklearn, matplotlib, seaborn, mlxtend

## Data Cleaning 
Fortnunately for all the data collected there were no empty values, so all that was required was to merge all the different metrics into a single data frame for each year and then drop the team names, and merge all the years into a single dataframe. 

## Exploratory Data Analysis 
Seaborn and matplotlib were used to generate histograms to determine the distribution of data. Unfortunately due to the nature of the NBL having so few games and Teams within a season very little data was actually collected and there may still be significant changes in play style over recent years being impacted with the 3Point boom. 

Initially I used seaborn to eliminated data from the original dataframe that did not have a normal distribution, as a result percentage based stats had normal distributions and then. I removed data that was either a combination of other data or a component based on the the linear relationship to the win/loss percentage. 

For the figure showing the histograms please see Figure 2020-09-14 130300 in the repository as it is too large to display in the readme. 

Once complete, it was run through the exhaustive feature selection in a linear regression model which selected the following 8 Variables  eFG%, OppeFG%, ORB%, DRB%, TOV%, OppTOV%, STL% and AverageOppPF. 


## Proposed linear model for predicting win% 
Where all percentages are given as decimals. 

Win% = -0.41 + (2.4 * eFG%) - (2.62* OppeFG%) + (7.8+ORB%) + (0.87 * DRB%) - (4.25 * TOV%) + (4.31 * OppTOV%) - (1.82 * STL%) + (0.0001 * AvgOppPF)


## References 
inspiration for the model was provided by Ken Jee his youtube link is https://www.youtube.com/c/KenJee1/videos
Mathletics: How Gamblers, Managers, and Sports Enthusiasts Use Mathematics in Baseball, Basketball, and Football
Book by Wayne L. Winston
Computerphiles youtube chanel was used to help improve my understanding of data science https://www.youtube.com/user/Computerphile
Pandas, matplotlib, seaborn, sklearn, mlxtend UserGuides were used to understand the tools used within the project

## Prior Information Gathered from mathletics  
The Four Factor models for team offense and defense from the book Mathletics
Offense: 
  1. EFG 
  2. TPP 
  3. ORP 
  4. FTR
Defense: 
  1. Opponent EFG 
  2. Defensive TPP 
  3. DRP 
  4. Opponents FTR

