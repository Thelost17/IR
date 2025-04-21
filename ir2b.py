#AIM : IMPLEMENT VECTOR SPACE MODEL

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
from numpy.linalg import norm

# Training and test documents
train_set = ["The sky is blue.", "The sun is bright."]
test_set = ["The sun in the sky is bright."]

# Initialize vectorizer (with stopwords) and transformer
vectorizer = CountVectorizer(stop_words="english")
transformer = TfidfTransformer()

# Generate TF-IDF features
train_vectors = transformer.fit_transform(vectorizer.fit_transform(train_set)).toarray()
test_vectors = transformer.transform(vectorizer.transform(test_set)).toarray()

# Display TF-IDF features
print("Training Set TF-IDF:", train_vectors)
print("Test Set TF-IDF:", test_vectors)

# Function to compute cosine similarity
def cosine_similarity(vec1, vec2):
    return round(np.dot(vec1, vec2) / (norm(vec1) * norm(vec2)), 3)

# Compute cosine similarity between training and test vectors
for train_vec in train_vectors:
    for test_vec in test_vectors:
        print("Cosine Similarity:", cosine_similarity(train_vec, test_vec))
