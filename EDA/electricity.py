import pandas as pd
import os 
import matplotlib.pyplot as plt
os.chdir("../")


def load_data():
    ett = pd.read_csv("data/ETTh1.csv")
    weather = pd.read_csv("data/WTH.csv")
    return ett, weather

def plot_col(data, col):
    plt.plot(data[col])
    plt.xlabel("Time")
    plt.ylabel(col)
    plt.title(col)
    plt.show()

if __name__ == "__main__":
    ett, weather = load_data()
    plot_col(ett, "OT")
    plot_col(weather, "WetBulbCelsius")
