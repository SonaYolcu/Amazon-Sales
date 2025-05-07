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
- **Histograms**: The distribution of actual prices is visualized using histograms, allowing for an understanding of pri
  ![Снимок экрана (20)](https://github.com/user-attachments/assets/4c52e83a-2d2b-49fa-b4ef-2642c909c1c4)
cing trends across products.
 
- **Bar Charts**: Bar charts are created to display the top 10 products by category and to compare ratings with the count of positive comments, highlighting key performers.
 ![Снимок экрана (21)](https://github.com/user-attachments/assets/9faeffc9-f37b-47bf-a518-eee332ba5aba)

-**Dual Axis Charts**: A dual-axis bar chart is utilized to visualize the relationship between ratings and discount percentages, providing insights into how discounts may influence customer perceptions.
![Снимок экрана (22)](https://github.com/user-attachments/assets/746c8f06-3a6e-4e32-bdda-eda7cad9bbf2)

![Снимок экрана (23)](https://github.com/user-attachments/assets/7058217b-1574-485b-81d9-6c21ad65e36a)

## Summary
Our insightful exploration of the Amazon Sales dataset, characterized by its remarkable cleanliness and consistency, yielded a treasure trove of findings. Through a series of targeted inquiries, we unlocked detailed answers:
- There is an inverse proportionality between the discount on the product price and the rating. means that as the product rating increases, the discount on it decreases, and vice versa. That is, the higher the product rating, the lower the discount, and the lower the rating, the greater the discount. This may indicate that higher-quality or popular products have lower discounts because they are already selling well, while less popular products may be offered at significant discounts to attract customers.
- Products with the highest review counts within their categories might be considered potential top sellers, even without direct sales data.
- The average discount percentage vary across categories: Average discount percentages vary widely across categories, ranging from 0% to 78.39%.
- Categories "Computers&Accessories" and  "Electronics" stand out with notably higher average discounts (90.09% and 56.34%), suggesting potential factors like clearance efforts, high competition, or lower-profit margins.
- Smart Watches and Charging Cables are the most popular product categories.
- If we look at the number of positive reviews, categories "Computers&Accessories|USBCables", "Electronics|SmartWatches" and "Electronics|SmartTelevisions" are in the top three.

## Conclusion

This project provides insights into Amazon sales data, highlighting trends in product ratings and customer sentiment. The visualizations help in understanding the relationship between discounts and ratings, as well as the overall customer feedback on products.The Amazon Sales dataset is a valuable resource for businesses and researchers alike.

## Usage
To run this project, ensure you have the required libraries installed and the dataset available at the specified path. Adjust the file path in the code as necessary.

## License
[License](https://github.com/SonaYolcu/Amazon-Sales/blob/main/LICENSE.txt)



