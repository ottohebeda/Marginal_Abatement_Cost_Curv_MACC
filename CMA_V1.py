# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:46:56 2025

@author: ottoh
"""
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

# Carregar os dados
dfcma = pd.read_excel('C:/Users/ottoh/OneDrive/Doutorado/Tese/Resultados/Imagine/MIT1/CMA_MIT1 - Copia.xlsx')

# Resetar o índice para usar como referência
dfcma = dfcma.sort_values('custo da medida').reset_index(drop=True)
dfcma['quantidade abatida acumulada'] = dfcma['quantidade abatida'].cumsum()

# Eixos X e Y
x = [0] + list(dfcma['quantidade abatida acumulada'])
y = [dfcma['custo da medida'].iloc[0]] + list(dfcma['custo da medida'])

# Cores por setor
setores = dfcma['setor'].unique()
cores = plt.cm.tab20.colors
mapa_cores = {setor: cores[i % len(cores)] for i, setor in enumerate(setores)}

# Iniciar figura
fig, ax = plt.subplots(figsize=(14, 6))

# Barras coloridas por setor
for i in range(len(dfcma)):
    x_start = x[i]
    x_end = x[i + 1]
    y_value = y[i + 1]
    setor = dfcma['setor'].iloc[i]
    color = mapa_cores[setor]
    ax.fill_between([x_start, x_end], [y_value, y_value], step="pre", color=color, alpha=0.8)

# Linhas horizontais
ax.axhline(y=0, color='black', linewidth=1.2)
ax.axhline(y=100, color='red', linestyle='--', linewidth=1.5)

# Linha CMA
ax.step(x, y, where='pre', color='black', linewidth=1.5)

# Anotar índice no meio de cada barra
for i in range(len(dfcma)):
    x_middle = (x[i] + x[i + 1]) / 2
    ax.annotate(str(i),
                (x_middle, y[i + 1]),
                xytext=(0, -17),
                textcoords='offset points',
                ha='center', va='center', fontsize=9)
# Ajustar os limites do eixo X para começar junto ao eixo Y
ax.set_xlim(0, x[-1])

# Eixos e título
ax.set_xlabel("Abatimento (MtCO2e)", fontsize=12, fontfamily='Calibri')
ax.set_ylabel("CMA ($/tCO2e)", fontsize=12, fontfamily='Calibri')
ax.set_title("Curva de Custo Marginal de Abatimento", fontsize=14, fontweight='bold', fontfamily='Calibri')

# Legenda por setor
legend_setores = [mpatches.Patch(color=mapa_cores[setor], label=setor) for setor in setores]
legend_setores.append(mpatches.Patch(color="red", label="Limite de 100 $/tCO2e", linestyle="--"))
ax.legend(handles=legend_setores, loc='upper left', bbox_to_anchor=(1.01, 1), fontsize=9)


# Adicionar texto ao lado do gráfico (ajuste y e x conforme necessário)
# fig.text(1.02, 0.5, legenda_texto, va='center', ha='left', fontsize=9, fontfamily='Calibri')

# Salvar
plt.savefig("CMA_MIT1_setores_legenda_indices.png", dpi=300, bbox_inches='tight')

plt.show()

