import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: movies with titles and overviews
data = pd.DataFrame({
    'title': [
        "Toy Story", 
        "Jumanji", 
        "Grumpier Old Men", 
        "Waiting to Exhale", 
        "Father of the Bride Part II"
    ],
    'overview': [
        "A story of a boy and his toys that come to life.",
        "A magical board game that brings adventure and danger.",
        "Two aging men navigate the complications of love and friendship.",
        "A group of women bond as they face personal struggles.",
        "Family chaos ensues during a wedding."
    ]
})

# Fill any missing values in 'overview'
data['overview'] = data['overview'].fillna("")

# Step 1: Vectorize the overviews using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['overview'])

# Step 2: Compute cosine similarity between movies
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 3: Create a reverse map: movie title -> DataFrame index
indices = pd.Series(data.index, index=data['title']).drop_duplicates()

# Function that takes in a movie title and returns similar movies
def get_recommendations(title, cosine_sim=cosine_sim, top_n=3):
    # Find the index for the movie that matches the title
    idx = indices[title]
    
    # Get pairwise similarity scores for that movie with all others
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort the movies based on the similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices for the top_n most similar movies (skip the first as it is the same movie)
    sim_scores = sim_scores[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the top_n most similar movies
    return data['title'].iloc[movie_indices]

# Example usage:
print("Movies similar to 'Toy Story':")
print(get_recommendations("Toy Story"))
