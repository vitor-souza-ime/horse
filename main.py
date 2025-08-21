import matplotlib.pyplot as plt
import numpy as np

# Matriz do tour do cavalo
tour = np.array([
 [ 0, 59, 38, 33, 30, 17,  8, 63],
 [37, 34, 31, 60,  9, 62, 29, 16],
 [58,  1, 36, 39, 32, 27, 18,  7],
 [35, 48, 41, 26, 61, 10, 15, 28],
 [42, 57,  2, 49, 40, 23,  6, 19],
 [47, 50, 45, 54, 25, 20, 11, 14],
 [56, 43, 52,  3, 22, 13, 24,  5],
 [51, 46, 55, 44, 53,  4, 21, 12]
])

# ✅ Imprimir matriz no console (como antes)
print("Tour do Cavalo (matriz):")
print(tour)

# ----------------------------
# Gráfico do tabuleiro
fig, ax = plt.subplots(figsize=(10, 10))  # tamanho do gráfico
n = tour.shape[0]

# Criar tabuleiro xadrez
colors = ["#f0d9b5", "#b58863"]  # tons de xadrez
for i in range(n):
    for j in range(n):
        color = colors[(i + j) % 2]
        ax.add_patch(plt.Rectangle((j, n-1-i), 1, 1, facecolor=color))

# Adicionar números do tour
for i in range(n):
    for j in range(n):
        if tour[i, j] == 0:  # início
            ax.text(j + 0.5, n-1-i + 0.5, str(tour[i, j]),
                    ha='center', va='center', fontsize=14, color='green', fontweight='bold')
        elif tour[i, j] == n*n-1:  # fim
            ax.text(j + 0.5, n-1-i + 0.5, str(tour[i, j]),
                    ha='center', va='center', fontsize=14, color='red', fontweight='bold')
        else:
            ax.text(j + 0.5, n-1-i + 0.5, str(tour[i, j]),
                    ha='center', va='center', fontsize=12, color='black')

# Desenhar caminho do cavalo
for i in range(n):
    for j in range(n):
        neighbors = np.argwhere(tour == tour[i, j] + 1)
        if neighbors.size != 0:
            ni, nj = neighbors[0]
            ax.plot([j + 0.5, nj + 0.5], [n-1-i + 0.5, n-1-ni + 0.5], 'b-', linewidth=1)

# Ajustes finais
ax.set_xlim(0, n)
ax.set_ylim(0, n)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title("Tour do Cavalo 8x8", fontsize=16)
plt.show()
