from copy import deepcopy
from tqdm import tqdm
import numpy as np


class NeuralNetwork:
    def __init__(self, layers_chain, cost):
        """
        Initializes the neural network.
        
        Parameters:
        - layers_chain: List of layer objects defining the architecture of the network.
        - cost: An object of the Cost class (or subclass) defining the loss function.
        """
        self.layers_chain = layers_chain
        self.n_layers = len(layers_chain)
        self.cost = cost

    def forward(self, input_values, y_true=None, debug=False):
        """
        Performs forward propagation through all layers of the network.

        Parameters:
        - input_values: Input data for the network.
        - y_true: True labels for the data (used to calculate cost).
        - debug: Boolean flag to print intermediate outputs for debugging.

        Returns:
        - If y_true is provided: A tuple of final predictions and the calculated cost.
        - If y_true is not provided: The final predictions.
        """
        if debug:
            print("*** Forward Propagation ***\nInput:\n" + str(input_values))
        for i, layer in enumerate(self.layers_chain):
            input_values = layer.forward(input_values)
            if debug:
                print(f"\nAfter layer {i+1}:\n" + str(input_values))
        if debug and (y_true is not None):
            print(f'\nCost: {self.cost.cost(input_values, y_true)}')
        if y_true is None:
            return input_values
        else:
            return input_values, self.cost.cost(input_values, y_true)

    def backward(self, y_pred, y_true, learning_rate, debug=False):
        """
        Performs backward propagation, updating the weights and biases of each layer.

        Parameters:
        - y_pred: Predictions from the forward pass.
        - y_true: True labels for the data.
        - learning_rate: Learning rate for updating the weights and biases.
        - debug: Boolean flag to print gradients for debugging.

        Returns:
        - The gradient of the cost with respect to the input (for debugging).
        """
        output_gradient = self.cost.cost_derivative(y_pred, y_true)
        if debug:
            print("*** Backward Propagation ***\nOutput gradient:\n" + str(output_gradient))
        for i, layer in enumerate(self.layers_chain[::-1]):
            output_gradient = layer.backward(output_gradient, learning_rate, debug=debug)
            if debug:
                print(f"\nAfter layer {self.n_layers-i}:\n" + str(output_gradient))
        return output_gradient

    def fit(self, X, Y, epochs, learning_rate, batch_size=None, save_layers_history=True):
        """
        Trains the neural network using the provided data.

        Parameters:
        - X: Input data matrix.
        - Y: True labels matrix.
        - epochs: Number of iterations over the entire dataset.
        - learning_rate: Learning rate for updating weights and biases.
        - batch_size: Number of samples per batch. If None, uses the entire dataset as one batch.
        - save_layers_history: Boolean flag to save the state of the layers after each batch.
        
        Returns:
        - cost_history: List of costs computed during training.
        - layers_chain_history: List of deep copies of the layers_chain after each batch (if save_layers_history is True).
        """
        if batch_size is None:
            batch_size = X.shape[1]

        x_batches = [X[:, i:i + batch_size] for i in range(0, X.shape[1], batch_size)]
        y_batches = [Y[:, i:i + batch_size] for i in range(0, Y.shape[1], batch_size)]

        cost_history = []
        layers_chain_history = []

        for _ in tqdm(range(epochs)):
            for x_batch, y_batch in zip(x_batches, y_batches):
                y_pred, cost = self.forward(x_batch, y_true=y_batch)
                if save_layers_history:
                    layers_chain_history.append(deepcopy(self.layers_chain))
                cost_history.append(cost)
                self.backward(y_pred, y_batch, learning_rate=learning_rate)
        return cost_history, layers_chain_history

    def print_architecture(self):
        """
        Prints a detailed description of the network's architecture, including layer types and dimensions.
        """
        print('*** Full Architecture ***')
        print(f'Number of layers: {len(self.layers_chain)}')
        for i, layer in enumerate(self.layers_chain):
            print(f'\n* Layer N{i+1} ({layer.type}):')
            layer.print_info()