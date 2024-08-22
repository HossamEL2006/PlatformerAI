import numpy as np

# Layer Types
CUSTOM_LAYER = 'CUSTOM LAYER'
DENSE_LAYER = 'DENSE LAYER'
ACTIVATION_LAYER = 'ACTIVATION LAYER'

# Activation Types
CUSTOM_ACTIVATION = 'CUSTOM ACTIVATION'
SIGMOID_ACTIVATION = 'SIGMOID ACTIVATION'
RELU_ACTIVATION = 'RELU ACTIVATION'
LEAKY_RELU_ACTIVATION = 'LEAKY RELU ACTIVATION'
TANH_ACTIVATION = 'TANH ACTIVATION'

class Layer:
    def __init__(self):
        """
        Base class for all layers in the neural network.
        """
        self.type = CUSTOM_LAYER
        self.input = None
        self.output = None

    def forward(self, input_values):
        """
        Forward pass logic for the layer. Should be overridden by subclasses.

        Parameters:
        - input_values: Input data for the layer.

        Returns:
        - Output after the layer's operations.
        """
        pass

    def backward(self, original_gradient, learning_rate=0.1, debug=False):
        """
        Backward pass logic for the layer. Should be overridden by subclasses.

        Parameters:
        - original_gradient: Gradient of the loss with respect to the layer's output.
        - learning_rate: Learning rate for updating the layer's parameters.
        - debug: Boolean flag to print gradients for debugging.

        Returns:
        - Gradient of the loss with respect to the layer's input.
        """
        pass

    def print_info(self):
        """
        Prints information about the layer. Should be overridden by subclasses.
        """
        print('(No description specified)')

class Dense(Layer):
    def __init__(self, input_size, output_size):
        """
        Fully connected layer (Dense layer).

        Parameters:
        - input_size: Number of input units.
        - output_size: Number of output units.
        """
        super().__init__()
        self.type = DENSE_LAYER
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.normal(size=(output_size, input_size))
        self.biases = np.random.normal(size=(output_size, 1))

    def forward(self, input_values):
        """
        Performs the forward pass by calculating the weighted sum of inputs and adding biases.

        Parameters:
        - input_values: Input data for the layer.

        Returns:
        - Output of the layer after applying weights and biases.
        """
        self.input = input_values
        self.output = self.weights @ input_values + self.biases
        return self.output

    def backward(self, original_gradient, learning_rate=0.1, debug=False):
        """
        Performs the backward pass, updating weights and biases using gradient descent.

        Parameters:
        - original_gradient: Gradient of the loss with respect to the layer's output.
        - learning_rate: Learning rate for updating the layer's parameters.
        - debug: Boolean flag to print gradients for debugging.

        Returns:
        - Gradient of the loss with respect to the layer's input.
        """
        # Compute gradients
        dcdW = original_gradient @ self.input.T
        dcdb = np.sum(original_gradient, axis=1, keepdims=True)
        dcdX = self.weights.T @ original_gradient

        # Update parameters
        self.weights -= dcdW * learning_rate
        self.biases -= dcdb * learning_rate

        if debug:
            print('W gradient:\n' + str(dcdW))
            print('b gradient:\n' + str(dcdb))

        return dcdX

    def print_info(self):
        """
        Prints information about the Dense layer, including weights and biases.
        """
        print(f'Input size: {self.input_size}')
        print(f'Output size: {self.output_size}')
        print('Weights matrix:')
        print(self.weights)
        print('Biases matrix:')
        print(self.biases)

class Activation(Layer):
    def __init__(self, activation, activation_derivative):
        """
        Activation layer applying a given activation function element-wise.

        Parameters:
        - activation: Activation function to apply.
        - activation_derivative: Derivative of the activation function for backpropagation.
        """
        super().__init__()
        self.type = ACTIVATION_LAYER
        self.activation = activation
        self.activation_derivative = activation_derivative
        self.activation_name = CUSTOM_ACTIVATION

    def forward(self, input_values):
        """
        Performs the forward pass by applying the activation function.

        Parameters:
        - input_values: Input data for the layer.

        Returns:
        - Output of the layer after applying the activation function.
        """
        self.input = input_values
        self.output = self.activation(input_values)
        return self.output

    def backward(self, original_gradient, learning_rate=0.1, debug=False):
        """
        Performs the backward pass using the derivative of the activation function.

        Parameters:
        - original_gradient: Gradient of the loss with respect to the layer's output.

        Returns:
        - Gradient of the loss with respect to the layer's input.
        """
        return original_gradient * self.activation_derivative(self.input)

    def print_info(self):
        """
        Prints information about the Activation layer.
        """
        print(self.activation_name)

class Sigmoid(Activation):
    def __init__(self):
        """
        Sigmoid activation layer.
        """
        super().__init__(Sigmoid.sigmoid, Sigmoid.sigmoid_derivative)
        self.activation_name = SIGMOID_ACTIVATION

    @staticmethod
    def sigmoid(x):
        """
        Sigmoid activation function.
        """
        return 1 / (1 + np.exp(-x) + 1e-15)

    @staticmethod
    def sigmoid_derivative(x):
        """
        Derivative of the sigmoid function for backpropagation.
        """
        a = Sigmoid.sigmoid(x)
        return a * (1 - a)

class ReLU(Activation):
    def __init__(self):
        """
        ReLU activation layer.
        """
        super().__init__(ReLU.relu, ReLU.relu_derivative)
        self.activation_name = RELU_ACTIVATION

    @staticmethod
    def relu(x):
        """
        ReLU activation function.
        """
        return np.maximum(0., x)

    @staticmethod
    def relu_derivative(x):
        """
        Derivative of the ReLU function for backpropagation.
        """
        return np.where(x <= 0, 0., 1.)

class LeakyReLU(Activation):
    def __init__(self, alpha=0.01):
        """
        Leaky ReLU activation layer.

        Parameters:
        - alpha: Negative slope coefficient.
        """
        super().__init__(self.leaky_relu, self.leaky_relu_derivative)
        self.alpha = alpha
        self.activation_name = LEAKY_RELU_ACTIVATION

    def leaky_relu(self, x):
        """
        Leaky ReLU activation function.
        """
        return np.where(x > 0, x, self.alpha * x)

    def leaky_relu_derivative(self, x):
        """
        Derivative of the Leaky ReLU function for backpropagation.
        """
        return np.where(x > 0, 1, self.alpha)

    def print_info(self):
        """
        Prints information about the Leaky ReLU layer, including the alpha value.
        """
        print(f'{self.activation_name}\nAlpha = {self.alpha}')

class Tanh(Activation):
    def __init__(self):
        """
        Tanh activation layer.
        """
        super().__init__(Tanh.tanh, Tanh.tanh_derivative)
        self.activation_name = TANH_ACTIVATION

    @staticmethod
    def tanh(x):
        """
        Tanh activation function.
        """
        return np.tanh(x)

    @staticmethod
    def tanh_derivative(x):
        """
        Derivative of the tanh function for backpropagation.
        """
        return 1 - np.tanh(x) ** 2