[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2ikCo-Ga)
# Inventory_Management_System

**Topics**

- All the python module 

**Project Description:**

The objective of this project is to develop a simple inventory management system for a store. The system will allow you to add products, remove products, update quantities, retrieve product information, and calculate the total value of the inventory.
It involves creating classes to represent products and an inventory manager to handle product operations. You will implement unit tests using the unittest module and mock external dependencies for testing.

**Project structure**

To organize our project, we will create multiple files and folders. Follow the steps below to set up the project structure:

Create a new folder for your project. Name it something like `InventoryManagementSystem`.
Inside the `InventoryManagementSystem` folder, create the following sub_folders:

- `inventory` : This folder will contain the implementation of the inventory-related classes.
- `tests` : This folder will contain the unit tests for the inventory-related classes.

Create the following files and place them in the corresponding folders:

- `inventory/product.py` : This file will contain the implementation of the `Product` class.
- `inventory/inventory_manager.py`: This file will contain the implementation of the `InventoryManager` class.
- `tests/test_inventory_manager.py`: This file will contain the unit tests for the `InventoryManager` class.

your project structure should look something like this:
```
InventoryManagementSystem/
├── inventory/
│   ├── __init__.py
│   ├── product.py
│   └── inventory_manager.py
├── tests/
│   ├── __init__.py
│   └── test_inventory_manager.py
└── main.py
```

**Note**: this is the simplest structure. You can further organize it into submodules if your project grows.

**Implementetion steps**

1. Step 1: Implement the `Product class` in `product.py`

    - Define a class named `Product` 
    - Add attributes such as `name`, `price`, `quantity`, etc., to the `Product` class
    - Implement methods to update product details such as `update_quantity` to update the quantity of the product. You can implement similar methods for updating the price or other attributes.
    - Implement the `get_product_info` method (or call it the way you prefer) to return a string representation of the product's information.
    
 2. Step 2: Implement the `InventoryManager` Class in `inventory_manager.py`:
    - Define a class named `InventoryManager`.
    - Implement methods in the class to add products, remove products, update quantities
    - Create a method to retrieve product information by providing a `product_name` parameter. If the product with the given name exists in the inventory, call the corresponding method of the `Product`       object to retrieve its information; otherwise, return a "Product not found" message.
    - Implement a method called `get_total_inventory_value` to calculate the total value of the entire inventory. This method should allow you to determine the total worth of the inventory by summing         up the individual values of each product based on its price and quantity.
  

 3. Step 3: Remember to create the `main.py` file at the root level.
    - It serves as entry point for your application. Typically, the main file is responsible for starting the program, initializing objects, and calling relevant functions.
    - Creates an instance of the `InventoryManager`, adds some sample products to the inventory, and then calculates and prints the total inventory value.   
    

4. Step 4: Write Unit Tests in `test_inventory_manager.py`:
    - Use the unittest module to write unit tests for the `Product` and `InventoryManager` classes.
    - Import all the necessary modules in the test file.
    - In the `setUp` method, create an instance of the `InventoryManager` class and assign it to `self.inventory_manager`. This method is executed before each test method.
    - Inside the `TestInventoryManager` class, define test methods for each functionality of the `InventoryManager` class. (e.g. the method for adding products, removing products and so on;
      Remember the arrange, act and assert phase. Each test method should start with the necessary arrangements, such as creating `Product` instances and adding them to the `InventoryManager`.)
    - Navigate to the root folder of your project (`InventoryManagementSystem`).
    - Run the following command to execute the unit tests: `python3 -m unittest`.
  
**Note**: If you want a more user-friendly interface, consider creating a GUI using Tkinter.
                 
          
 5. Step 5: Add Extra Features:
     - You can extend the project by adding additional functionalities to the `Product` and `InventoryManager` classes.
       For example, you can implement features like searching for products, generating reports or statistics on the inventory, create categories for the inventoryetc.
     - Write corresponding unit tests for the new features to ensure their correctness.
     - Update the test cases in `test_inventory_manager.py` to cover the new functionalities.
     - **Note**
      - You can use to **Mock** any external dependencies or interactions, as external services, using the `mock` module to isolate the tests.
        Identify the part of the code that requires mocking,  (e.g., the behavior of the `Product` objects and the `InventoryManager` object,in `get_total_inventory_value`) for testing purposes.
        However, I can suggest for understanding purposes to add a function with external dependencies, in the `InventoryManager` class:
           - you can create a `external_service.py` file in the inventory folder. Create a method (`add_product_with_logging`), that takes the name of the product as an argument and prints a message to simulate the logging process ("Logging product addition:").
           (Remember, this is a simplified example to demonstrate the concept of an external dependency. In a real-world scenario, the ExternalService class might interact with a database, API, or other external systems.)
           - The `ExternalService` class simulates an external service, such as logging or notification functionality, in the `inventory_manager.py` (Call the external service to log the addition of the product)
           - Use mocking to test add_product_with_logging and `get_total_inventory_value`.
           
           (you can watch this video for getting an idea: https://www.youtube.com/watch?v=xT4SV7AH3G8 (please do not worry, in future we will learn more about API)

Remember to write clean and readable code, follow best practices, and document your code using comments to make it more understandable for yourself and others who may review or maintain it in the future. 
By completing this exercise, you will gain hands-on experience in implementing unit tests using unittest and applying mocking techniques to isolate dependencies for testing. 
You will also enhance your understanding of writing test cases, assertions, and verifying expected outcomes.

###Summary of the Fields Covered:
- Software Development: OOP, software design patterns, modularization.
- Business & Enterprise Systems: Inventory management.
- Testing & Quality Assurance: Unit testing with unittest and mocking.
- Automation: Automating the tasks of managing an inventory.
- Data Management: Handling and processing product data.


## How to work in groups by using SCRUM?

- Define the roles:
  
  - Product Owner: The person responsible for defining the product's features and ensuring that the team delivers value to the customer. In this case, the Product Owner will prioritize features (e.g., managing the product inventory).
  - Scrum Master: The facilitator who ensures the team follows Scrum practices. They help remove impediments and keep the team focused on goals.
  - Development Team Members: In this case, all group members will be part of the development team. Each of them can be responsible for different tasks, such as coding, testing, and implementing features.
  (for practicing reason product owner and scrum muster will be also developers)

- Break Down the Project into Tasks (Product Backlog)
    - Backlog: List of all the tasks that need to be done.
    - To Do: Tasks that are selected for the current sprint.
    - In Progress: Tasks that are currently being worked on.
    - Testing: Tasks that need to be tested.
    - Done: Completed tasks.
  
-  Define the Sprint Plan
   - Sprint duration
   - Sprint goals

 - Scrum encourages daily standup meetings to check on the progress of tasks. These meetings are short (about 15 minutes) and are meant to answer three questions:

       - What did you work on yesterday?
       - What are you working on today?
       - Are there any blockers or issues preventing you from progressing?

- Sprint Review and Retrospective

## How to collaborate on github?

- Create a Repository:
   - One member can create a new repository on GitHub.
   - Make it public (if the project is open-source) or private if at the moment it is internal
   - Add a descriptive README.md file to explain the project's purpose.
 
- add collaborators in the respository, invite team members

- manage permissions
    - Owner: Full control over the repository.
    - Admin: Manage settings and users.
    - Collaborator: Contribute code and manage issues.
 
- Sync and Stay Updated

  - Pull Regularly:
  efore starting new work, pull the latest changes to stay up-to-date.
  - Resolve Conflicts:
   Communicate actively if merge conflicts occur. Resolve them collaboratively if needed.
 
**Note**: Ensure you're working on a separate branch to avoid overwriting others' work on the main branch.
If someone else has made changes to the same branch, you may need to pull their updates first to avoid conflicts.
After completing your work on a branch, create a Pull Request (PR) on GitHub.
Other team members review and approve the changes.
Once approved, the branch is merged into the main branch.
Communicate: Let your teammates know when you’re pushing changes to avoid overlap.











