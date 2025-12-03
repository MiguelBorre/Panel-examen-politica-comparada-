import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

IMPORT_DIR = "./data"
EXPORT_DIR = "./exports"

PAIS_COLORES = {"USA": "#082f6d", "United Kingdom": "#c8102e", "Switzerland": "#8bb311", "Sweden": "#fecc00", "Spain": "#9672bd", "Portugal": "#006600",
          "Italy": "#d1953e", "Germany": "#000000", "Denmark": "#6dd0f7", "Belgium": "#215f02"}

def pais_y_variable(data, variable, pais):

    data_reduced = data[data["country"] == pais]

    plt.clf()
    ax = plt.figure(figsize=(12, 12))
    sns.lineplot(data=data_reduced, x="year", y=variable, color = PAIS_COLORES[pais])
    if variable == "gov_type":
        plt.yticks([i+1 for i in range(7)], ["Single-party majority government", "Minimal winning coalition", "Surplus coalition", "Single-party minority government",
                    "Multi-party minority government", "Caretaker government", "Technocratic government"])
    elif variable == "fed":
        plt.yticks([i for i in range(3)], ["no", "weak", "strong"])
    elif variable == "prop":
        plt.yticks([i for i in range(3)], ["single-member, simple plurality systems", "modiﬁed proportional representation",
                    "proportional representation"])
    elif variable == "bic":
        plt.yticks([i+1 for i in range(4)], ["unicameralism", "weak bicameralism", 
                    "medium strength bicameralism", "strong bicameralism"])
        
    plt.title(f"{pais} en función de {variable}")
    plt.tight_layout()
    return (ax)

def comparacion_paises(data, variable, pais1, pais2):
    data_reduced1 = data[data["country"] == pais1]

    data_reduced2 = data[data["country"] == pais2]

    plt.clf()
    ax = plt.figure(figsize=(12, 12))
    sns.lineplot(data=data_reduced1, x="year", y=variable, color = PAIS_COLORES[pais1], label = pais1)
    sns.lineplot(data=data_reduced2, x="year", y=variable, color = PAIS_COLORES[pais2], label = pais2)
    if variable == "gov_type":
        plt.yticks([i+1 for i in range(7)], ["Single-party majority government", "Minimal winning coalition", "Surplus coalition", "Single-party minority government",
                    "Multi-party minority government", "Caretaker government", "Technocratic government"])
    elif variable == "fed":
        plt.yticks([i for i in range(3)], ["no", "weak", "strong"])
    elif variable == "prop":
        plt.yticks([i for i in range(3)], ["single-member, simple plurality systems", "modiﬁed proportional representation",
                    "proportional representation"])
    elif variable == "bic":
        plt.yticks([i+1 for i in range(4)], ["unicameralism", "weak bicameralism", 
                    "medium strength bicameralism", "strong bicameralism"])
        
    plt.title(f"{pais1} con {pais2} en función de {variable}")
    plt.legend()
    plt.tight_layout()
    
    return ax

data = pd.read_excel(f"{IMPORT_DIR}/cpds-1960-2023-update-2025.xlsx")

st.title("Panel para ver los datos para el examen de Alba")

variable_a_estudiar = st.selectbox("Elige la variable para estudiar", ["gov_type", "rae_leg", "effpar_leg", "instcons", "fed", "prop", "bic", "womenpar"])
pais1 = st.selectbox("Selecciona el 1 país a estudiar", ["USA", "United Kingdom", "Switzerland", "Sweden", "Spain", "Portugal",
          "Italy", "Germany", "Denmark", "Belgium"])
pais2 = st.selectbox("Selecciona el 2 país a estudiar", ["USA", "United Kingdom", "Switzerland", "Sweden", "Spain", "Portugal",
          "Italy", "Germany", "Denmark", "Belgium"])

if pais1 == pais2:
    grafico = pais_y_variable(data, variable_a_estudiar, pais1)
    st.pyplot(grafico)
else:
    grafico = comparacion_paises(data, variable_a_estudiar, pais1, pais2)
    st.pyplot(grafico)