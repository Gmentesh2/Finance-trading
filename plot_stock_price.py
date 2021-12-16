import pandas as pd

import matplotlib.pyplot as plt

#
def main():
    """Apple's stock open graph 1 years statistics"""
    df = pd.read_csv("data/AAPL.csv")
    df["Adj Close"].plot()
    plt.savefig("graphs/aapl.png")


if __name__=="__main__":
    main()

def main():
    """Facebook's stock open graph 1 years statistics"""
    df = pd.read_csv("data/FB.csv")
    df["Adj Close"].plot()
    plt.savefig("graphs/FB.png")

if __name__=="__main__":
    main()

def main():
    """Walt disney's stock open graph 1 years statistics"""
    df = pd.read_csv("data/DIS.csv")
    df["Open"].plot()
    plt.savefig("graphs/waltdisnay.png")
if __name__=="__main__":
    main()

def main():
    """Walmart's stock open graph 1 years statistics"""
    df = pd.read_csv("data/WMT.csv")
    df["Open"].plot()
    plt.savefig("graphs/walmart.png")
if __name__=="__main__":
    main()


