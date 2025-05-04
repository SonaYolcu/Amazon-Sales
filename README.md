# Amazon Sales Data Analysis

![alt text](https://static.seekingalpha.com/uploads/2017/7/11/9642931-1499797608109025_origin.jpg)

## Overview
This project aims to analyze and explore Amazon sales data, focusing on data cleaning, transformation, and visualization to extract meaningful insights. By leveraging various analytical techniques, we can better understand sales trends, customer sentiment, and product performance.

## Libraries Used
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For data visualization.
- **TextBlob**: For sentiment analysis of reviews.

## Data Loading and Exploration
1. **Load Data**: The dataset is imported from a CSV file into a pandas DataFrame for further analysis.
2. **Data Overview**: The structure and data types of the DataFrame are examined using `info()` and `columns` methods.
3. **Missing Values**: Missing values are identified and handled by dropping rows with null values.

## Data Cleaning
- **Data Type Conversion**: Necessary columns, particularly those related to ratings and prices, are converted from object to float to facilitate numerical analysis.
- **String Replacement**: Functions are created to clean up string data in specific columns (e.g., removing commas and currency symbols)..
- **Sentiment Analysis**: A dedicated function is created to analyze the sentiment of reviews using TextBlob, categorizing them into Positive, Negative, or Neutral sentiments for further analysis.

## Data Aggregation
- **Grouping**: The dataset is grouped by product category to calculate mean ratings and discount percentages.
- **Pivot Tables**: A pivot table is generated to summarize the distribution of positive, negative, and neutral reviews by category, enabling quick insights into customer feedback.

## Data Visualization
- **Histograms**: The distribution of actual prices is visualized using histograms, allowing for an understanding of pricing trends across products.
- **Bar Charts**: Bar charts are created to display the top 10 products by category and to compare ratings with the count of positive comments, highlighting key performers.
-**Dual Axis Charts**: A dual-axis bar chart is utilized to visualize the relationship between ratings and discount percentages, providing insights into how discounts may influence customer perceptions.

## Conclusion
This project provides insights into Amazon sales data, highlighting trends in product ratings and customer sentiment. The visualizations help in understanding the relationship between discounts and ratings, as well as the overall customer feedback on products.

## Usage
To run this project, ensure you have the required libraries installed and the dataset available at the specified path. Adjust the file path in the code as necessary.

## License



