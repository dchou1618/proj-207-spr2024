import sys
sys.path.append('..')
from EDA import electricity
import numpy as np


class LSTM:
    def __init__(self, data, n_steps, n_features):
        self.data = data
        self.n_steps = n_steps
        self.n_features = n_features

    def prepare_data(self):
        X, y = list(), list()
        for i in range(len(self.data)):
            end_ix = i + self.n_steps
            if end_ix > len(self.data) - 1:
                break
            seq_x, seq_y = self.data[i:end_ix], self.data[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def lstm_model(self):
        from keras.models import Sequential
        from keras.layers import LSTM, Dense
        X, y = self.prepare_data()
        X = X.reshape((X.shape[0], X.shape[1], self.n_features))
        model = Sequential()
        model.add(LSTM(50, activation='relu', return_sequences=True, input_shape=(self.n_steps, self.n_features)))
        model.add(LSTM(50, activation='relu'))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        model.fit(X, y, epochs=200, verbose=1)
        return model
    
    def predict(self, model, data):
        X, y = self.prepare_data()
        X = X.reshape((X.shape[0], X.shape[1], self.n_features))
        return model.predict(X, verbose=0)
    
    def evaluate(self, model, data):
        X, y = self.prepare_data()
        X = X.reshape((X.shape[0], X.shape[1], self.n_features))
        return model.evaluate(X, y, verbose=0)
    


if __name__ == '__main__':
    data = electricity.load_data(fname="data/ETTh1.csv")["OT"]