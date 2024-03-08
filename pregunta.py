"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip(" ")
    df["barrio"] = df["barrio"].str.lower().str.strip(" ")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int).astype(str)
    df["monto_del_credito"] = df["monto_del_credito"].str.strip(" ").str.strip("$").str.replace(",", "").str.replace(".", "")
    df["línea_credito"] = df["línea_credito"].str.lower().str.strip().str.replace("-", " ").str.replace("_", " ").str.strip(" ")
    
    
    return df

df = clean_data()
print(df.línea_credito.value_counts().to_list())
