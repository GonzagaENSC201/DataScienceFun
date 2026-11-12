# EDA: exploratory data analysis
# getting familiar with your data

# example of EDA: data visualization
# goals of data viz
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

import numpy as np
import matplotlib.pyplot as plt

def plot_data(x, y):
    # let's have one figure with 2 charts in a row
    fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 12" width x 4" height

    # chart 1: basic
    ax = axes[0]
    ax.plot(x, y, label="Random data in [1, 101)",
            color="red", lw=5)
    ax.set_title("Chart 1")
    ax.set_xlabel("X Units")
    ax.set_ylabel("Y Units")
    ax.legend()
    ax.grid()

    # chart 2: reference line and point of interest
    ax = axes[1]
    ax.plot(x, y)
    ax.axhline(y.mean(), label="Y Mean", ls=":", color="green")
    ax.plot(x[3], y[4], marker="X", ms=10, label="Point of Interest")
    ax.legend()


    # after add all chart components good to call:
    fig.tight_layout()

def main():
    # 1st demo: using the pyplot interface (simplest)
    # we need data
    x = np.arange(10) # 0 1 2 3... 9
    y = np.random.randint(1, 101, len(x)) # [1, 101)
    print(x)
    print(y)
    # plt.plot(x, y)
    # plt.show() # launches an interactive window

    # 2nd demo: using "object oriented" interface (more control)
    plot_data(x, y)
    plt.savefig("demo_s1.png")

main()