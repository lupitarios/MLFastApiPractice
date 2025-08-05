#step 4 : Model Validation using sklearn split and train_test_split

from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from org.mgrm.practice.firssteps.kagglelearn.introml.selection_data_modeling import X, y

# split data into training and validation data, for both features and target variable
# The split is based on a random number generator. Supplying a numeric value to the random_state argument
# ensures you get the same results in each run.
print("\n\n*** Model Validation using sklearn split and train_test_split ***\n")

trainX, valX, trainY, valY = train_test_split(X, y, random_state=0)
#define model
melbourne_model = DecisionTreeRegressor(random_state=1)
# fit model to training data
melbourne_model.fit(trainX, trainY)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(valX)
print("\n MAE \n", mean_absolute_error(valY, val_predictions))