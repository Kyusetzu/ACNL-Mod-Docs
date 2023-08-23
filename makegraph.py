import os
import re
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Setting the backend to 'Agg' for compatibility with environments lacking a display
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke

# Directory path for the 'docs' folder
path = 'docs'

# Color variables for various elements
NODE_COLOR = "#97c2fc"
NODE_BORDER_COLOR = "#668fc8"
BACKGROUND_COLOR = "#2e303d"  # Only used if IS_TRANSPARENT is False
EDGE_COLOR = "#3d4b65"
FONT_COLOR = "white"
FONT_OUTLINE_COLOR = "#668fc8"

# Toggles 
IS_TRANSPARENT = True  # Set to False if you want to use the BACKGROUND_COLOR
SHOW_FILENAMES = False  # Set to False to hide filenames
SHOW_NODE_BORDER = True  # Set to False to hide node borders


NODE_DISTANCE = 1
FONT_SIZE = 8



# Collect all .md files from the 'docs' directory
files = [os.path.join(root, filename) for root, _, filenames in os.walk(path) for filename in filenames if filename.endswith('.md')]

# Extract titles from filenames (excluding the extension)
file_titles = {f: os.path.splitext(os.path.basename(f))[0] for f in files}

# Initialize a graph
G = nx.Graph()

# Add each file as a node to the graph
for title in file_titles.values():
    G.add_node(title)

# Scan each file in the directory for links in the format [[title]]
for file, title in file_titles.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        for match in re.findall(r'\[\[(.*?)\]\]', content):
            if match in file_titles.values():
                G.add_edge(title, match)

# Default node size
node_size_default = 10

# Determine the size of each node based on its degree (number of connections)
node_size = [node_size_default + (v * 10) for v in dict(G.degree()).values()]

# Generate positions for each node using the spring layout
pos = nx.spring_layout(G, NODE_DISTANCE)  # 'k' is a parameter that controls distance between nodes

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
        edgecolors=NODE_BORDER_COLOR if SHOW_NODE_BORDER else NODE_COLOR,
        linewidths=1 if SHOW_NODE_BORDER else 0,
        alpha=0.9
       )

if SHOW_FILENAMES:
    for node, (x, y) in pos.items():
        plt.text(x, y, node, color=FONT_COLOR, fontsize=FONT_SIZE, ha='center', va='center',
                 path_effects=[withStroke(linewidth=3, foreground=FONT_OUTLINE_COLOR)])

# Check if the 'assets' folder exists in 'docs', if not create it
assets_path = os.path.join(path, 'assets')
if not os.path.exists(assets_path):
    os.makedirs(assets_path)

# Save the graph as a PNG file in the 'assets' directory
plt.savefig(os.path.join(assets_path, 'graph.png'), facecolor=("none" if IS_TRANSPARENT else BACKGROUND_COLOR), transparent=IS_TRANSPARENT)
