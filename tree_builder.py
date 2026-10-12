class EmployeeNode:
    """Represents one employee in the company tree."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """Manages the company's reporting structure."""

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Error: Add a team lead first.")
            return

        if current_node is None:
            current_node = self.root

        side = side.lower()

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the LEFT of {manager_name}.")
                else:
                    print(f"Error: {manager_name} already has a left report.")
            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the RIGHT of {manager_name}.")
                else:
                    print(f"Error: {manager_name} already has a right report.")
            else:
                print("Error: Side must be left or right.")
            return

        if current_node.left is not None:
            self.insert(manager_name, employee_name, side, current_node.left)
            return

        if current_node.right is not None:
            self.insert(manager_name, employee_name, side, current_node.right)
            return

        print(f"Error: Manager '{manager_name}' was not found.")

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            if node is None:
                return

        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    company = TeamTree()

    while True:
        print("\nTeam Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if company.root is not None:
                print("Error: The team lead has already been added.")
            else:
                name = input("Enter team lead's name: ").strip()
                if name:
                    company.root = EmployeeNode(name)
                    print(f"{name} added as the team lead.")
                else:
                    print("Error: Name cannot be empty.")

        elif choice == "2":
            if company.root is None:
                print("Error: Add a team lead first.")
                continue

            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input("LEFT or RIGHT? ").strip().lower()

            if employee:
                company.insert(manager, employee, side)
            else:
                print("Error: Employee name cannot be empty.")

        elif choice == "3":
            print("\nCurrent Team Structure:")
            company.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    company_directory()


# Design Memo

# Recursive insertion works by checking the current employee to see if
# they are the manager we want. If they are, the new employee is added
# to the selected side if that spot is open. If not, the method searches
# the existing branches to find the right manager.
#
# One challenge was making sure the program checks whether a spot is
# already taken and handles managers that do not exist. Recursion can
# be confusing because the method calls itself with a different node
# each time. Testing different managers and both sides helped me
# understand how the tree grows.
#
# Trees are useful when information has a clear hierarchy. A company
# directory is one example because employees report to managers, who
# may report to other managers. Trees can also organize computer files,
# website elements, and family relationships. Compared with a simple
# list, a tree makes these parent-child relationships easier to
# represent and follow.