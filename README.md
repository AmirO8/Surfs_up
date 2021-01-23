# surfs_up
SQLite

# Analysis

To analyze temperature data for the months of June and December in Oahu to see if a surf shop can be sustainable year-round.

# Results
![June Temps](https://github.com/AmirO8/surfs_up/blob/main/Resources/June_Temps.png)     ![December Temps](https://github.com/AmirO8/surfs_up/blob/main/Resources/December_Temps.png)

- June has more data points than December 1700 to 1517
- Avg temp for June 74.95°, Avg temp for December 71.04°
- The minimum temperature has the biggest difference(8°)

# Summary
Considering June is summer month and December is a winter month their average temperatures were only seperatd by 3.91°. That is a good sign as it seems that you can surf year round. The next data point I would like to see is the percipitation. I can assume that no one wants to go surfing and have ice-cream when it is raining. Adjusting the initial query we can use the following: 
 - december_rain = session.query(Measurement.prcp).filter( extract('month', Measurement.date) == '12')
 - june_rain = session.query(Measurement.prcp).filter( extract('month', Measurement.date) == '06')
 
 Below are the results:
 
 ![June Rain](https://github.com/AmirO8/surfs_up/blob/main/Resources/June%20Rain.png) ![December Rain](https://github.com/AmirO8/surfs_up/blob/main/Resources/December%20Rain.png)
