# src/rdd.py


from .node import Node
from .dag import DAG
from .executor import Executor
from .optimizer import Optimizer



class RDD:


    def __init__(
        self,
        data,
        dag=None
    ):


        self.data = data


        if dag:

            self.dag = dag

        else:

            self.dag = DAG()



    # Transformation

    def map(self,function):


        node = Node(

            operation="MAP",

            function=function

        )


        self.dag.add_node(node)


        return RDD(
            self.data,
            self.dag
        )



    # Transformation

    def filter(self,function):


        node = Node(

            operation="FILTER",

            function=function

        )


        self.dag.add_node(node)


        return RDD(
            self.data,
            self.dag
        )



    # Transformation

    def flatMap(self,function):


        node = Node(

            operation="FLATMAP",

            function=function

        )


        self.dag.add_node(node)


        return RDD(
            self.data,
            self.dag
        )



    # Action

    def collect(self):


        print(
            "\nBefore Execution:"
        )


        self.dag.display()



        optimizer = Optimizer()


        optimized_dag = optimizer.optimize(
            self.dag
        )


        executor = Executor(
            optimized_dag
        )


        result = executor.run(
            self.data
        )


        return result



    # Action

    def count(self):

        return len(
            self.collect()
        )