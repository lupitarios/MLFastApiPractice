#step 3: building a model using scikit-learn
from sklearn.tree import DecisionTreeRegressor

from org.mgrm.practice.firssteps.kagglelearn.introml.selection_data_modeling import X, y

print("\n\n*** Building a Model using scikit-learn ***\n")

melbourne_model = DecisionTreeRegressor(random_state=1)  # Define the model. What type of model would it be?
# ensures you get the same results in each run.
# The model is a Decision Tree Regressor, which is suitable for regression tasks.
melbourne_model_fitted = melbourne_model.fit(X, y)  # Fit the model to the data. Capture patterns from provided data. This is the heart of modeling.
print("\n*** melbourne_model_fitted\n", melbourne_model_fitted)
print("\nMaking predictions for the following 5 houses:\n", X.head())
print("\nThe predictions are:\n")

melbourne_model_predicted = melbourne_model_fitted.predict(X.head())
print(melbourne_model_predicted)  # Predict the price of the first 5 houses in the dataset.
# The predict method uses the fitted model to make predictions based on the features in X.
# The output will be the predicted prices for these houses.