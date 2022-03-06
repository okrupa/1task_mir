import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV


def loadData(file_name):
    return pd.read_csv("../data/processed/" + file_name)

train_data = loadData("train.csv")
test_data = loadData("test.csv")

target = "time"
features = train_data.columns.tolist()
features.remove(target)

train_data_X = train_data[features]
train_data_Y = train_data[target]




random_grid = {
    "n_estimators": [int(x) for x in np.linspace(start = 200, stop = 2000, num = 100)],
    "max_features": ['auto', 'sqrt'],
    "max_depth": [int(x) for x in np.linspace(1, 100, num = 50)],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "bootstrap": [True, False]
}

randomForest = RandomForestRegressor()
randomForest_Randomizer = RandomizedSearchCV(estimator = randomForest, param_distributions = random_grid, n_iter = 1000, cv = 3, verbose = 2, random_state = 42, n_jobs = -1)


randomForest_Randomizer.fit(train_data_X, train_data_Y)

print("Best Params:")
print(randomForest_Randomizer.best_params_)
print("Best Score:")
print(randomForest_Randomizer.best_score_)