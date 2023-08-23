import os
import re
import networkx as nx
import matplotlib

matplotlib.use(
    "Agg"
)  # Setting the backend to 'Agg' for compatibility with environments lacking a display
import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke

# Directory path for the 'docs' folder
path = "docs"

# Color variables for various elements
NODE_COLOR = "#a877c8"
NODE_BORDER_COLOR = "#723f93"  # Color for node borders
BACKGROUND_COLOR = "white"
EDGE_COLOR = "gray"
FONT_COLOR = "black"
FONT_OUTLINE_COLOR = "white"
TAG_NODE_COLOR = "#67c570"
TAG_BORDER_COLOR = "black"

# Toggles
IS_TRANSPARENT = True
SHOW_FILENAMES = False
SHOW_NODE_BORDER = True
USE_TAGS = True  # Toggle to connect files using tags

# Sizes
node_size_default = 200
NODE_DISTANCE = 5
FONT_SIZE = 8
# Collect all .md files from the 'docs' directory
files = [
    os.path.join(root, filename)
    for root, _, filenames in os.walk(path)
    for filename in filenames
    if filename.endswith(".md")
]

# Extract titles from filenames (excluding the extension)
file_titles = {f: os.path.splitext(os.path.basename(f))[0] for f in files}

# Initialize a graph
G = nx.Graph()

# Add each file as a node to the graph
for title in file_titles.values():
    G.add_node(title)

# Extracting tags from each file and adding as nodes
tags = set()
if USE_TAGS:
    tag_pattern = r"#[\w\d_\-]+"  # Matches words like #tagname

    for file in files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            file_tags = re.findall(tag_pattern, content)
            tags.update(file_tags)

    # Adding each unique tag as a node
    for tag in tags:
        G.add_node(tag)

# Scan each file in the directory for links and tags
for file, title in file_titles.items():
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

        # Connect files based on [[links]]
        for match in re.findall(r"\[\[(.*?)\]\]", content):
            if match in file_titles.values() and title != match:
                G.add_edge(title, match)

        # Connect files to tags if USE_TAGS is True
        if USE_TAGS:
            for tag in tags:
                if tag in content:
                    G.add_edge(title, tag)


# Determine the size of each node based on its degree (number of connections)
node_size = [node_size_default + (v * 10) for v in dict(G.degree()).values()]

# Generate positions for each node

pos = nx.kamada_kawai_layout(G)
#, NODE_DISTANCE)

# Draw the graph
plt.figure(figsize=(12, 12))

if IS_TRANSPARENT:
    plt.gca().set_facecolor("none")
else:
    plt.gca().set_facecolor(BACKGROUND_COLOR)

# Separate the node colors: files vs. tags
node_colors = [TAG_NODE_COLOR if node in tags else NODE_COLOR for node in G.nodes()]
border_colors = [
    TAG_BORDER_COLOR
    if node in tags
    else (NODE_BORDER_COLOR if SHOW_NODE_BORDER else NODE_COLOR)
    for node in G.nodes()
]

nx.draw(
    G,
    pos,
    with_labels=False,
    node_size=node_size,
    node_color=node_colors,
    edge_color=EDGE_COLOR,
    edgecolors=border_colors,
    linewidths=1 if SHOW_NODE_BORDER else 0,
    alpha=0.9,
)

if SHOW_FILENAMES:
    for node, (x, y) in pos.items():
        plt.text(
            x,
            y,
            node,
            color=FONT_COLOR,
            fontsize=FONT_SIZE,
            ha="center",
            va="center",
            path_effects=[withStroke(linewidth=3, foreground=FONT_OUTLINE_COLOR)],
        )

# Check if the 'assets' folder exists in 'docs', if not create it
assets_path = os.path.join(path, "assets")
if not os.path.exists(assets_path):
    os.makedirs(assets_path)

# Save the graph as a PNG file in the 'assets' directory
plt.savefig(
    os.path.join(assets_path, "graph.png"),
    facecolor=("none" if IS_TRANSPARENT else BACKGROUND_COLOR),
    transparent=IS_TRANSPARENT,
)
