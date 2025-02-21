# EXPLORATORY DATA ANALYSIS - ONLINE SHOPPING IN RETAIL 


## Table of Contents
1. [Project Description](#project-description)
2. [Installation Instructions](#installation-instructions)
3. [Usage Instructions](#usage-instructions)
4. [File Structure](#file-structure)
5. [License](#license)

## Project Description

This project analyzes customer activity data from an online retail store. 

The goal is to explore user behavior, gain insights usind data analysis techniques and understad key metrics.

### What I Learned:

1. **GitHub Workflow:**
   - **Version Control**: Through Git and GitHub, I learned to manage version control for my code, which allows me to maintain a clear history of changes made to the project.
   - **Committing and Pushing**: I practiced making changes to my local code, creating commits with descriptive messages, and pushing those changes to a remote GitHub repository. This helps to keep a detailed log of all progress and facilitates collaboration in projects.
   - **Branching and Merging**: I used branches to experiment with new ideas without affecting the main code, and then merged those changes efficiently into the main branch.
   - **Collaboration**: I learned to collaborate with others on GitHub via Pull Requests (PRs), which helps review code and integrate new features into the project.

2. **Handling Missing Values:**
   - **Identifying Missing Data**: I learned to identify missing or null values in the data using methods like `isnull()` or `isna()` in Pandas, which gives me an overview of the data’s quality.
   - **Removing Missing Data**: I understood when it’s appropriate to remove rows with missing values. This is useful when the missing data represents a small proportion and won’t significantly affect the analysis. I used `dropna()` to remove rows or columns with missing data.
   - **Imputing Missing Data**: In situations where removing data isn't ideal, I learned to impute the missing values with the mean, median, or a constant value using `fillna()` in Pandas. This is essential to avoid losing valuable information in large datasets.
   - **Imputation with Advanced Techniques**: For categorical columns, I learned to impute missing values with the most frequent value in the column or using more complex predictive models like KNN (K-Nearest Neighbors) imputation.

3. **Transforming Skewed Data:**
   - **Understanding Data Skewness**: I learned to identify skewness in the data using the skewness coefficient (`skew()`) and how skewness affects statistical models.
   - **Transformations**: To reduce skewness in data distributions, I applied logarithmic transformations (`log1p()`) and square root transformations (`sqrt()`). These transformations help make the data approach a normal distribution and improve the accuracy of predictive models.

4. **Outlier Removal:**
   - **Identifying Outliers**: I learned to identify outliers in the data using statistical methods like calculating the Z-score. Values with a Z-score greater than 3 or less than -3 are considered outliers.
   - **Removing Outliers**: I used filtering techniques to remove outliers that could distort the analysis results. I also understood that, in some cases, outliers may be valuable and should not be removed without proper justification.

5. **Removing Highly Correlated Columns:**
   - **Correlation Matrix**: I learned to calculate and visualize the correlation matrix to detect highly correlated columns. This is crucial to avoid multicollinearity in predictive models.
   - **Threshold for Correlation**: I defined a threshold (e.g., 0.9) to remove columns that have a high correlation. This helps reduce noise in the data and improves the interpretability of the model.
   - **Handling Multicollinearity**: By removing highly correlated columns, I improved the quality of the dataset for modeling and avoided issues like overfitting.

6. **Data Visualization:**
   - **Exploratory Data Analysis (EDA)**: I practiced performing exploratory data analysis to gain an overall understanding of the dataset. This includes visualizing distributions, identifying outliers, and analyzing correlations.
   - **Visualizing Skewed Data**: I used plots such as histograms with KDE (Kernel Density Estimation) to visualize the distribution of data before and after transformations, allowing me to compare the effects of the transformations.
   - **Heatmaps for Correlation**: I learned to use heatmaps to visualize the correlation matrix, making it easier to detect highly correlated columns that might need to be removed.

7. **Data Cleaning and Preprocessing:**
   - **Preprocessing for Modeling**: I understood that cleaning and transforming the data properly is a crucial step before applying any predictive models. Ensuring the data is well-distributed, free from outliers, and without multicollinearity significantly improves model accuracy.
   - **Feature Engineering**: I performed an analysis to create new features from existing ones, which can improve the performance of machine learning models.

By learning these techniques and tools, I have enhanced my ability to prepare and clean data, which is essential for conducting accurate analyses and developing robust machine learning models.





## Installation Instructions
To get started with this project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```

2. Navigate to the project folder:
    ```bash
    cd your-repository-name
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage Instructions
To run the project, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the Python script:
    ```bash
    python your_script_name.py
    ```

3. Ensure that the data file (data_without_null_values.csv) is available in the correct directory.


### File structure of the project

├── data_without_null_values.csv         # The cleaned dataset
├── your_script_name.py                  # Python script with EDA code
├── requirements.txt                     # List of dependencies
├── README.md                            # Project documentation
└── other_files_and_folders              # Any additional files

## License information
This project is licensed under the MIT License - see the LICENSE file for details.
