import os

# Define the base directory for the project
base_path = "/home/dci-student/Projects/Study-DCI/Study/Git_Tasks/group-project-Geronimo1975"

# Define the structure of the project
project_structure = {
    "InventoryManagementSystem": {
        "inventory": [
            "__init__.py",
            "product.py",
            "inventory_manager.py"
        ],
        "tests": [
            "__init__.py",
            "test_inventory_manager.py"
        ]
    },
    "main.py": None,
    "requirements.txt": None
}

# Create the project structure
for folder, contents in project_structure["InventoryManagementSystem"].items():
    folder_path = os.path.join(base_path, "InventoryManagementSystem", folder)
    os.makedirs(folder_path, exist_ok=True)
    if contents:
        for file in contents:
            open(os.path.join(folder_path, file), 'w').close()

# Create the main.py file at the root level
open(os.path.join(base_path, "InventoryManagementSystem", "main.py"), 'w').close()

# Create requirements.txt
requirements = """
unittest
"""
with open(os.path.join(base_path, "InventoryManagementSystem", "requirements.txt"), 'w') as req_file:
    req_file.write(requirements)

print("Project structure created successfully!")
