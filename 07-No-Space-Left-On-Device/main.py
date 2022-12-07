def get_terminal_output_from(file_name):
    with open(file_name) as file:
        return [line.rstrip() for line in file.readlines()[:-1]]


class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.flat_size = 0
        self.total_size = 0
        self.children = []
        self.parent = None

    def add(self, child) -> None:
        self.children.append(child)
        child.parent = self

    @property
    def children_names(self):
        return [child.name for child in self.children]
    
    def calculate_size(self):
        self.total_size = self.flat_size + sum(child.calculate_size() for child in self.children)
        return self.total_size


def populate_tree(root: Directory, terminal_output):
    current_node = root

    # Skip cd to root
    for line in terminal_output[1:]:

        if current_node is None:
            raise Exception("too many 'cd ..' were given")

        if line[2:4] == "cd":
            dir_name = line.split(" ")[2] + " (dir)"
            if ".." not in dir_name:

                if dir_name not in current_node.children_names:
                    raise Exception("cd in unknown directory")
                else:
                    current_node = [
                        child
                        for child in current_node.children
                        if child.name == dir_name
                    ][0]
            else:
                current_node = current_node.parent

        elif line[2:4] == "ls":
            continue

        else:
            if "dir" in line:
                new_node = Directory(line.split(" ")[1] + " (dir)")
                current_node.add(new_node)
            else:
                file_size = int(line.split(" ")[0])
                current_node.flat_size += file_size


root_directory = Directory("root")
populate_tree(root_directory, get_terminal_output_from("test_input.txt"))
root_directory.calculate_size()
print(root_directory.total_size)
