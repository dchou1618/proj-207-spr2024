import pandas as pd
import os 
import matplotlib.pyplot as plt
os.chdir("../")


def load_data(fname="data/ETTh1.csv"):
    df = pd.read_csv(fname)
    return df

def plot_col(data, col):
    plt.plot(data[col])
    plt.xlabel("Time")
    plt.ylabel(col)
    plt.title(col)
    plt.show()

if __name__ == "__main__":
    etth1 = load_data(fname="data/ETTh1.csv")
