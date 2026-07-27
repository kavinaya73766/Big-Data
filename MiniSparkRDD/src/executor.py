# src/executor.py



class Executor:



    def __init__(self,dag):

        self.dag = dag



    def run(self,data):


        result = data



        for node in self.dag.get_nodes():



            if node.operation == "FILTER":


                result = list(

                    filter(

                        node.function,

                        result

                    )

                )



            elif node.operation == "MAP":


                result = list(

                    map(

                        node.function,

                        result

                    )

                )



            elif node.operation == "FLATMAP":


                output = []


                for item in result:


                    values = node.function(item)


                    output.extend(values)



                result = output



        return result