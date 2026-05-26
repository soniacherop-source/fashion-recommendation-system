# Fashion Recommendation System

## Project Overview

This project develops a Fashion Recommendation System using collaborative filtering techniques to recommend fashion products based on user preferences and rating behavior. The system analyzes similarities between users and generates personalized product recommendations.

The project also includes a popularity-based recommendation fallback strategy to improve recommendation robustness for users with limited interaction history.

Additionally, a Streamlit web application is developed to provide an interactive interface for generating recommendations dynamically.

---

## Business Problem

Online fashion platforms often struggle to provide personalized shopping experiences due to the large number of available products. Customers may find it difficult to discover products that match their preferences.

This project addresses this problem by building a recommendation system that suggests fashion products based on similarities in user behavior and ratings.

---

## Objectives

- Understand user-product interaction behavior
- Build a collaborative filtering recommendation model
- Generate personalized product recommendations
- Improve recommendation quality using fallback recommendations
- Visualize recommendation performance and user similarities
- Develop an interactive Streamlit application

---

## Dataset Features

The dataset contains:

- User ID
- Product ID
- Product Name
- Brand
- Category
- Price
- Rating
- Color
- Size

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook

---

## Project Structure

```bash
fashion-recommendation-system/
│
├── data/
│   └── fashion_products.csv
│
├── notebooks/
│   └── notebooks folder
│
├── 01_business_and_data_understanding.ipynb
├── 02_data_preprocessing_and_modeling.ipynb
├── app.py
├── README.md
└── .gitignore
```

---

## Methodology

### 1. Business and Data Understanding
- Understanding the recommendation problem
- Exploring dataset structure and features

### 2. Data Preprocessing
- Encoding categorical variables
- Handling missing values
- Creating the user-item interaction matrix

### 3. Collaborative Filtering
- Computing cosine similarity between users
- Identifying similar users
- Generating personalized recommendations

### 4. Recommendation Improvement
- Implementing popularity-based fallback recommendations

### 5. Evaluation and Visualization
- User similarity heatmaps
- Recommended product rating visualizations

### 6. Streamlit Application
- Interactive recommendation interface
- Dynamic recommendation generation

---

## Sample Recommendation Output

| Product Name | Brand | Category | Rating |
|---|---|---|---|
| Jeans | H&M | Men's Fashion | 4.73 |
| T-shirt | Zara | Kids' Fashion | 4.45 |
| Shoes | Gucci | Kids' Fashion | 3.99 |

---

## Streamlit Application
A Streamlit web application was developed to demonstrate the recommendation system interactively.

Features:
- User-based recommendation generation
- Product recommendation display
- Simple and user-friendly interface
Run the application using:

```bash
streamlit run app.py
```

---

## Key Insights

- Users with similar rating patterns tend to prefer similar products
- Collaborative filtering can effectively personalize recommendations
- Popularity-based recommendations improve robustness for sparse user interactions

---

## Tableau Dashboard

An interactive Tableau dashboard was created to visualize:
- Fashion product category distribution
- Average product ratings across brands
- Product rating distributions

The dashboard provides insights into user preferences and product trends within the recommendation system.

## Tableau Public Dashboard

[View Interactive Dashboard]
https://public.tableau.com/views/FashionRecommendationSystemAnalysis/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Author

Sonia Cherop