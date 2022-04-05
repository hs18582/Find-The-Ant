# Implementation Report

# List of Contents
* [Technology used](#technology-used)  
    * [PyCharm 2021.3.3](#pycharm-2021.3.3)
        * [How to run the game through Pycharm](#how-to-run-the-game-through-pycharm)  
	    * [What is PyCharm](#what-is-pycharm) 
    * [Python IDLE](#python-idle)
    * [Pygame](#pygame)
* [Why is the code written in this way](#why-is-the-code-written-in-this-way)
* [Diagrams](#diagrams)  
    * [Use Case Diagram](#use-case-diagram)  
	* [Game Flowchart](#game-flowchart)

## Technology used
Here are the list of software I used:
* Pycharm 2021.3.3
* Python 3.8 (Pygame library)

### Pycharm 2021.3.3
The main software I used to create this game was Pycharm. I used this software compared to Python IDLE was because I was able to connect to gitlab from Pycharm and directly commit my code from there. This saved me a lot of time, however there are other methods that I could have used such as through the command prompt. Python interpreter is already integrated therefore you dont need Python IDLE downloaded. It also has its own terminal so the PC command prompt cannot be used, but the PyCharm terminal can used as you would on a normal PC terminal (this was how pygame was downloaded)

#### What is PyCharm
PyCharm is a dedicated Python Integrated Development Environment (IDE) which provides tools for developers all in one place. Which can be used for an effective Python, web, and data science development.
![picture](Documentation/Images/Implementation/Pycharm.JPG)

#### How to run the game through Pycharm
As I am a student I was able to ge the [free educational license](https://www.jetbrains.com/community/education/#students) this would give professional Pycharm for free
If not the code would also work with the free version:
Here is where to [download PyCharm ](https://www.jetbrains.com/pycharm/download/#section=windows)

Once you have downloaded Pycharm, would would need to make sure the interpreter is python 3.8. Then open up the project in Pycharm. 
Open up the terminal `pip install pygame`. Hopefully before this you would have pip automatically installed. Run the game. Pygame can also be added through the IDE, libraries.

### Python IDLE
[Python 3.8 download](https://www.python.org/downloads/release/python-358/)
Python is a programming language that supports objects, modules, threads, and automated memory management. Its benefits are well established. It is easy to use, portable, extendable, has a built-in structure, and is open-source.

Eventhough the game was created in Pycharm, it can be run and edited in Python IDLE as well. In this case pygame should be downloaded through the PC terminal

### Pygame
[Pygame download](https://www.pygame.org/download.shtml)
Pygame is a collection of Python modules for creating video games that is cross-platform. It's a Python-based collection of computer graphics and sound libraries.

## Why is the code written in this way
The format of the code written in a specific way so it is easy to find. It starts of the with the class where the variables are initialsed and used thorughout the code. The iInitialising class is added in to get rid of any global variables. Then the rest of the order is in which it it shown in the game except main menu which is at the end as it calls all/most functions. 
The order is the following:
* Initialising Class
    * setN function
    * getN function
    * setHighscore function
    * getHighscore function
* Write to file function
* Levels function
* Game function
* Winner function
* Loser function
* Highscore function
* Rules function
* Pheromone colours function
* Main menu function

## Diagrams
### Use Case Diagram
![picture](Documentation/Images/Implementation/UseCase.png)
### Game Flowchart
![picture](Documentation/Images/Implementation/Flowchart.jpg)
