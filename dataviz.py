import streamlit as st
import pandas as pd
import plotly.express as px

# Titre de l'application
st.title("Analyse des données des étudiants")

# Chargement des données
def load_data():
    # Chargez votre DataFrame à partir d'un fichier CSV
    df = pd.read_csv("student_spending.csv")
    return df

# Chargement des données
df = load_data()

# Afficher le DataFrame
st.subheader("Aperçu des données:")
st.write(df)

# Visualisation des données
st.subheader("Visualisation des données:")

# Histogramme du revenu mensuel
st.subheader("Histogramme du revenu mensuel")
fig_income = px.histogram(df, x="monthly_income")
st.plotly_chart(fig_income)

# Diagramme en entonnoir des méthodes de paiement préférées
st.subheader("Diagramme en entonnoir des méthodes de paiement préférées")
fig_payment = px.funnel(df, x='preferred_payment_method')
st.plotly_chart(fig_payment)

# Nuage de points du revenu mensuel par sexe
st.subheader("Nuage de points du revenu mensuel par sexe")
fig_scatter = px.scatter(df, x="gender", y="monthly_income", color="gender",
                         hover_data=["age", "major"], title="Revenu mensuel par sexe")
st.plotly_chart(fig_scatter)

import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données
def load_data():
    # Charger le DataFrame à partir du fichier CSV
    df = pd.read_csv("student_spending.csv")
    return df

# Chargement des données
df = load_data()

# Titre de l'application
st.title("Analyse des dépenses des étudiants")

# 1. Afficher les données des étudiants
if st.checkbox("Afficher les données des étudiants"):
    st.subheader("Données des étudiants:")
    st.write(df)

# 2. Visualisation : Diagramme à barres des dépenses par catégorie
st.subheader("Diagramme à barres des dépenses par catégorie")
fig_expenses = px.bar(df.drop(columns=["total", "total_spend", "total_income", "money_saved"]).sum(), 
                       title="Dépenses par catégorie")
st.plotly_chart(fig_expenses)

