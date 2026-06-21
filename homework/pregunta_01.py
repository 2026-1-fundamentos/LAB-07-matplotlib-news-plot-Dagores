"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # Read data
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Ensure output directory exists
    out_dir = os.path.join("files", "plots")
    os.makedirs(out_dir, exist_ok=True)

    # Create plot
    plt.figure(figsize=(8, 5))
    for col in df.columns:
        plt.plot(df.index.astype(int), df[col], marker="o", label=col)

    plt.title("News consumption by medium")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    # Save plot
    out_path = os.path.join(out_dir, "news.png")
    plt.savefig(out_path)
    plt.close()
