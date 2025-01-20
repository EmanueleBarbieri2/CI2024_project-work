# SYMBOLIC REGRESSION

The proposed program has four different versions each one for a certain number of x variables (1, 2, 3, and 6) but all the versions have the same structure and are simply adaptations of the single x variable problem when considering more variables.

## GP framework
Firstly, the genetic programming framework is setup by defining a ```terminal_set``` (containing the x variables and some numeric constants) and a ```function_set``` (containing different numpy fuctions). The sets are both dictionaries that associate strings to symbols, numbers, or expressions

With the framework, a function ```evaluate_tree_array``` to evaluate a formula for certain values of the different x variables is defined along with functions ```mean_squared_error``` and a ```fitness function``` that also takes into consideration bloating by worsening the fitness of formulas based on their length. 


## Population initialization
Two different tree generation functions are defined; ```generate_full_tree``` and ```generate_grow_tree``` which use the functions ```random_function``` and ```random_terminal``` to select respectively a random function and a random terminal from the ```terminal_set``` and the ```function_set```. The final phase of population initalization ```initialize_population``` generates a population composed in half by grow trees and in half by full trees given a certain population size and max depth.

## Fitness
The function ```evaluate_population``` takes as an argument the population of trees and computes the fitness of each individual returning an array of tuples composed by individuals and their corresponding fitness. 

## Evolution
To evolve the population accross multiple generations a function ```evolve_population``` is defined. The fuction uses the array of individuals with their corresponding fitness and performs ```selection```, ```crossover```, and ```mutation```. Selection is performed by discarding the bottom half of the population ranked by fitness. The discarded half is then filled by individuals that are created using crossover between two different parents or mutation which is similar to crossover but the second parent is generated and runtime using population initalization functions defined previously.


## Best solution
Finally, the best solution is computed by sorting the population by fitness and selecting the most fit individaul. The best individual is then simplified through a ```break_tree``` function that computes a solution whose fitness matches the best solution's fitness by discarding terminals or functions from the best solution starting from the end. 