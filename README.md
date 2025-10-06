# CODTECH INTERNSHIP

*COMPANY*: CODTECH IT SOLUTIONS  
*NAME*: [Kajal Balu Bad]  
*INTERN ID*: [CT06DY2158]  
*DOMAIN*: [Python Programming]  
*DURATION*: 6 Weeks  
*MENTOR*: [Neela Santosh Kumar]  

---

## TASK 1 - API INTEGRATION AND DATA VISUALIZATION  

*Description*:  
During this task, I worked on integrating a public API with Python to fetch live data and then visualize it. The objective of the task was to understand how APIs provide real-time data from different sources and how this data can be converted into useful insights using Python libraries.  

I started by exploring different public APIs such as weather APIs, COVID-19 statistics APIs, and financial market APIs. Once I selected an API, I used the requests library in Python to send HTTP requests and fetch JSON-formatted responses. Understanding the JSON structure was a key step because it required parsing nested objects and extracting only the relevant information for visualization.  

After fetching the data, I processed it using the pandas library. With pandas, I converted the JSON data into a DataFrame which made it easier to analyze, clean, and filter. This step also included handling missing values, converting data types, and renaming columns for better readability.  

The visualization part was implemented using matplotlib and seaborn. I created bar charts, line graphs, and pie charts depending on the nature of the dataset. For example, if I fetched weather data, I visualized temperature trends over a week. If I fetched COVID-19 data, I plotted graphs comparing daily cases and recoveries.  

This task also introduced me to challenges like rate-limiting, where APIs restrict the number of requests in a certain period. To handle this, I added error handling and request delays. Another challenge was authentication since some APIs required API keys. I learned how to securely use API keys without exposing them in the code.  

Overall, this task gave me practical experience in real-world API usage and taught me how to transform raw JSON data into meaningful graphs. These skills are highly useful in fields like data analysis, business intelligence, and machine learning projects.  

---

## Features
- Weather data API integration
- Data visualization using Python
- Data cleaning and preprocessing
- Error handling for API requests
- Support for multiple public APIs

## How to Run
1. Make sure Python 3.x is installed on your system.
2. Install the required libraries:
   
   pip install requests pandas matplotlib seaborn
   
3. Run the script:
   
   python weather_data.py
   
4. View the output graphs and results in your terminal or as saved files.
## Output


