import numpy as np

class Neuron:
    # Don't change anything in the `__init__` function.
    def __init__(self, examples):
        np.random.seed(42)
        # Three weights: one for each feature and one more for the bias.
        self.weights = np.random.normal(0, 1, 3 + 1)
        self.examples = examples
        self.train()

    # Don't use regularization.
    # Use mini-batch gradient descent.
    # Use the sigmoid activation function.
    # Use the defaults for the function arguments.
    def train(self, learning_rate=0.01, batch_size=10, epochs=200):
        # Write your code here.
        curr_spot = 0
        # Looping through all the examples given
        for epoch in range(epochs):
            # Looping through the mini-batch
            while(curr_spot < len(self.examples)):
                batch = self.examples[curr_spot:curr_spot+batch_size]
                gradient_per_weight = np.array([0, 0, 0, 0], dtype=float)
                # Looping through a batch
                for sample in batch:
                    curr_prediction = self.predict(sample["features"])
                    features = sample["features"] + [1]
                    # Summing the loss for each weight for the batch
                    for weight in range(len(self.weights)):
                        gradient_per_weight[weight] += (curr_prediction - sample["label"]) * features[weight]
                gradient_per_weight = [gradient / batch_size for gradient in gradient_per_weight]
                # Update the weights
                for weight in range(len(self.weights)):
                    self.weights[weight] = self.weights[weight] - (learning_rate*(gradient_per_weight[weight]))
                curr_spot += batch_size
            curr_spot = 0

    # Return the probability—not the corresponding 0 or 1 label.
    def predict(self, features):
        # Write your code here.
        x = np.dot(features + [1], self.weights)
        activation = 1/(1 + np.exp(-x))
        return activation
