import matplotlib.pyplot as pyplot
import json

def barChart(names: list[str], times: list[float]):
    maxIndex = times.index(max(times)) # Encontra o maior tempo
    minIndex = times.index(min(times)) # Encontra o menor tempo

    # Cores personalizadas
    colors = ["#1f77b4"] * len(times) # Cor padrao matplotlib
    colors[maxIndex] = "red" # Para o maior tempo
    colors[minIndex] = "green" # Para o menor tempo

    # Tamanho do gráfico
    fig, axis = pyplot.subplots(figsize=(10, 6))
    axis.set_title("Comparação entre o tempo de consulta em estruturas Python") # Titulo do grafico 
    axis.set_xlabel("Estruturas Python") # label para o eixo X
    axis.set_ylabel("Tempo de consulta (ms)") # label para o eixo y

    axis.bar(names, times, color=colors) # Gera as

    # Seta os valores para as barras
    for index, value in enumerate(times):
        axis.text(index, value, f"{value:.2f}", ha="center", va="bottom", fontsize=8)

    # Rotaciona as labels dos nomes das estruturas
    axis.set_xticklabels(names, rotation=45, ha="right")

    # Traca linhas horizontais 
    axis.grid(axis="y", linestyle="--", alpha=0.4)

    pyplot.tight_layout()
    #pyplot.savefig("BarChartGet.png", dpi=600, bbox_inches="tight")
    pyplot.show()