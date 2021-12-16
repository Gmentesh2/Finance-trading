from os import name
import pandas as pd

import matplotlib.pyplot as plt


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
    print(df["Open"])
    df["Open"].plot()
    plt.savefig("graphs/walmart.png")
if __name__=="__main__":
    main()
    
def main():
    """Shows apple's graph with high&low stock values in 1 years statistics """
    df = pd.read_csv('data/AAPL.csv')
    print(df)
    df[["High","Low"]].plot()
    plt.savefig("graphs/apple")
if __name__=="__main__":
    main()


def main():
    """Shows apple's graph with open&close stock values in 1 years statistics"""
    df = pd.read_csv("data/AAPL.csv")
    print(df)
    df[["Open","Close"]].plot()
    plt.savefig("graphs/apple2")

if __name__=="__main__":
    main()
       
    


