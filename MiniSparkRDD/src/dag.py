# src/dag.py


class DAG:


    def __init__(self):

        self.nodes = []



    def add_node(self,node):

        self.nodes.append(node)



    def get_nodes(self):

        return self.nodes



    def display(self):

        print("\nExecution DAG\n")


        for node in self.nodes:

            print(
                "↓",
                node.operation
            )