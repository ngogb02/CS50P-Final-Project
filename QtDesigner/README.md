# Project Title: My House's Inventory 
#### Video Demo: [Youtube Video](https://www.youtube.com/)
#### Introduction: 
Everytime I'm at Costco with my wife, we end up forgetting or arguing about what we still have left at home, and, in my opinion, we end up buying more than we need!     

me: "we don't need more saran wrap"  
her: "yes, we do, we're running out"  
*thinking to myself*: I wish I had an inventory that shows what we currently have at home to win this arguement*

In this project, I created a GUI (graphical user interface), that display a list of items currently available in my house. For the GUI layout design, I took inspiration from a MMOPRG (Massive Multiplayer Open Role Playing Game) game's inventory. In this case, I took inspiration from my childhood's favorite MMORPG - MapleStory. The inventory from MapleStory looks like this:

MapleStory Inventory:  
![alt text](https://i.redd.it/2is64cwcsgya1.jpg)

My inventory GUI will be similar to this, it will have tabs for each different category (in the image above, there are "EQUIP, USE, ETC., SET-UP, CASH, DEC." tabs). 
Each tab will display/house items that should belong in that category. 

Ultimately, it is up to the user to decide what items they want to put in their inventory and what category those items should belong in. After all, the user should create an inventory that best suits them. 

## Table of Contents
1. [Introduction](#inspiration)
2. [Description](#description)
3. [Front End Description](#front-end-description) 
    - [How to navigate the GUI](#1-how-to-navigate-the-gui)
    - [GUI Design Layout](#2-gui-design-layout)
4. [BackEnd Description](#backend-description)

## Description: 
<div style="text-align: justify">Most, if not all, of this project is written using OOP (object oriented programming). The reason why I decided on this was because:

1. I learned that games are written using OOP because characters and items share attributes, and using OOP is a powerful way to create many unique characters and items that share an inherent trait. For example, every game character has a health bar and a mana bar. Obviously, this isn't a game project and has nothing to do with building a game, but using MMORPG was a great way for me to visualize how OOP works.  
2. I wanted to get more practice and exposure to OOP. 
I will attempt to explain how the core principles of OOP (Abstraction, Encapsulation, Inheritance, and Polymorphism) was used in my project. 


The GUI of this project was created using the PySide6 Python package/module and along side it, Qt Designer, which came with the PySide6 package/module.
The project description will first go over the frontend side, which is the GUI, how to navigate and use it. Then, it will shift to explaining the backend side of the GUI, diving into the underlying functions and how it works under the hood. The later portion will go over lession learns, mistakes, flawed structures, etc...  

### FrontEnd Description
#### 1. How to navigate the GUI:
_Figure 1. My House's Inventory GUI_:<br>![alt text](image-1.png)

This  is the GUI that will launch when the user runs _main.py_ *PLACEHOLDER*
Note that when a new user launches the application, the table will be empty and there won't be any category tabs.
It is up to the user to input in their items and determine what category those items should belong to. 

The GUI has 3 push buttons:
1. Button - Create a new item:  
    <div style="text-align: justify">This button is to create a brand new item in your inventory. Looking at Figure 1, category Fruits, you can see there 
    are many items already existing, like Apple, Banana, etc... 
    You would want to use this button "Create a new item", when you want to input a new item that doesn't yet exist, say, for example, DragonFruit. 
    In this section, you would also input in the quantity (how many of the item you want to input),
    the location selection (where it is place in your house), date (when was the date you input in the item - note that the GUI has a little 
    date/time icon at the bottom right corner to help the user know what is the current time and date), and finally, there is a 
    category selection (where you decide the item should go into).  
    Here, the location and category have a few selections for the user to choose from. This is imposed on the user
    so that the user doesn't create too many categories and too many random locations. It was also to demonstrate the usage of a 
    selection bar in the GUI. The selection bar is called a "Combo Box" by the package/module Pyside6, that was used to create the GUI. The technicality of
    PySide6 and the implementation of this button "Create a new item" will be explained in greater details in the Backend Section (PLACEHOLDER). </div> <br>                                                                                                                                                            
2. Button - Adjust item:  
    <div style="text-align: justify">This button is for the user to adjust the attributes of the items that already exist within the table, like 
    quantity, location, date, and even category. Even though the button "Adjust item" takes in the same arguments as the button "Create a new item", under the hood
    they do things differently. Admittedly, the design of the button "Adjust item" was poorly conceptualized and seems almost redundant or too cumbersome to use. 
    In section <em>Lessons Learned (PLACEHOLDER)</em>, a discussion of flawed structure and project deisgn/planning is what led to this. The implementation of this button will be explained
    in greater details in the Backend Section.</div><br>
   
3. Button - Remove item:  
   <div style="text-align: justify"> This button is for the user to remove a certain item from a certain category, if the user does not specify the item's name, and 
   only the have the category selected, it will remove that category, which means it will remove every items within that category. Again, the implementation of this 
   button will be explained in greater details in the Backend Section (PLACEHOLDER). </div>

#### 2. GUI Design Layout:
#### Main Layout:  
<div style="text-align: justify"> First thing you'll notice about this layout is that you can't drag the border to minimize or enlarge it, and that the enlarge icon on the top right corner
is greyed out, indicating that there's no entire screen maximize option. This was purposefully implemented to maintain a fixed size main window so that there 
would not be a need to set the buttons, line edits, tables, etc... to scale properly in the event that the main window size is changing, thus reducing unnecessary complexity.    

### Icons:  
The icons used in this GUI were downloaded from a free source ([flaticon](https://www.flaticon.com/)).
Icons were added to be attached to all of the push buttons, the date/clock at the bottom right corner, and depending on which Operating System the user is running on, they may also see an icon next to the application's title "My House Inventory". User using Linux will likely see a centered application's title and no icon. 
In the top right corner, an image is embedded and placed in the corner of the GUI, this is just for decoration purposes and keeping the MapleStory game inventory's theme. </div>

## BackEnd Description
These are the relevant files in this project that are all needed to properly connect the GUI's frontend and backend to produce a functioning application:
1. class_project.py    
2. classes.py
3. project.py
4. inventory.json
5. main.py
6. My_House_Inventory.ui -> My_House_Inventory.py (this file is produced by Qt Designer - see explaination on _PLACEHOLDER_)
8. resource.qrc -> resource.py (this file is produced by Qt Designer - see explaination on _PLACEHOLDER_)

The images/icons are not actually needed to run the application, but nice to have, to produce a polished looking GUI. 
<br> 8. images folder (this folder contains the images for setting the icons mentioned in the FrontEnd section)

### class_project.py
This file contains the class House() and class InputReq():

The importance of this file is that when the user presses "Create a new item", the code will create a custom class with the name of that item, and that class will inherent the class InputReq(). Then it will initialize that newly created class to create a custom object that contains the instance attributes from InputReq(), thus defining the location, quantity, and date of the newly created custom object. In summary, InputReq() is what give the items its attributes. Note that class_project.py by itself, does not do all of this, many of the other files call to it to be able to inherent InputReq() and set instance attributes to the item created by the user. 

The class House() is initialized in file project.py _PLACEHOLDER_, class House() essentially acts like a dictionary, where after the user has created their items, they can put those items into the inventory. In hindsight, this was not a great way to structure how data were being passed and stored, it will be discussed in the lesson learned section. 

- class House() is initialized with an empty dictionary called "inventory". Within class House(), there are 3 methods add_item(), remove_item(), and print_inventory(). 
As stated, since class House() gets initiated with an empty dictionary "inventory", the 3 methods are for adding items into the inventory, removing items from the inventory, or print what's currently in the inventory.<br>  
Note that these are just code snippets to aid visualization. 
```python
        def __init__(self) -> None:
        self.inventory = {}

        def add_item(self, category: str, *item) -> None:
            ...
        def remove_item(self, category: str, *item) -> None:
            ...
        def print_inventory(self):
            ...
```
<br>

- class InputReq(), this class has several instance attributes for initialization. All of the attributes are default to None so that a user does not have to input in every arguments to run compile the code. Note that attribute _price_ and _barcode_ will not be used in this entire project. It was the included in the beginning of the project, but in order to reduce complexity and development time, it is considered inactive. It is still kept in the source code as a showcase for later section discussing about lessons learned.
2 interesting methods in the class InputReq() is _add_ and _consume_, these methods may not have been put to use and will be discussed about in the lesson learned.<br>  
Note that these are just code snippets to aid visualization.  
```python
        def __init__(self, location: str = None, quantity: int = None, date: str = None, price: float = None, barcode: int = None) -> None:
        self.location = location
        self.quantity = quantity
        self.date = date
        self.barcode = barcode #-> concept for next iteration, for now stays as None :)
        self.price = price
        ...

        #adding for quantity increase
        def add(self, _: int):

        #consuming for quantity decrease
        def consume(self, _: int):
```

### classes.py
Initially, this file does not contian anything, but its first line must be:
```python
    from class_project import InputReq
```
The reason by this is to be, is because whenever the user pressed the button "Create a new item", the code will open up this file "classes.py" and write to it. It will create a class with the name of the item the user has input, and it will inherent InputReq from class_project.py. Then, it will create an object by initializing the class and set the instance attributes to the user input. Recall that prior to clicking "Create a new item" on the GUI, the user has to input in the Item Name, Quantity, Location, Date, and Category (view Figure 1 for visual reference). 

Essentially, this file houses all of the custom class of each items and its initial instance attributes. _PLACEHOLDER: need to describe the flaw of this structure_

### project.py
This file is basically the main file that pulls everything together, it import class House() from "class_project.py" to initialize the empty dictionary, so that items can be put into that dictionary. This file also import from "classes.py", in order to get access to all of the items that the user has created, so that those items can be placed into the dictionary/inventory. Recall that "classes.py" houses all the initial classes and objects. 

The way that this entire file works, is that first, it creates the item, then it put those items inside the initially empty dictionary/inventory. The inventory is used to update the JSON file, the JSON file is what is used to display the item that's currently in My_House_Inventory. The JSON file basically acts as the database that contains all of the items that the user has created. Of course, with adding items, this file also provide functions to remove items or adjust its attributes. 

How this was set up to update the JSON file is admittedly, once again, not ideal and will be discussed in Lession Learned section. 

```python
    from class_project import House
    from classes import *
    from icecream import ic
    import sys, json, os

    my_house = House()

    # This function writes to classes.py.
    # Create a custom item class that inherits InputReq from class_project.py, 
    # Then create that class object with the attributes from user inputs.
    def create_item_class(item_name: str, location: str, quantity: int, date: str) -> None:

    # This function calls method in class House() to add items into the inventory "my_house"
    # This function basically acts to populate the inventory, which is used to update the JSON file.
    def insert_items_into_inventory(Category: str, *item: object) -> None:
        
    # This function calls method in class House() to remove items into the inventory "my_house"
    # This function basically acts to populate the inventory, which is used to update the JSON file.
    def remove_items_from_inventory(Category: str, *item: object) -> None:

    # This is a passive function mainly used to aid developer visualization and troubleshooting; basically shows what's currently in the inventory/dict.
    def show_init_inventory() -> None:

    # This function loads the json file and set it to a variable. Note that the json file contains items that are put in a dictionary structure; [category][item_name][item_attributes].
    def load_inventoryJSON(filename: str) -> None:

    # This file will call load_inventoryJSON to get what's currently in the JSON file, and modify depending on removing or adding items. 
    # After completing, this file will call save_inventoryJSON, to update the JSON file with the latest info.
    # When the user press "Adjust item", it will will this function, which calls the other functions, to basically update the JSON file as appropriate, so that the changes are visually reflected on the GUI. 
    def update_inventoryJSON(filename: str) -> None:
    
    # Saves the newly updated inventory into JSON file. Gets called by update_inventoryJSON at the end. 
    def save_inventoryJSON(inventory: str, filename: str) -> None:
    
    # Function used to remove certain items from the JSON file, by removing item from the JSON file, it will remove that item from showing up in the GUI.
    # When the user presses "Remove item", this function will be called, given that the user has specific the name of the item they want to remove.  
    def remove_item_from_JSON(filename: str, category: str, *items: object) -> None:

    # Function used to remove the entire category from the JSON file, this will also delete every items that exist within that category, and the GUI will reflect that change by  deleting the category tab and no items are 
    # associate with it. 
    # If the user does not specify an item name when pressing "Remove item", it will remove the entire category and any items that lives in that category.
    def remove_category_from_JSON(filename: str, category: str) -> None:
```

### inventory.json
As mentioned in project.py, this file is the database that houses all the information about the category, items, and its attributes. When the GUI display the information, that information is from this database, the inventory.json. When the user create an item, that item is written into this inventory, and when a user remove an item, that item is removed fromt his database. 

The structure of this database is similar to that of a python dictionary. It can be seen as such; inventory[category][item_name][attributes]. Each item is belongs to a certain category, and each item has several attributes linked to it. 

### main.py 
This file just contains the basic set up for launching the GUI, the majority of the codes responsible for the GUI layout and behavior is not embedded in this file. 

### My_House_Inventory.py | My_House_Inventory.ui -> ui_My_House_Inventory_01.py 
First, lets clarify any confusion. My_House_Inventory.py, My_House_Inventory.ui, and ui_My_House_Inventory_01.py are 3 different files that does different things. 

My_House_Inventory.py is the file responsible for setting up the entire GUI, the layout, the information display, the buttons, the connections, etc... When you run main to launch the GUI, the main.py imports My_House_Inventory to launch the GUI. 

Now, lets briefly talk about PySide6, which is the python package/module that was used to contruct the GUI. Along with PySide6, there is an application that can be launched by typing in the terminal, "pyside6-designer". This is most commonly known as Qt Designer, in short, Qt Designer is an application that allow users to customize how they want their GUI application to look like without having to hardcode in the positions of the buttons, size, vertical/horizontal alignment, etc... think of it as like the coding language Scratch, where users place blocks to construct their code. Anything that cannot be accomplished by Qt Designer would need to be hardcoded. In a way, this takes out all of the unnecessary coding and leaves only the things that needs to be coded, to be coded. 

The way that PySide6 works is that after you are finished with generating a layout, it will be saved as a .ui file, the .ui file is not something python can read, so it must be converted to a .py, so why the tite is stated as "My_House_Inventory.ui -> ui_My_House_Inventory_01.py ". 

The code to convert .ui to .py file is as such:
```python
    pyside6-uic My_House_Inventory_01.ui > ui_My_House_Inventory_01.py
```

### resource.qrc -> resource.py
