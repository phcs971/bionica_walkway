import pandas as pd
from entities.study import Study
from helpers.plot_helper import PlotHelper
from helpers.classification_helper import ClassificationHelper

def main():
    studies = [
        Study('data/healthy/lga1-1-1.xlsx'), 
        Study('data/patients/lga30-1-1.xlsx'),
        Study('data/healthy/lga2-1-1.xlsx'),
    ]
    PlotHelper.plot_studies(studies, use_subplots=False)
    # ClassificationHelper.train()

if __name__ == '__main__':
    main()

