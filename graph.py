class Graph:
    def __init__(self):
        self.matrix_ady : list[list] = []

    def create_graph(self, number_of_nodes):
        zeros_matrix : list[list] = [[0] * number_of_nodes] * number_of_nodes
        value = None
        for rows in range (len(zeros_matrix)):
            for columns in range (len(zeros_matrix[0])):
                value = (input(f"Node {rows+1} is connect with Node {columns+1}?\nAnswer(y/n): "))
                while (value.lower() != "y") and (value.lower() != "n"):
                    value = (input(f"Oops, last entry doesn't work please enter again\nNode {rows+1} is connect with Node {columns+1}?\nAnswer(y/n): "))
                if value.lower() == "y":
                    value = 1
                elif value.lower() == "n":
                    value = 0
                zeros_matrix[rows][columns] = value
        final_matrix = zeros_matrix
        self.matrix_ady = final_matrix
