from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import pickle



def main():
    model = LogisticRegression(max_iter=500)
    X,y = load_iris(return_X_y=True,as_frame=True)
    model.fit(X,y)
    filename = 'model.pkl'
    pickle.dump(model, open(filename, 'wb'))
    X = [[1, 1, 1, 1]]
    y_pred = model.predict(X)
    print(y_pred)

if __name__ == "__main__":
    main()