# importamos las librerías que necesitamos

# Tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np
import re

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest

# Fase 1: Exploración y Limpieza

def minus_guion_bajo(df):
    """
    Función para reemplazar los espacios en las columnas por guiones bajos
    y convertirlas a minúsculas.

    Parámetros:
    df (DataFrame): DF cuyas columnas se desean modificar.

    Devuelve:
    DataFrame: DF con los nombres de las columnas modificados.
    """
    # Convertir nombres de columnas a minúsculas y reemplazar espacios por guiones bajos
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df
