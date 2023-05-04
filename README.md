# AI-FlappyBird
This project explores the use of a genetic algorithm combined with a neural network for reinforcement learning in the popular game Flappy Bird. The goal is to maximize the score achieved by each individual in the population by evolving neural network weights and biases over multiple generations. The neural network, trained using the genetic algorithm, learns to play the game and reach the highest score possible through repeated trial and error. This approach allows the machine to self-learn and adapt to the game dynamics, ultimately achieving a high level of performance.

## Table of Contents
+ Requirements
+ Installation
+ Usage
+ Customization
+ License

###Requirements
Python 3.x
NumPy
Installation
Clone this repository
bash
Copy code
git clone https://github.com/yourusername/flappy-bird-ai.git
Navigate to the project directory
bash
Copy code
cd flappy-bird-ai
Usage
Run the main.py file to start the Flappy Bird game and watch the AI learn how to play.
bash
Copy code
python main.py
The program will run through generations, updating the neural network's weights and biases. The AI's performance should improve over time.
Customization
You can customize the number of nodes in the hidden layer and the population size in each iteration by modifying the settings.py file. This allows you to fine-tune the system to find the optimal configuration that works best for the game. In addition, the genetic algorithm allows you to incorporate other factors, such as the bird's previous actions and the game's difficulty, into the decision-making process, allowing for even more sophisticated learning.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
