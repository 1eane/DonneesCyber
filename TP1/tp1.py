import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy as np
import hashlib

colors = ["red", "blue", "yellow"]

"""
    generate_random_3_colorable_graph

    Description:
        This function generates a random 3-colorable graph with a specified number of nodes. A 3-colorable graph is one in which no two adjacent nodes share the same color. The function returns the node colors and the corresponding adjacency matrix.

    Parameters:
        - num_nodes (int): The number of nodes in the graph.

    Returns:
        - node_colors (list): A list representing the colors assigned to each node in the graph.
        - matrice_adj (numpy.ndarray): A 2D NumPy array (adjacency matrix) indicating the connections between nodes. An entry matrice_adj[i][j] is set to 1 if nodes i and j are connected, and 0 otherwise.

"""


def generate_random_3_colorable_graph(num_nodes):
    node_colors = [random.choice(colors) for _ in range(num_nodes)]

    matrice_adj = np.zeros((num_nodes, num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and node_colors[i] != node_colors[j]:
                rand = random.random()
                if rand <= 0.5:
                    matrice_adj[i][j] = 1
                    matrice_adj[j][i] = 1

    return node_colors, matrice_adj


def permuted_colors(node_colors):
    # Permuter les indices des couleurs de manière aléatoire
    random_indices = list(range(len(colors)))
    random.shuffle(random_indices)

    # Créer un dictionnaire de correspondance des couleurs
    color_mapping = dict(zip(colors, [colors[i] for i in random_indices]))

    # Transformer les couleurs dans node_colors de manière aléatoire
    transformed_colors = [color_mapping[color] for color in node_colors]

    return transformed_colors


"""
permuted_colors

Parameters:
    - node_colors (list): A list of node colors to be permuted.

Returns:
    - transformed_colors (list): A new list of colors obtained by randomly permuting the indices of the input node_colors.
"""


def dessiner_graphe(node_colors, matrice_adj):
    G = nx.Graph()

    # Ajoutez les nœuds avec leurs couleurs
    for node, color in enumerate(node_colors):
        G.add_node(node, color=color)

    for i in range(len(node_colors)):
        for j in range(i + 1, len(node_colors)):
            if matrice_adj[i][j]:
                G.add_edge(i, j)

    pos = nx.circular_layout(G)

    nx.draw(G, pos, node_color=node_colors, with_labels=True)

    plt.show()


"""
hash_node

Parameters:
    - node_color (str): The color of the node to be hashed.
    - random_value (bytes): Random bytes to introduce variability in the hash.

Returns:
    - hash_hexdigest (str): The hexadecimal representation of the SHA-1 hash generated using the input node_color and random_value.
"""


def hash_node(node_color, random_value):
    hash = hashlib.sha1()

    hash.update(node_color.encode('utf-8'))
    hash.update(random_value)
    hash.digest()

    return hash.hexdigest()


"""
mise_en_gage_coloriage

Parameters:
    - node_colors (list): A list of node colors.
    - random_values (list): A list of random values associated with each node color.

Returns:
    - hashed_values (list): A list of SHA-1 hash values obtained by hashing each node color with its corresponding random value.
"""


def mise_en_gage_coloriage(node_colors, random_values):
    hashed_values = []

    for i in range(len(node_colors)):
        hashed_value = hash_node(node_colors[i], random_values[i])
        hashed_values.append(hashed_value)

    return hashed_values


"""
proof_color

Parameters:
    - node_colors (list): A list of node colors.
    - random_values (list): A list of random values associated with each node color.
    - mise_en_gage (list): A list of SHA-1 hash values obtained by hashing node colors with corresponding random values.
    - i (int): Index of the first node.
    - j (int): Index of the second node.

Returns:
    - is_valid_proof (bool): True if the proof is valid, False otherwise.
"""


def proof_color(node_colors, random_values, mise_en_gage, i, j):
    ri_ci = mise_en_gage[i]
    rj_cj = mise_en_gage[j]

    color_i = node_colors[i]
    color_j = node_colors[j]

    hash_ri_ci = hash_node(color_i, random_values[i])
    hash_rj_cj = hash_node(color_j, random_values[j])

    return hash_ri_ci == ri_ci and hash_rj_cj == rj_cj and color_i != color_j


"""
select_two_nodes

Parameters:
    - matrice_adj (numpy.ndarray): A 2D NumPy array representing the adjacency matrix of a graph.
    - num_nodes (int): The number of nodes in the graph.

Returns:
    - node_indices (tuple): A tuple containing two randomly selected node indices that share an edge in the graph.
"""


def select_two_nodes(matrice_adj, num_nodes):
    edge_found = False
    while not edge_found:
        i, j = np.random.choice(num_nodes, 2, replace=False)
        if matrice_adj[i][j] == 1 or matrice_adj[j][i] == 1:
            edge_found = True

    return i, j


"""
main

Parameters:
    - num_nodes (int): The number of nodes in the 3-colorable graph.

Returns:
    - is_valid_simulation (bool): True if the simulation successfully validates color proofs for all node pairs, False otherwise.
"""


def main(num_nodes):
    # Generate a random 3-colorable graph
    node_colors, matrice_adj = generate_random_3_colorable_graph(num_nodes)

    successful_tests = 0
    for _ in range(num_nodes*num_nodes):
        shuffle_colors = permuted_colors(node_colors)

        random_values = [str(random.getrandbits(128)).encode('utf-8')
                         for _ in range(num_nodes)]

        mise_en_gage = mise_en_gage_coloriage(shuffle_colors, random_values)
        i, j = select_two_nodes(matrice_adj, num_nodes)

        if proof_color(shuffle_colors, random_values, mise_en_gage, i, j):
            successful_tests += 1

    return successful_tests == num_nodes*num_nodes


# try protocole
print('Le graph est-il valide ? ', main(6))
