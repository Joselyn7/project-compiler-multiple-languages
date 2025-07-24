from graphviz import Digraph

def draw_tree(tree, filename='static/syntax_tree'):
    dot = Digraph(comment='Syntax Tree')

    def add_nodes(node, parent_id=None):
        node_id = str(id(node))
        label = str(node[0]) if isinstance(node, tuple) else str(node)
        dot.node(node_id, label)

        if parent_id:
            dot.edge(parent_id, node_id)

        if isinstance(node, tuple):
            for child in node[1:]:
                if isinstance(child, (tuple, list)):
                    add_nodes(child, node_id)
                else:
                    leaf_id = str(id(child)) + str(hash(child))
                    dot.node(leaf_id, str(child))
                    dot.edge(node_id, leaf_id)

    add_nodes(tree)
    dot.render(filename, format='png', cleanup=True)
