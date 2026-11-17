# EDA: exploratory data analysis
# getting familiar with your data

# we are going to learn how to visualize data w/matplotlib
# 3 goals of data visualization
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

import numpy as np
import matplotlib.pyplot as plt

def plot_data(x, y):
    # let's have 2 charts in one "figure"
    # the 2 charts will be side by side in one row
    fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 12" width x 4" height
    # tuesday 11/17 warm-up task #1
    fig.suptitle("Subplots Demo", fontsize=15, fontweight="bold")

    # chart 1: basic
    ax = axes[0]
    ax.plot(x, y, label="Random data in [1, 101)",
            color="red", lw=5)
    ax.set_title("Chart 1")
    ax.set_xlabel("X Units")
    ax.set_ylabel("Y Units")
    ax.legend()
    ax.grid()

    # chart 2: point of interest and adding a reference line
    ax = axes[1]
    ax.plot(x, y)
    ax.plot([x[4]], y[4], label="Point of Interest", marker="X", ms=10)
    # tuesday 11/17 warm-up task #2
    ax.annotate("Point of Interest #2", xy=(x[7], y[7]), 
                xytext=(x[7], y[7] + 20), arrowprops={"facecolor": "black"})
    ax.axhline(y.mean(), color="cyan", lw=5, ls="--", label="Y Mean")
    ax.legend()



    fig.tight_layout() # good to call last, after adding all figure components

def main():
    # we need some data!
    x = np.arange(10) # 0 1 2 ... 9
    y = np.random.randint(1, 101, len(x)) # random ints in [1, 101)
    print(x)
    print(y)

    # 1st demo: using the pyplot interface (simplest)
    # plt.plot(x, y)
    # plt.show() # shows an interactive window

    # 2nd demo: using the "object oriented" interface (more control)
    plot_data(x, y)
    plt.savefig("demo_s2.png") # instead of showing window, let's save figure to a file

main()