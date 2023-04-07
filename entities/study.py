import pandas as pd
from entities.footprint import Footprint

class Study:
    def __init__(self, filename):
        self.filename = filename
        self._read_data()
        self._split_info()
        self._get_footprints()

    def _read_data(self):
        df = pd.read_excel(self.filename).dropna()
        self.df = df[df['Obj'] < 100]

    def _split_info(self):
        data = self.filename.split('/')[-1].split('.')[0].split('-')
        self.subject = ''.join([c for c in data[0] if c.isnumeric()])
        
        self.type = data[1]
        if len(data) > 2:
            self.session = data[2]
        else:
            self.session = 1

    def _get_footprints(self):
        self.footprints = []
        for foot in self.df['Obj'].unique():
            positions = self.df[self.df['Obj'] == foot].reset_index(drop=True)
            self.footprints.append(Footprint(positions))
    
    def plot(self, plt, color=None):
        for foot in self.footprints:
            if foot == self.footprints[0] and color is not None:
                label = str(self)
            else :
                label = None
            foot.plot(plt, color=color, label=label)
            

    def __str__(self):
        return f'Paciente {self.subject} - {_types[self.type]} - Sessão {self.session}'
    

_types = {
    "1": "Andando", 
    "2": "Andando devagar",
    "3": "Andando rápido",
    "4": "Andando + Atv. Cognitiva",
    "5": "Andando + Atv. Motora",
    "8": "Andar | Parar | Andar",
}