from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle

#--- FUNCION ELIMINAR COLUMNAS QUE NO VAMOS A USAR ---#

def drop_colum(x):
    x.drop(['url','company','price_financed','is_professional','dealer','version','country','publish_date','insert_date'],axis=1,inplace=True)


#--- FUNCION LIMPIEZA Y FEATURE ENGINEERING ---#
def limpieza(x):
    
    fuel = []
    
    for i in x['fuel']:
        if i =='Gas natural (CNG)':
            i = 4
            fuel.append(i)
        elif i == 'Gasolina':
            i = 4
            fuel.append(i)
        elif i == 'Híbrido enchufable':
            i = 6
            fuel.append(i)
        elif i == 'Eléctrico' or i == 'Híbrido':
            i = 5
            fuel.append(i)
        elif i == "Diésel":
            i = 3
            fuel.append(i)
        elif i == 'Gas':
            i =2
            fuel.append(i)
        else:
            i = 1
            fuel.append(i)

    shift = []
    for i in x['shift']:
        if i == 'Manual':
            i = 2 
            shift.append(i)
        elif i == 'Automático':
            i = 3 
            shift.append(i)
        else:
            i = 1
            shift.append(i)



    colores = []
    for i in x['color']:
        if i == 'Plata':
            i = 1
            colores.append(i)
            
        elif i == 'Negro':
            i = 2
            colores.append(i)

        elif i == 'Blanco':
            i = 3
            colores.append(i)

        else:
            i = 4
            colores.append(i)
    
    
    marca = []
    for i in x['make']:
        if i == "BENTLEY" or i == "FERRARI" or i =="LAMBORGHINI":
            i = 5
            marca.append(i)
        elif i =="ASTON MARTIN" or i =="ALPINE" or i =="PORSCHE" or i=="MASERATI" or i=="TESLA":
            i = 4
            marca.append(i)
        elif i == "CORVETTE" or i=="CUPRA" or i=="LAND-ROVER" or i=="HUMMER" or i=="LOTUS" or i== "ISUZU" or i=="MORGAN" or i=="JAGUAR" or i=="MERCEDES-BENZ":
            i = 3
            marca.append(i)

        elif i == "DS" or i=="LEXUS" or i=="JEEP" or i=="DFSK" or i=="VOLVO" or i=="BMW" or i=="AUDI" or i=="SUBARU" or i=="INFINIT" or i=="MAXUS" or i=="ABARTH":
            i = 2
            marca.append(i)
        else:
            i=1
            marca.append(i)

    puertas = []
    
    for i in x['doors']:
        if i == 4 or i == 5:
            i = 2
            puertas.append(i)
        elif  i == 2:
            i = 3
            puertas.append(i)
        else:
            i = 1
            puertas.append(i)


    le = LabelEncoder()
    le.fit(x['province'])
    x['province'] = le.transform(x['province'])

    le = LabelEncoder()
    le.fit(x['model'])
    x['model'] = le.transform(x['model'])
    
    x['make'] = marca
    x['shift'] = shift
    x['color'] = colores
    x['fuel'] = fuel
    x['doors'] = puertas

    x['model'].fillna('León',inplace=True)
    x['make'].fillna('CITROEN',inplace=True)
    x['fuel'].fillna('Gasolina',inplace=True) 
    x['year'].fillna(2019,inplace=True)
    x = x.dropna(inplace=True)  


## FUNCION DE ML GUIDE ##
def data_report(df):

    cols = pd.DataFrame(df.columns.values, columns=["COL_N"])

    types = pd.DataFrame(df.dtypes.values, columns=["DATA_TYPE"])

    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    percent_missing_df = pd.DataFrame(percent_missing.values, columns=["MISSINGS (%)"])

    unicos = pd.DataFrame(df.nunique().values, columns=["UNIQUE_VALUES"])
    
    percent_cardin = round(unicos['UNIQUE_VALUES']*100/len(df), 2)
    percent_cardin_df = pd.DataFrame(percent_cardin.values, columns=["CARDIN (%)"])

    concatenado = pd.concat([cols, types, percent_missing_df, unicos, percent_cardin_df], axis=1, sort=False)
    concatenado.set_index('COL_N', drop=True, inplace=True)


    return concatenado.T


##Función para interfaz grafica##



def predecir(x):
    with open('model/my_model', 'rb') as archivo_entrada:
        model_1 = pickle.load(archivo_entrada)
    model_1
    prediction = model_1.predict(x)
    return str(prediction[0].round(2)) + ' €'



