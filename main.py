import pandas as pd
from entities.study import Study
from helpers.plot_helper import PlotHelper
from helpers.classification_helper import ClassificationHelper

def main():
    studies = [
        Study('data/healthy/lga1-1-1.xlsx'), 
        Study('data/patients/lga30-1-1.xlsx'),
        Study('data/patients/lga31-1-1.xlsx'),
        Study('data/patients/lga32-1-1.xlsx'),
        Study('data/healthy/lga2-1-1.xlsx'),
        Study('data/patients/lga33-1-1.xlsx'),
        Study('data/patients/lga34-1-1.xlsx'),
        Study('data/healthy/lga3-1-1.xlsx'),
        Study('data/patients/lga35-1-1.xlsx')
    ]

    PlotHelper.plot_studies(studies, use_subplots=False)
    
    for i in range(len(studies)):
        print("--------------------------------------------------")
        print(f"Classificando estudo {i+1} de {len(studies)}")
        print(f"Nome do arquivo: {studies[i].filename}\n")
        ClassificationHelper.classify(studies[i].df)

if __name__ == '__main__':
    main()