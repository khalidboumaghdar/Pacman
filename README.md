*This project has been created as part of the 42 curriculum by eanjar, bkhalid.*

<br>

### Description
In this project, we should create a complete and playable Pac-Man game in Python, using object-oriented programming, a simple graphical library (MLX or similar), and a modular, reusable architecture, this is a funny project, it helped us to learn many new concepts in game Development.


### Instructions
to install the packages of the project type this command in terminal at the project root directory:
"make install"

to run the game, type this gommand:
"make run"

to clean the project (remove unnecessary files) type this command:
"make clean"

### Resources
https://www.google.com/search?q=pacman&oq=pacman&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDsyBggCEEUYOzIGCAMQRRg8MgYIBBBFGDwyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgxNDg0ajBqN6gCALACAA&sourceid=chrome&source=chrome.ob&ie=UTF-8https://bbbbbbbbbbbbbbbbbb
https://www.pygame.org/docs/ref/display.html
https://www.youtube.com/shorts/VI3O6-vI-5Q
https://www.reddit.com/r/pygame/comments/12eklyg/maximized_window_in_pygame/
<br>


### Configuration
dyalk a si khalid, inchaaAllah.


### Highscore
dyalk a si khalid, inchaAllah.



### Maze Generation
so the generated maze is generated using the assigned A-Maze-ing packag, so after generating our maze. the first state of it at the begin is simply a 2d list, where the parent/main list contain many lists inside it, where all those lists each one of them indicate to a complete x-directional positional-line, and each one of them, include in inside cells where each one of those cells is represented as a dictionary which indicate to the state of the north, east, south, west, then we take it from this form/state to another form/state in order to represent it into a simple descriptive 2d list, containing only 1 and 0 values where 1 represnet apen corridor and 1 idicate close corridor/wall, we transform it from the state of 2d list of cells-dictionaries, into 2d list of only 0 and 1, so the maze size get doubled and incremented by 1 \ in both width and height.


### Implementation
so for the game mechanism implementation we used the greedy bfs algorithm to move the ghosts into the target, and so for ghsots they are able to be in four modes during the game, scatter mode, or chase mode, or eaten mode, or frightened mode, where each one indicate special move/behavior, and simply I used the bfs greedy algorithm for both the scatter mode behavior and chase mode behavior, and for pacman mouvement I move it trough detecting user keyboard input, depending on the up, down, left and right arrows of the keyboard, since pygame give us the ablility to do that, and for the game implementation we used pygame since it's simple effective and famous python game-devlopment library.

### General Software Architecture
for the project  we followd very important principe related to our custom software devlopment life cyle (SDLC), including custom software design, regulare meetings, and descriptive classes/modules names, which are devided into different folders, and in each folder there is relationships moduls/classes, we used this technique to imporove our custom software engineering princples, since in each folder there is relationships moduls/classes which are related trough importing, methods customisation, imporving code quality, faster debugging time.


### Project Management
dyalk a si khalid, inchaAllah.
