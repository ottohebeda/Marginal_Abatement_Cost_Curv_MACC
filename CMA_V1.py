# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 20:46:56 2025

@author: ottoh
"""
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
dfcma = pd.read_excel('C:/Users/CMA_MIT1.xlsx')

# Ordenar os dados pelo custo da medida
dfcma = dfcma.sort_values('custo da medida')
dfcma['quantidade abatida acumulada'] = dfcma['quantidade abatida'].cumsum()

# Criar os eixos X e Y
x = [0] + list(dfcma['quantidade abatida acumulada'])
y = [dfcma['custo da medida'].iloc[0]] + list(dfcma['custo da medida'])

plt.figure(figsize=(12, 6))

# Criar a escada colorida
for i in range(len(dfcma)):
    x_start = x[i]
    x_end = x[i + 1]
    y_value = y[i + 1]

    color = "#7EC8E3" if y_value <= 100 else "#F4A261"  # Azul claro ou laranja claro
    plt.fill_between([x_start, x_end], [y_value, y_value], step="pre", color=color, alpha=0.7)

# Plotar a curva CMA em linha preta
plt.step(x, y, where='pre', color='black', linewidth=1.5, label="CMA")

# Adicionar linha de referência em 100 $/tCO2e
plt.axhline(y=100, color='red', linestyle='--', linewidth=1.5, label="Limite de 100 $/tCO2e")

# Adicionar rótulos das medidas no gráfico
for i in range(len(dfcma)):
    x_middle = (x[i] + x[i + 1]) / 2
    plt.annotate(dfcma['nome da medida'].iloc[i], 
                 (x_middle, y[i + 1]),
                 xytext=(0, -17),
                 textcoords='offset points',
                 ha='center', va='center', fontsize=9)

# Configuração dos eixos e legenda
plt.xlabel("Abatimento (MtCO2e)", fontsize=12, fontfamily='Calibri')
plt.ylabel("CMA ($/tCO2e)", fontsize=12, fontfamily='Calibri')
plt.title("Curva de Custo Marginal de Abatimento", fontsize=14, fontweight='bold', fontfamily='Calibri')

# Criar legendas personalizadas
import matplotlib.patches as mpatches
legend_patches = [
    mpatches.Patch(color="#7EC8E3", label="Medidas abaixo de 100 $/tCO2e"),
    mpatches.Patch(color="#F4A261", label="Medidas acima de 100 $/tCO2e"),
    mpatches.Patch(color="red", label="Limite de 100 $/tCO2e", linestyle="--")
]

plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), fontsize=9, frameon=True)

# Salvar o gráfico
plt.savefig("CMA_MIT1_colorido.png", dpi=300, bbox_inches='tight')

plt.show()


