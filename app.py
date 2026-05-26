import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('data/fashion_products.csv')

# Create user-item matrix
user_item_matrix = df.pivot_table(
    index='User ID',
    columns='Product ID',
    values='Rating'
)

# Fill missing values
user_item_matrix_filled = user_item_matrix.fillna(0)

# Compute similarity
user_similarity = cosine_similarity(user_item_matrix_filled)

user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix_filled.index,
    columns=user_item_matrix_filled.index
)

# Recommendation function
def recommend_products(user_id, num_recommendations=5):

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)

    similar_users = similar_users.drop(user_id)

    most_similar_user = similar_users.index[0]

    products_rated_by_similar_user = user_item_matrix_filled.loc[most_similar_user]

    products_not_rated_by_user = user_item_matrix_filled.loc[user_id] == 0

    recommended_products = products_rated_by_similar_user[products_not_rated_by_user]

    recommended_products = recommended_products.sort_values(ascending=False)

    recommended_product_ids = recommended_products.head(num_recommendations).index

    recommended_product_details = df[df['Product ID'].isin(recommended_product_ids)][
        ['Product Name', 'Brand', 'Category', 'Price', 'Rating']
    ]

    return recommended_product_details

# Streamlit UI
st.title("Fashion Recommendation System")

st.write("This application recommends fashion products using collaborative filtering.")

user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    max_value=100,
    value=1
)

if st.button("Get Recommendations"):

    recommendations = recommend_products(user_id)

    st.subheader("Recommended Products")

    st.dataframe(recommendations)
    