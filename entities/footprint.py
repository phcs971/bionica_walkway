import pandas as pd
from entities.position import Position

class Footprint:
    def __init__(self, dataframe):
        self.id = dataframe['Obj'][0]
        self.left = dataframe['L/R'][0] == 0
        self.df = dataframe[['Time', 'X', 'Y']]
        self._get_positions()

    def _get_positions(self):
        self.heel = Position(self.df.values[0])
        self.support = Position(self.df.values[1])
        self.positions = [Position(p) for p in self.df.values[2:]]

    def plot(self, plt, color=None, label=None):
        x = [p.x for p in self.positions]
        y = [p.y for p in self.positions]
        if label is not None:
            plt.plot(x, y, c=color, label=label)
        else:
            plt.plot(x, y, c=color)
        plt.scatter(self.heel.x, self.heel.y, c=color)
        plt.scatter(self.support.x, self.support.y, c=color)