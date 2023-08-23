import os
import re
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Setzen des Backends auf 'Agg'
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke

# Pfad zum Ordner 'docs'
path = 'docs'

# Farbvariablen
NODE_COLOR = "#FFAA00"
BACKGROUND_COLOR = "#323232"  # Wird nur verwendet, wenn IS_TRANSPARENT False ist
EDGE_COLOR = "white"
FONT_COLOR = "black"
FONT_OUTLINE_COLOR = "white"

# Toggle für transparenten Hintergrund
IS_TRANSPARENT = True  # Setzen Sie dies auf False, um den Hintergrundfarbenwert zu verwenden

# Pfad zum Ordner 'docs'
path = 'docs'

# Alle .md Dateien sammeln
files = []
for root, dirs, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.md'):
            files.append(os.path.join(root, filename))

# Dateititel aus Dateinamen extrahieren (ohne Erweiterung)
file_titles = {f: os.path.splitext(os.path.basename(f))[0] for f in files}

# Graph erstellen
G = nx.Graph()

# Jede Datei zum Graphen als Knoten hinzufügen
for title in file_titles.values():
    G.add_node(title)

# Jede Datei im Verzeichnis durchsuchen
for file, title in file_titles.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Für jede Verknüpfung im Format [[titel]] in der Datei
        for match in re.findall(r'\[\[(.*?)\]\]', content):
            # Wenn der gefundene Titel in der Liste der Dateititel ist
            if match in file_titles.values():
                # Füge Kanten zum Graphen hinzu
                G.add_edge(title, match)

# Die Knotengröße festlegen
node_size_default = 350  # Dies ist die Standardgröße für alle Knoten

# Die Knotengröße basierend auf deren Grad (Anzahl der Verbindungen) festlegen
node_size = [node_size_default + (v * 100) for v in dict(G.degree()).values()]


# Positionen für alle Knoten erzeugen
pos = nx.spring_layout(G, k=1)  # k ist ein Parameter, den Sie anpassen können, um die Knoten näher oder weiter voneinander entfernt anzuordnen

# Graph zeichnen
plt.figure(figsize=(12, 12))

if IS_TRANSPARENT:
    plt.gca().set_facecolor("none")
else:
    plt.gca().set_facecolor(BACKGROUND_COLOR)

nx.draw(G, pos,
        with_labels=False,
        node_size=node_size,
        node_color=NODE_COLOR,
        edge_color=EDGE_COLOR,
        edgecolors="black",
        linewidths=1,
        alpha=0.9
       )

# Fügen Sie die Titel separat mit einer Umrandung hinzu
for node, (x, y) in pos.items():
    plt.text(x, y, node, color=FONT_COLOR, fontsize=10, ha='center', va='center',
             path_effects=[withStroke(linewidth=3, foreground=FONT_OUTLINE_COLOR)])

# Überprüfen Sie, ob der 'assets' Ordner in 'docs' existiert, andernfalls erstellen Sie ihn
assets_path = os.path.join(path, 'assets')
if not os.path.exists(assets_path):
    os.makedirs(assets_path)

# Save the file
plt.savefig(os.path.join(path, 'assets', 'graph.png'), facecolor=("none" if IS_TRANSPARENT else BACKGROUND_COLOR), transparent=IS_TRANSPARENT)
