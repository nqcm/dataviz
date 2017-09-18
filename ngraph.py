from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

from nparse import parse

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")

    # make a new variable  'counter' from iterating through each line of
    #data in the parsed data, and count how many incidents happen on
    #each day of week
    counter = Counter(item["DayOfWeek"] for item in data_file)
    data_list = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot from day_list
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph!
    plt.savefig("Days.png")
    plt.clf()

def visualize_type():
    """Visualize data by category"""
    data_file = parse(MY_FILE, ",")
    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Type.png".  This is our graph!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()
