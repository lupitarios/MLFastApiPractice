#step 6. The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree.
#It generally has much better predictive accuracy than a single decision tree, and it works well with default parameters.

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from org.mgrm.practice.firssteps.kagglelearn.introml.model_validation_sklearn import trainX, trainY, valX, valY

print("\n\n*** Random Forest Model ***\n")

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(trainX, trainY)
melb_preds = forest_model.predict(valX)
print("\nMAE for Random Forest Model:", mean_absolute_error(valY, melb_preds))