# ♞ Horse Tour - Problema do Cavalo no Xadrez

Este projeto implementa e visualiza uma solução para o **Problema do Tour do Cavalo** no tabuleiro de xadrez 8x8, utilizando **Python** e **Matplotlib**.  

O **Tour do Cavalo** consiste em mover um cavalo por todas as casas de um tabuleiro de xadrez exatamente uma vez, formando um ciclo ou caminho fechado/aberto.  

<p align="center">
  <img src="https://raw.githubusercontent.com/vitor-souza-ime/horse/main/demo.png" alt="Exemplo do Tour do Cavalo" width="500"/>
</p>

---

## 🚀 Execução

Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/horse.git
cd horse
````

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python main.py
```

---

## 📂 Estrutura do Projeto

```
horse/
│── main.py          # Código principal que gera a visualização
│── requirements.txt # Dependências do projeto
│── README.md        # Este arquivo
│── demo.png         # Exemplo da saída (opcional para visualização no GitHub)
```

---

## 🖼️ Saída

O programa gera uma visualização gráfica de um tabuleiro de xadrez 8x8:

* As casas do tabuleiro são coloridas em padrão clássico.
* Cada número representa a ordem da visita do cavalo.
* O ponto de partida (0) é destacado em **verde**.
* O ponto final (63) é destacado em **vermelho**.
* O caminho do cavalo é desenhado em azul.

---

## 📦 Dependências

* [Python 3.8+](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [NumPy](https://numpy.org/)

Para instalar manualmente:

```bash
pip install matplotlib numpy
```

---

## 📖 Referências

* [Problema do Cavalo - Wikipedia](https://pt.wikipedia.org/wiki/Problema_do_cavalo)
* [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
* [NumPy Documentation](https://numpy.org/doc/)

---

## 👨‍💻 Autor

* **Vitor Amadeu Souza**

  * [GitHub](https://github.com/vitor-souza-ime)

