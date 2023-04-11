from skmultiflow.meta import AdaptiveRandomForestClassifier
from skmultiflow.trees import ExtremelyFastDecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from entities.study import Study
import numpy as np
import pandas as pd
import pickle
import os

# model= MLPClassifier(n_neighbors= 9, weights= 'distance', metric= 'manhattan')
model= ExtremelyFastDecisionTreeClassifier()

class ClassificationHelper:
    @staticmethod
    def train():
        types= []
        healthy= os.listdir('data/healthy')
        healthy= [os.path.join('data/healthy', file) for file in healthy]
        patients= os.listdir('data/patients')
        patients= [os.path.join('data/patients', file) for file in patients]

        for file in healthy:
            col_health= []
            study= Study(file).df
            for i in range(len(study)):
                col_health.append(1)

            study['healthy']= col_health
            types.append(study)

        for file in patients:            
            col_health= []
            if file.endswith('.xlsx'):
                study= Study(file).df
                for i in range(len(study)):
                    col_health.append(0)

                study['healthy']= col_health
                types.append(study)
                
        types= pd.concat(types)
        x_train, x_test, y_train, y_test= train_test_split(types[['L/R', 'X', 'Y']], types['healthy'], test_size= 0.2, random_state= 42)
        model.fit(x_train.values, y_train.values)
        
        print(f"Treinamento concluído!")
        print(f"Acurácia: {accuracy_score(y_test.values, model.predict(x_test.values))}")

        with open(os.path.join("helpers", 'model_classifier.pkl'), "wb") as f:
            pickle.dump(model, f)
        f.close()

    @staticmethod
    def classify(study):
        with open(os.path.join("helpers", 'model_classifier.pkl') , "rb") as f:
            model = pickle.load(f)
        f.close()

        predict= model.predict(study[['L/R', 'X', 'Y']].values)
        count_healthy= np.count_nonzero(predict)
        count_sick= len(predict) - count_healthy

        print(f"O paciente tem {count_healthy} passos saudáveis e {count_sick} passos não saudáveis.")
        print(f"Resultado da análise: ")
        print(f"O paciente está saudável!\n" if np.mean(predict) > 0.65 and np.std(predict) < 0.2 else f"O paciente está doente!\n")

        return predict