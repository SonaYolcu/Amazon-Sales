# Amazon Sales Data Analysis

## Overview
This project aims to analyze and explore Amazon sales data, focusing on data cleaning, transformation, and visualization to extract meaningful insights. By leveraging various analytical techniques, we can better understand sales trends, customer sentiment, and product performance.

## Libraries Used
- pandas: Essential for data manipulation and analysis, allowing for efficient handling of large datasets.
- matplotlib: Utilized for creating a variety of data visualizations to represent findings graphically.
- TextBlob: Employed for performing sentiment analysis on customer reviews, categorizing sentiments as Positive, Negative, or Neutral.

## Data Loading and Exploration
1. Load Data: The dataset is imported from a CSV file into a pandas DataFrame for further analysis.
2. Data Overview: The structure and data types of the DataFrame are examined using the
info()
and
columns
methods to ensure proper understanding of the dataset.
3. Missing Values: Missing values are identified and addressed by dropping rows with null values to maintain data integrity.

## Data Cleaning
- Data Type Conversion: Necessary columns, particularly those related to ratings and prices, are converted from object to float to facilitate numerical analysis.
- String Replacement: Custom functions are implemented to clean string data in specific columns, such as removing commas and currency symbols for accurate numerical representation.
- Sentiment Analysis: A dedicated function is created to analyze the sentiment of reviews using TextBlob, categorizing them into Positive, Negative, or Neutral sentiments for further analysis.

## Data Aggregation
- Grouping: The dataset is grouped by product category to calculate mean ratings and discount percentages, providing a clearer view of performance across different categories.
- Pivot Tables: A pivot table is generated to summarize the distribution of positive, negative, and neutral reviews by category, enabling quick insights into customer feedback.

## Data Visualization
- Histograms: The distribution of actual prices is visualized using histograms, allowing for an understanding of pricing trends across products.
- Bar Charts: Bar charts are created to display the top 10 products by category and to compare ratings with the count of positive comments, highlighting key performers.
- Dual Axis Charts: A dual-axis bar chart is utilized to visualize the relationship between ratings and discount percentages, providing insights into how discounts may influence customer perceptions.





