import numpy as np
import pandas as pd

iris = pd.read_csv('/home/nurlan/Desktop/Artificial Neural Network(ANN)/iris_num .data')


iris.sample(frac = 1).reset_index(drop = False)


#This function helps me to shuffle my data in ordet to get rid of overfitting 
def Shuffle(data):
    data = data.sample(frac = 1).reset_index(drop = True)
    
