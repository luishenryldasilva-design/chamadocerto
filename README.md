# ChamadoCerto 🎯

Sistema de **triagem de chamados de suporte de TI**: classifica categoria e prioridade, define o prazo de SLA e mostra indicadores em um painel.

## O problema
Em equipes pequenas de TI, chamados chegam sem padrão e a prioridade costuma ser definida "no olho". Isso gera retrabalho, usuários insatisfeitos e decisões sem dados.

## A solução
- Classificação automática de **categoria** (Acesso, Hardware, Rede, Software, Outros) por palavras-chave.
- Definição de **prioridade** (Baixa, Média, Alta, Crítica) e **prazo de SLA** em horas.
- **Painel** com total de chamados, chamados críticos e gráficos por categoria e prioridade.
- Campo para **testar um novo chamado** e ver a classificação na hora.

## Tecnologias
Python · Pandas · Streamlit · Git/GitHub

## Como rodar
```bash
git clone https://github.com/luishenryldasilva-design/chamadocerto.git
cd chamadocerto
pip install -r requirements.txt
streamlit run app.py
```

## Estrutura
