# House Rocket - Data Analysis

   <p align="center">
      <img width="600" height="300" src="!https://user-images.githubusercontent.com/87772120/141787219-33dab969-37e8-4c43-b3a6-1ba6dc7a2644.png">
   </p>   





This project contains American real estate analytical insights based on datasets made available by the House Rocket Company in King County (USA)

Case study:
This study project aims to develop tools and panels to answer business questions created by the company's CEO and allow him or other members of the company to have access to different roles for the tool as they select in the filters.

1. Business problem
  House Rocket is currently in the real estate market buying and reselling properties through a digital platform. The data scientist is responsible for developing an online dashboard that can be accessed by the CEO from a cell phone or computer with information on properties sold in King County (USA).

  The panel must contain:

  - Data Overview - Database Overview;
  - Properties by zip code - information about properties grouped by zip code;
  - Portfolio Density Map - A map view with database distribution;
  - Property price by timeline - property price by year of construction or by sale date and property price distribution;
  - Distribution of properties by main attributes - distribution of properties by number of bedrooms, bathrooms, floors and whether or not the property has a sea       view;
  - Custom Data and Map View - A section to choose attributes and see the dataframe and map distribution of these properties.

2. Business Assumptions
  Available data are only from May 2014 to May 2015.
  The variables are as follows:
   
| Variable	| Definition |
| :---------------- | :---------------- |
|id	| Unique ID for each property sold |
|date	| Date of the property sale |
|price	| Price of each property sold |
|bedrooms	| Number of bedrooms |
|bathrooms	| Number of bathrooms, where .5 accounts for a room with a toilet but no shower, and .75 or ¾ bath is a bathroom that contains one sink, one toilet and either a shower or a bath.|
| sqft_living	| Square footage of the apartments interior living space|
| sqft_lot	| Square footage of the land space|
| floors	| Number of floors |
| waterfront	| A dummy variable for whether the apartment was overlooking the waterfront or not|
| view	| An index from 0 to 4 of how good the view of the property was|
| condition	| An index from 1 to 5 on the condition of the apartment| 
|grade	|An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above	|The square footage of the interior housing space that is above ground level|
|sqft_basement	|The square footage of the interior housing space that is below ground level|
|yr_built	|The year the property was initially built|
|yr_renovated	|The year of the property’s last renovation|
|zipcode	|What zipcode area the property is in|
|lat	|Lattitude|
|long	|Longitude|
|sqft_living15	|The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15	|The square footage of the land lots of the nearest 15 neighbors|

3. Solution Strategy
   - Understanding the business model;
   - Understanding the business problem;
   - Collecting the data;
   - Data Preparation;
   - Exploratory Data Analysis;
   - Dashboard deploy on Heroku.

4. Conclusion
   The objective of this study case was to create a online dashboard to House Rocket's CEO. Deploying the dashboard on Heroku platforms provides the CEO acess from anywhere facilitating both pre-arrange or costumized data visualization.
   
5. Next Steps
   - Create and analyze some business hypotheses;
   - Flag the recommendation to buy or not the properties in the dataset;
   - Flag the sales recommendation with an increase of 10% or 30%;
   - Update the online dashboard with these improvements. See more at: https://houserocket-analytics-data.herokuapp.com/


References:

- Python from Zero to DS lessons on "Comunidade DS - course"
- Blog Seja um Data Scientist
- Dataset House Sales in King County (USA) from Kaggle
- Variables meaning on Kaggle discussion
- Icons made by https://www.flaticon.com/authors/monkik from https://www.flaticon.com/free-icon/data_993688?term=data%20analysis&related_id=993688
