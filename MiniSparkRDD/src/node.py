# src/node.py


class Node:


    def __init__(
        self,
        operation,
        function=None,
        parent=None
    ):


        self.operation = operation

        self.function = function

        self.parent = parent



    def __repr__(self):

        return (
            f"Node("
            f"{self.operation}"
            f")"
        )