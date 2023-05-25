class Graph:
    def __init__(self):
        self.matrix_ady : list[list] = []

    def create_graph(self, number_of_nodes):
        zeros_matrix = [[0] * number_of_nodes for i in range(number_of_nodes)]
        for rows in range(len(zeros_matrix)):
            for columns in range(len(zeros_matrix[0])):
                user_input = input(f"Node {rows + 1} is connected with Node {columns + 1}?\nAnswer(y/n): ")
                while user_input.lower() != "y" and user_input.lower() != "n":
                    user_input = input(
                        f"Oops, last entry doesn't work. Please enter again.\nNode {rows + 1} is connected with Node {columns + 1}?\nAnswer(y/n): ")
                connection = 0
                if user_input.lower() == "y":
                    connection = 1
                elif user_input.lower() == "n":
                    connection = 0
                zeros_matrix[rows][columns] = connection
        self.matrix_ady = zeros_matrix

    def show_graph(self):
        print("")
        for row in self.matrix_ady:
            print(str(row))
        print("")
    def add_node(self):
        zeros_matrix = [[0] * (len(self.matrix_ady) + 1) for i in range(len(self.matrix_ady)+1)]
        for rows in range(len(self.matrix_ady)):
            for columns in range(len(self.matrix_ady[0])):
                zeros_matrix[rows][columns] = self.matrix_ady[rows][columns]
        for rows in range(len(zeros_matrix)):
            user_input = input(f"Node {rows+1} is connected with Node {len(zeros_matrix)}?\nAnswer(y/n): ")
            while user_input.lower() != "y" and user_input.lower() != "n":
                user_input = input(
                    f"Oops, last entry doesn't work. Please enter again.\nNode {rows+1} is connected with Node {len(zeros_matrix)}?\nAnswer(y/n): ")
            connection = 0
            if user_input.lower() == "y":
                connection = 1
            elif user_input.lower() == "n":
                connection = 0
            zeros_matrix[rows][len(zeros_matrix)-1] = connection
        for columns in range(len(self.matrix_ady[0])):
            user_input = input(f"Node {len(zeros_matrix)} is connected with Node {columns+1}?\nAnswer(y/n): ")
            while user_input.lower() != "y" and user_input.lower() != "n":
                user_input = input(
                    f"Oops, last entry doesn't work. Please enter again.\nNode {columns+1} is connected with Node {len(zeros_matrix)}?\nAnswer(y/n): ")
            connection = 0
            if user_input.lower() == "y":
                connection = 1
            elif user_input.lower() == "n":
                connection = 0
            zeros_matrix[len(zeros_matrix)-1][columns]=connection
        self.matrix_ady = zeros_matrix

    def find_way_between_two_nodes(self, node_1, node_2, way=""):
        row_node = self.matrix_ady[node_1 - 1]
        if row_node[node_2 - 1] == 1:
            way += f"{node_1} -> {node_2}"
            return way
        else:
            counter = 0
            for connection in row_node:
                counter += 1
                if connection == 1 and counter != node_1:
                    new_way = way + f"{node_1} -> "
                    result = self.find_way_between_two_nodes(counter, node_2, new_way)
                    if result:
                        return result
        return None









