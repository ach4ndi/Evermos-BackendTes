
## Question ##

### 1. Online Store Problem ###

#### Fact

1. Customers were able to put items in their cart, check out, and then pay. After several days, many of our customers received calls from our Customer Service department stating that their orders have been canceled due to stock unavailability.
2. These bad reviews generally come within a week after our 12.12 event, in which we held a large flash sale and set up other major discounts to promote our store.

1. Our inventory quantities are often misreported, and some items even go as far as having a negative inventory quantity.
2. The misreported items are those that performed very well on our 12.12 event.
3. Because of these misreported inventory quantities, the Order Processing department was unable to fulfill a lot of orders, and thus requested help from our Customer Service department to call our customers and notify them that we have had to cancel their orders.

### 2. Treasure Hunt ###

Build a simple command-line program for helping the user hunt for a treasure that satisfies the following requirements:

#### Requirements

1. Build a simple grid with the following layout :
    ```bash
    ########
    #......#
    #.###..#
    #...#.##
    #X#....#
    ########
    ```

    where `#` represents an obstacle, `.` represents a clear path and `X` represents the player’s starting position.

2. A treasure is hidden within one of the clear path points, and the user must find it.
3. From the starting position, the user must navigate in a specific order: Up/North A step(s), then Right/East B step(s), then Down/South C step(s).
4. The program must output a list of probable coordinate points where the treasure might be located.
5. Bonus points: display the grid with all the probable treasure locations marked with a $ symbol.

## Solution ##

### 1. Online Store Problem ###

Based on my limited knowledge about this problem on e-commerce or warehouse development, we need additional data like history data to tracking this complex problem to find the culprit. But Negative stock quantity problem can be solved where add some validation to check item quantity on inventory every user trying to check out.

### 2. Treasure Hunt ###

just cli application, checking condition each array on matrix of map.

## Answer ##

### 1. Proof of Concept for Online Store Problem ###

* Make sure your machine is already installed python 3.7, before running PoC application.
* Poc for problem online store are on backend directory
* First, make sure your computer is already can used virtualenvwrapper for python <a href="https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation" target="_blank">[How to Install]</a>, read and follow it exactly as stated, most importantly Shell Startup File section.
* After the installion is complete, then create new virtual environment project :
    ```bash
    mkvirtualenv test-evermos
    ```
* When virtual environment is created:
    ```bash
    workon test-evermos
    ```
    your shell will like:
    ```bash
    (test-evermos) .\_git>
    ```
* Second, when already setting up virtual environment, install requirement file for running PoC file
    ```bash
    pip install -r requirements.txt
    ```
* On first time, we need apply migrate database:
    ```bash
    python manage.py migrate
    ```
  and then create super user (default username and password are admin being used on this case):
    ```bash
    python manage.py createsuperuser --email admin@example.com --username admin
    ```
* and run server on local machine:
     ```bash
    python manage.py runserver
     ```
* url for access PoC :
    ```bash
    http://127.0.0.1:8000/admin
    http://127.0.0.1:8000/api/item/?format=api
    ```

### 2. Running Treasure Hunt App ###
* Make sure your machine is already installed python 3.7, before running PoC application. 
* Treasure Hunt App no need any library to run, only python 3.7.
* First, run app:
    ```bash
    python .\index.py
    ```
* You will see some option to pick on app :
    ```bash
    1 : Print Map
    2 : Print Map with treasure
    3 : Print Treasure Position
    4 : Re-position of Treasure
    9 : Play Time!
    0 : Exit
    Option : <choice>
    ```
    Choice :
    ```bash
    1. to print Treasure Map
    2. to print Treasure Map (with treasure marking)
    3. to print Treasure Coordinate
    4. randomize treasure position and set how much treasure appear on the map
    9. play the game
    0. exit from loop
    ```
* When you pick choice 9 for playing treasure hunt, app will show :
    ```bash
    >> Map <<
    ######## 
    #......# 
    #.###..# 
    #...#.##
    #X#....#
    ########
    >> Map With Treasure <<
    ########
    #....$.#
    #.###..#
    #...#.##
    #X#....#
    ########
    Treasure position : [[1, 5]]
    ```
* The map and input movement are following Assessment Instruction, so you only can move up, right and down.