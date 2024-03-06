import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Load dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Use SVD algorithm
model = SVD()

# Evaluate model
cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
