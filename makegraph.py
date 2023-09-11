import os
import re
import networkx as nx
import matplotlib

# Setting the backend to 'Agg' for compatibility with environments lacking a display
matplotlib.use("Agg")
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
SHOW_FILENAMES = True
SHOW_NODE_BORDER = True
USE_TAGS = True  # Toggle to connect files using tags

# Sizes
NODE_SIZE_DEFAULT = 200
NODE_DISTANCE = 5
FONT_SIZE = 8

def get_files_from_directory(directory_path, file_extension=".md"):
    """
    Retrieve all files with a specified extension from a directory.
    
    Parameters:
    - directory_path (str): The path to the directory.
    - file_extension (str): The file extension to filter by (default is ".md").
    
    Returns:
    - list: A list of file paths.
    """
    return [
        os.path.join(root, filename)
        for root, _, filenames in os.walk(directory_path)
        for filename in filenames
        if filename.endswith(file_extension)
    ]


def extract_file_titles(files):
    """
    Extract titles from filenames (excluding the extension).
    
    Parameters:
    - files (list): A list of file paths.
    
    Returns:
    - dict: A dictionary mapping file paths to titles.
    """
    return {f: os.path.splitext(os.path.basename(f))[0] for f in files}


def extract_tags_from_files(files, pattern):
    """
    Extract tags from each file based on a regex pattern.
    
    Parameters:
    - files (list): A list of file paths.
    - pattern (str): The regex pattern to match tags.
    
    Returns:
    - set: A set of unique tags.
    """
    tags = set()
    for file in files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            file_tags = re.findall(pattern, content)
            tags.update(file_tags)
    return tags


def create_graph_from_files_and_tags(files, file_titles, tags):
    """
    Create a graph from files and tags. Files and tags are nodes, and links between them are edges.
    
    Parameters:
    - files (list): A list of file paths.
    - file_titles (dict): A dictionary mapping file paths to titles.
    - tags (set): A set of unique tags.
    
    Returns:
    - NetworkX Graph: A graph object.
    """
    G = nx.Graph()
    
    # Add each file as a node to the graph
    for title in file_titles.values():
        G.add_node(title)
    
    # Add each unique tag as a node
    for tag in tags:
        G.add_node(tag)
    
    # Scan each file for links and tags to add edges
    for file, title in file_titles.items():
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
            # Connect files based on [[links]]
            for match in re.findall(r"\[\[(.*?)\]\]", content):
                if match in file_titles.values() and title != match:
                    G.add_edge(title, match)
            
            # Connect files to tags
            for tag in tags:
                if tag in content:
                    G.add_edge(title, tag)
                    
    return G


def plot_graph(G, tags):
    """
    Plot the graph using matplotlib.
    
    Parameters:
    - G (NetworkX Graph): The graph object.
    - tags (set): A set of unique tags.
    """
    node_size = [NODE_SIZE_DEFAULT + (v * 10) for v in dict(G.degree()).values()]
    pos = nx.kamada_kawai_layout(G)
    
    plt.figure(figsize=(12, 12))
    
    if IS_TRANSPARENT:
        plt.gca().set_facecolor("none")
    else:
        plt.gca().set_facecolor(BACKGROUND_COLOR)

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

    assets_path = os.path.join(path, "assets")
    if not os.path.exists(assets_path):
        os.makedirs(assets_path)

    plt.savefig(
        os.path.join(assets_path, "graph.png"),
        facecolor=("none" if IS_TRANSPARENT else BACKGROUND_COLOR),
        transparent=IS_TRANSPARENT,
    )


# Constants
NODE_SIZE_DEFAULT = 200

# Retrieve files and titles
files = get_files_from_directory(path)
file_titles = extract_file_titles(files)

# Extract tags
tag_pattern = r"#[\w\d_\-]+"  # Can be optimized further if needed
tags = extract_tags_from_files(files, tag_pattern)

# Create graph and plot it
G = create_graph_from_files_and_tags(files, file_titles, tags)
plot_graph(G, tags)

