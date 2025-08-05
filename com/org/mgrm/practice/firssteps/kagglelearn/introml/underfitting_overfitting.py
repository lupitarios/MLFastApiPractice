#step5 Underfitting and Overfitting. accuracy on new data
'''
overfitting, where a model matches the training data almost perfectly, but does poorly in validation and other new data.
underfitting, When a model fails to capture important distinctions and patterns in the data, so it performs poorly even in training data
'''

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

from org.mgrm.practice.firssteps.kagglelearn.introml.model_validation_sklearn import trainX, valX, trainY, valY

print("\n\n*** Underfitting and Overfitting ***\n")

def get_mae(max_leaf_nodes, trainX, valX, trainY, valY):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(trainX, trainY)
    predictions = model.predict(valX)
    mae = mean_absolute_error(valY, predictions)
    return mae

#We can use a for-loop to compare the accuracy of models built with different values for max_leaf_nodes.
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, trainX, valX, trainY, valY)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" % (max_leaf_nodes, my_mae))
    #print("Max leaf nodes: %d \t\t Mean Absolute Error: %.2f" % (max_leaf_nodes, my_mae))


#for could be like this:
'''
score = {my_mae : get_mae(max_leaf_nodes, trainX, valX, trainY, valY) for max_leaf_nodes in [5, 50, 500, 5000]}
# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = min(score, key=score.get)

'''
#****
#We use validation data, which isn't used in model training, to measure a candidate model's accuracy.
# This lets us try many candidate models and keep the best one.

''' Exercices :: 
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
#wrong
score = {mae: get_mae(max_leaf_nodes, train_X,val_X, train_y, val_y) for max_leaf_nodes in candidate_max_leaf_nodes}
#right 
score = {max_leaf_nodes: get_mae(max_leaf_nodes, train_X,val_X, train_y, val_y) for max_leaf_nodes in candidate_max_leaf_nodes}
best_tree_size = min(score, key = score.get)
print (score)


# **Step 2: Fit Model Using All Data
# You know the best tree size. If you were going to deploy this model in practice, you would make it even more accurate
# by using all of the data and keeping that tree size. That is, you don't need to hold out the validation data now that
#  you've made all your modeling decisions.
# Fill in argument to make optimal size and uncomment
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)

# fit the final model and uncomment the next two lines
final_model.fit(X, y)

'''