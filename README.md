# House Rocket Project

![alt text](https://github.com/jaohenritm/House-Insights-Project/blob/main/istockphoto-109350668-612x612.jpg?raw=true)

The objective of this project is to provide the business team of a fictitious company a recommendation of which houses avaiable in
a portfolio they should buy.

The visualization tool used in this project is the Streamlit, which can enable the company to visualize this result graphically,
use localization maps and tabulate.

The result achieved is a selection of **8354 real estates** which corresponds to 38,65% of the properties in the avaiable portfolio.
Assuming that the House Rocket would buy and sell all these properties with a price atleast 40% higher than they bought and estimating
that the company would spend atleast 10% of the total value of the house in reforms, we should expect a maximum profit of **$1,612,361,730.29 dollars**.

| **Total of Properties** | **Total Cost** | **Total Revenue** | **Profit** |
| --- | --- | --- | --- |
| 8354 | $5,374,539,101.00 | $7,524,354,741.40 | $1,612,361,730.29

## Dashboard:   <a href="https://daxboard-house-rocket.herokuapp.com/" target="_blank"><img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" target="_blank"></a>
</div>


## 1. House Rocket

### 1.1 Business Context
House Rocket is a company whose business model is the purchase, renovating and sale of real estate.
The purpose of the case is to provide insights for the company to find the best business opportunities in the real estate market.

Their main strategy is to buy potential good homes that needs some renovation and then later resell them at higher prices.
The greater the difference between the purchase and the reform of the sale value, better will be their profit.

Our objective is to analyse which attributes play the main role of affecting the house prices and what the company should do
with them.

### 1.2 Motivation behind this Project
Considering that:

a) The business team can't take good decisions without analysing the data, and;
b) The portfolio is too large, which it would take a lot of time to do it manually.

The main goal of this project is to use the abilities and tools of the Data Science 
to make a selection with the best real estates opportunities that will provide the maximum profit for the company.

- Which real estates that House Rocket should purchase?
- Once the house is purchased, when is the best time to sell it and at what price? 

### 1.3 Data Description

The data was extracted from Kaggle where it lists all real estates on portfolio that are avaiable for the company to purchase.

https://www.kaggle.com/harlfoxem/housesalesprediction

In total, there are 21 attributes and 21613 records on this record.

| **Attributes** | **Description** |
| --- | --- |
| id | Unique identification of each property |
| date | Date that the house was put on for sale |
| price | Price that the house is being sold by it's owner |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| sqft_living | Measure in square feet of the total interior area of the property |
| sqft_lot | Measure in square feet of the total area |
| sqft_above | Measure in square feet of the above area |
| floors | Number of floors in the property |
| waterfront | Indicates the presence of water view or not (0 = no and 1 = yes) |
| view | Indicates the quality of the view (0 = Terrible and 4 = Great) |
| condition | Indicates the condition of the house (1 = Terrible and 5 = Great) |
| grade | Indicates the quality of the construction and design of the building (1 = Terrible and 13 = Great) | 
| sqft_basement | Measure in square feet of the total area of the basement | 
| yr_built | Year that the house has been built |
| yr_renovated | Year that the house has been renovated (0 = no renovation) |
| zipcode | Zipcode of the property | 
| lat | Latitude |
| long | Longitude |
| sqft_living15 | Measure in square feet of the total interior area of the 15 neighboors that are closer |
| sqft_lot15 | Measure in square feet of the total area of the 15 neighboors that are closer |

In addition to the dataset, it was also used a geojson archive for density maps. The API was extracted from the site ArcGIS Hub.

### 1.4 Business Premises
- Values that are equal to 0 in yr_renovated are houses that were never reformed.
- Duplicated values on id column were removed and just remained the more recent one.
- The condition, number of bathrooms and number of floors were the chosen attributes to determine the recommended properties.
- The row with bathrooms equals 33 was removed because it was considered an error.
- Column price is the price which the house will be purchased by House Rocket company.

It was assumed that the selling price would be 40% higher after the renovations are done in the property, and for properties that
are not gonna be renovated, only 10% using the season in favor.

## 2 Reaching the Solution

### 2.1 Data Exploration

The first step was to collect, treat and explore the data. After that it was possible to verify the necessity of doing some transformations
in the data like the creation of new attributes to provide some insights, and some conversions (square feet to square meter).

New features:
- m2_living: Measure in square meter of the interior area of the property
- m2_lot: Measure in square meter of the total area of the property
- m2_above: Measure in square meter of the above area
- m2_basement: Measure in square meter of the basement area
- month: Which month the house was put on for sale
- season: Which season the hosue was put on for sale
- old: Index that measures if the house is older than 1955 or not. (0 = older than 1955, 1 = newer than 1955)
- recent_reform: Index that says if the house was renovated in the last 5 years. (no or yes)

### 2.2 The Selection

After doing all the filtering and analysis, now it was time to create an app where the company could consult which house to buy, the recommendations,
 the insights and other informations.
 
**a) Which house should the House Rocket purchase?**

For that we verified which attributes have influence in the price formation and it was detected that there were some interesting things that they could do
to maximize the profits.
- Buy properties during winter and fall when they are with a lower cost due to low demand.
- Buy properties with 2 floor and add a 0.5 level.
- Buy properties with condition 2 and do some renovations that would make it to a condition 3 property.

**b) Once that the house is purchased, when is the best time to sell it?**

Very simple, the best time to do that is especially during the spring right after the winter ends and the demands returns to get higher.
 
### 2.3 Visualization

One of the main objectives of this project is to let the business team of the House Rocket company do their own analysis. For that we created an dashboard
with some maps, spreadsheets to facilitate the visualization of the data.

In the dashboard we got the original dataset for doing some consulting if necessary, but also some interesting maps like the density price where we can see
where are the most expensives places to buy some houses. Other one is the portfolio density where it lists every recommended property on the map where you can
interact and see also the house price.

![alt text](https://github.com/jaohenritm/Project-House-Rocket/blob/main/density_price.png)

![alt text](https://github.com/jaohenritm/Project-House-Rocket/blob/main/portfolio_density.png)

## 3 Insights
 
To start planning what to do, we started making questions to ourselves of what do we wanna know about the data. So some hypothesis were made and
the next step was to verify if they were true or not.
 
| **Hypothesis** | **Result** | **Business Language** |
| --- | --- | --- |
| The best time to sell Real Estate is during the Summer Season | False | It was verified that the best month to sell real estate is the spring season |
| Houses with waterview are more expensive. | True | Houses with waterview are in average 212% more expensive |
| New houses have higher prices than old ones. | False | The age of the house doesn't seem to affect the price, but their condition. |
| The price of the houses gets higher from year to year. | False | The age of the house doesn't seem to affect the price |
| For every half floor level added to the house, it's price raises by 20% | False | Every half floor level added to the house, the price raises in average 24% |
| Recent renovated houses got higher prices. | True | Houses that got recently renovated have in average prices 28% higher than houses that did not. |
| For every bathroom, the house price raises 10%. | False | Every bathroom added to the property, makes it's price goes 41% higher in average. |
| Every 1 level in condition, the price raises by 10%. | False |  The price difference between houses with 1 level difference to another in average is 18%. |
 
## 4 Financial Results

The objective of this project was to propose a list of real estates with options for purchase, sell and the maximum profit that could be obtained if all these
transactions occurs. So, let's see the results that House Rocket would achieve if the company follows every instruction.

| **Total of Properties** | **Total Cost** | **Total Revenue** | **Profit** |
| --- | --- | --- | --- |
| 8354 | $5,374,539,101.00 | $7,524,354,741.40 | $1,612,361,730.29
 
Otherwise we shall remember that every property can also be sold with a price 10% higher than it was bought without spending with reforms, so the results can
vary depending on what the business team will do with the property.
 
## 5 Conclusion

The main goal of this project was to generate some insights for the business, aswell to answer some questions made by the company. The objective was concluded 
as it was possibled to extract some relevant information of the data in a way that it would some direction to the next operations for House Rocket.

Also the visualizations will allow the company to keep getting better understandment about their properties and localizations to achieve much more in the future.

