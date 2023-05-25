from graph import *
class GraphConsoleUI:
    def __init__(self):
        self.graph = Graph()

    def run(self):
        while True:
            print("WORKSHOP GRAPHS 🤖\n")
            print("1. Create Graph 😃")
            print("2. Show Graph 📊")
            print("3. Add Node 🆕")
            print("4. Find Way 🗺️")
            print("5. Exit 🚪")
            choice = input("Enter your choice: \n")

            if choice == "1":
                self.create_graph()
            elif choice == "2":
                self.show_graph()
            elif choice == "3":
                self.add_node()
            elif choice == "4":
                self.find_way()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again. 😕\n")

    def create_graph(self):
        number_of_nodes = int(input("Enter the number of nodes: \n"))
        self.graph.create_graph(number_of_nodes)
        print("Graph created successfully! 🎉\n")

    def show_graph(self):
        self.graph.show_graph()

    def add_node(self):
        self.graph.add_node()
        print("Node added successfully! 🆗\n")

    def find_way(self):
        node_1 = int(input("Enter Source Node: \n"))
        node_2 = int(input("Enter Destination Node: \n"))
        way = self.graph.find_way_between_two_nodes(node_1, node_2)
        if way:
            print("Path:", way, "🚀\n")
        else:
            print("No path found. 😔\n")



