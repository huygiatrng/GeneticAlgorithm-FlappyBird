# Genetic Algorithm-Reinforcement Learning in Flappy Bird

In this project, we explore the use of a genetic algorithm combined with a neural network for reinforcement learning in the popular game Flappy Bird. The genetic algorithm is used to evolve a population of potential solutions (i.e. neural network weights and biases) over multiple generations, with the goal of maximizing the score achieved by each individual in the population. The neuron network, trained using the genetic algorithm, learns to play the game and reach the highest score possible through repeated trial and error. This approach allows the machine to self-learning and adapt to the game dynamics, ultimately achieving a high level of performance.

<p align="center">
  <img src="https://user-images.githubusercontent.com/67343196/182172948-30f9f13e-3b87-4cb1-900d-ae84da6136a4.gif" alt="review" />
</p>

Reinforcement learning is a type of machine learning that focuses on training agents to make decisions that maximize a specific reward. In the context of the popular game Flappy Bird, this could mean teaching a computer to play the game in a way that achieves the highest possible score. In this project, we use a combination of a genetic algorithm and a neural network to create a reinforcement learning system that can do just that.

The genetic algorithm is a powerful optimization technique that can be used to search for the best solution to a given problem. In our case, the problem is finding the weights and biases of a neural network that allow it to play Flappy Bird as well as possible. The genetic algorithm starts with a population of potential solutions, which we can think of as a group of different neural networks with randomly assigned weights and biases. These networks are then evaluated based on their performance in the game, and the best ones are selected to reproduce and create a new generation. This process is repeated over many generations, allowing the population to evolve and improve until it reaches a high level of performance.

The neural network is a simple model with only one hidden layer and five input parameters. These inputs are the distance to the nearest pipe, the height difference between the bird and the center of the next pair of pipes, the width of the tube, and the dimension of the bird. These parameters are used to make decisions about whether the bird should flap its wings or not, allowing it to navigate through the obstacles and reach the highest score possible.

The program allows us to customize the number of nodes in the hidden layer and the population size in each iteration. This means we can fine-tune the system to find the optimal configuration that works best for the game. In addition, the genetic algorithm allows us to incorporate other factors, such as the bird's previous actions and the game's difficulty, into the decision-making process, allowing for even more sophisticated learning.

Overall, combining a genetic algorithm and a neural network provides a powerful approach to reinforcement learning in Flappy Bird. By allowing the machine to self-learn and adapt to the game dynamics, this system can achieve a high level of performance and maximize the score achieved in the game.
