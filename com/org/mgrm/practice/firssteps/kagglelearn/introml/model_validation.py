# step 4 : Model Validation using Mean Absolute Error (also called MAE)
#use model validation to measure the quality of your model
''' With the MAE metric, we take the absolute value of each error.
This converts each error to a positive number. We then take the average of those absolute errors.
This is our measure of model quality. In plain English, it can be said as
    On average, our predictions are off by about X. '''

from sklearn.metrics import mean_absolute_error

from org.mgrm.practice.firssteps.kagglelearn.introml.build_model import melbourne_model_fitted
from org.mgrm.practice.firssteps.kagglelearn.introml.selection_data_modeling import y, X

print("\n\n*** Model Validation using Mean Absolute Error (also called MAE) ***\n")

melbourne_model_predicted = melbourne_model_fitted.predict(X)
loss_result = mean_absolute_error(y, melbourne_model_predicted)
print("\nMean Absolute Error (MAE):", loss_result)
