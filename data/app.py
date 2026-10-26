import pandas as pd
import streamlit as st

from triagem import triar

st.title("ChamadoCerto 🎯")
st.caption("Triagem inteligente de chamados de suporte de TI")

df = pd.read_csv("data/chamados.csv")
resultado = df["descricao"].apply(triar).apply(pd.Series)
df = pd.concat([df, resultado], axis=1)

col1, col2 = st.columns(2)
col1.metric("Total de chamados", len(df))
col2.metric("Chamados críticos", int((df["prioridade"] == "Crítica").sum()))

st.subheader("Chamados por categoria")
st.bar_chart(df["categoria"].value_counts())

st.subheader("Chamados por prioridade")
st.bar_chart(df["prioridade"].value_counts())

st.subheader("Todos os chamados")
st.dataframe(df)

st.subheader("Teste um novo chamado")
texto = st.text_input("Descreva o problema")
if texto:
    r = triar(texto)
    st.write(f"**Categoria:** {r['categoria']}")
    st.write(f"**Prioridade:** {r['prioridade']}")
    st.write(f"**Prazo (SLA):** {r['sla_horas']} horas")
