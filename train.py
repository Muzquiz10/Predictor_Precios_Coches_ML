import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle


#-- Cargo datos --#

df = pd.read_csv('data/processed/coches_segunda_mano_ML.csv')

#-- Separato en features y target --#

X = df.drop(['Precio'],axis=1)
y = df['Precio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

#-- Le paso los mejores parámetros que he obtenivo con el Grid Search --#

gbrt_grid = GradientBoostingRegressor(max_depth=4,
                                 n_estimators=200, 
                                 learning_rate=0.2,
                                 random_state=42,
                                 min_samples_split=2)

#-- Entreno el modelo --#
                                
gbrt_grid.fit(X_train, y_train)

#--Guardo el modelo--#

with open('modelos/final/new_model','wb') as archivo_salida:
    pickle.dump(gbrt_grid,archivo_salida)