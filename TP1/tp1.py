import networkx as nx
import random

def generate_random_3_colorable_graph(num_nodes, num_edges):
    # Créer un graphe vide
    G = nx.Graph()

    # Ajouter des nœuds au graphe
    G.add_nodes_from(range(num_nodes))

    # Créer une liste de couleurs (3 couleurs différentes)
    colors = ['red', 'green', 'blue']

    # Créer des arêtes aléatoires tout en maintenant la 3-colorabilité
    while G.number_of_edges() < num_edges:
        # Sélectionner deux nœuds au hasard
        node1 = random.choice(list(G.nodes()))
        node2 = random.choice(list(G.nodes()))

        # S'assurer que les nœuds sélectionnés sont de couleurs différentes
        color1 = G.nodes[node1].get('color', None)
        color2 = G.nodes[node2].get('color', None)

        if color1 != color2:
            # Ajouter une arête entre les deux nœuds
            G.add_edge(node1, node2)
        else:
            # Si les nœuds sont de la même couleur, changez la couleur d'un nœud
            new_color = random.choice([c for c in colors if c != color1])
            G.nodes[node1]['color'] = new_color

    return G

# Exemple d'utilisation : Générer un graphe avec 10 nœuds et 15 arêtes
graph = generate_random_3_colorable_graph(10, 15)

# Afficher les nœuds et les arêtes du graphe
print("Nœuds du graphe:", graph.nodes())
print("Arêtes du graphe:", graph.edges())

# Afficher les couleurs des nœuds
for node, color in nx.get_node_attributes(graph, 'color').items():
    print(f"Nœud {node}: {color}")