import sys
sys.path.append('..')
from EDA import electricity
import numpy as np
from filterpy.kalman import KalmanFilter


def filter_model(train_data):
    kf = KalmanFilter(dim_x=1, dim_z=1)
    kf.x = np.array([train_data[0]])
    kf.F = np.array([[1.]])
    kf.H = np.array([[1.]])
    kf.P *= 1000
    kf.R = 5
    for i in range(1, len(train_data)):
        kf.predict()
        kf.update(train_data[i])
    return kf



if __name__ == '__main__':
    data = electricity.load_data(fname="data/ETTh1.csv")["OT"]
    data = (data-data.mean())/data.std() 
    train_cutoff = int(len(data)*0.8)
    train_data = data[:train_cutoff].array.reshape(-1,1)
    test_data = data[train_cutoff:].array.reshape(-1,1)x

    filtermodel1 = filter_model(train_data)
    print(train_data)
    print(filtermodel1.predict(test_data[:24]))


