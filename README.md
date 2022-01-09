# Ex4_OOP
# POKEMON GAME 
In this assignment we were asked to design a Pokemon game, given a directed weihted graph, a set of agents located on the graph and pokemons located on the graph as well. <br>
The agents should catch as many pokemons as possible.
* __Pokemons :__ Each pokemon has its value, type and position.
* __Agents :__ Each agent has its id, value, source, destination, speed, position. <br>

## Game info :
- The game is played on a server wich was given to us, `Ex4_Server_v0.0.jar`
- The game has 16 cases to choose from [0,15]
- Each case has different number of pokemons and agents.
- Each gane has a fixed time between 30 and 120 seconds.
- We had to implement some methods from `Cient class`:
- - __get graph__
- - __get pokemons__
- - __get agents__
- - __add agent__
- - __Start the game__
- - __get the remaining time__
- - __choose next edge__
- - __move agents__
- - __get the game info :__ the grade and the number of moves of the current game. This data is printed at the end of each game.

### Our goal :
Our goal was to catch as many pokemons as possible and to maximize the overall sum of weights of the grabbed pokemons, but without exceeding the maximal 10 calls to move per second.

### Classes :
We used classes from `https://github.com/Lara1011/Ex3_OOP.git`, in addition to:
- __`Agent class` :__ Each agent has id, value, source, destination, speed, position.
- __`Pokemon` :__ Each pokemon has value, type and position.

