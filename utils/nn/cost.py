import numpy as np

# Cost Types
CUSTOM_COST = 'CUSTOM COST'
MSE_COST = 'MSE COST'
LOG_LOSS_COST = 'LOG LOSS COST'

class Cost:
    def __init__(self, cost, cost_derivative):
        """
        Base class for cost functions.

        Parameters:
        - cost: Function to calculate the cost (loss).
        - cost_derivative: Function to calculate the derivative of the cost with respect to predictions.
        """
        self.cost = cost
        self.cost_derivative = cost_derivative
        self.cost_name = CUSTOM_COST

    def print_info(self):
        """
        Prints the name of the cost function.
        """
        print(self.cost_name)

class MSE(Cost):
    def __init__(self):
        """
        Mean Squared Error (MSE) cost function.
        """
        super().__init__(MSE.mse, MSE.mse_derivative)
        self.cost_name = MSE_COST

    @staticmethod
    def mse(y_pred, y_true):
        """
        Calculates the Mean Squared Error between predictions and true values.

        Parameters:
        - y_pred: Predicted values.
        - y_true: True values.

        Returns:
        - MSE value.
        """
        m = y_true.shape[1]
        return np.sum((y_pred - y_true) ** 2) / (2 * m)

    @staticmethod
    def mse_derivative(y_pred, y_true):
        """
        Calculates the derivative of the MSE cost function with respect to predictions.

        Parameters:
        - y_pred: Predicted values.
        - y_true: True values.

        Returns:
        - Gradient of the loss with respect to predictions.
        """
        m = y_true.shape[1]
        return (y_pred - y_true) / m

class LogLoss(Cost):
    def __init__(self):
        """
        Log Loss (Binary Cross-Entropy) cost function.
        """
        super().__init__(LogLoss.log_loss, LogLoss.log_loss_derivative)
        self.cost_name = LOG_LOSS_COST

    @staticmethod
    def log_loss(y_pred, y_true):
        """
        Calculates the Log Loss (Binary Cross-Entropy) between predictions and true values.

        Parameters:
        - y_pred: Predicted probabilities.
        - y_true: True labels (0 or 1).

        Returns:
        - Log Loss value.
        """
        epsilon = 1e-15  # Small value to avoid log(0)
        m = y_true.shape[1]
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Clip values to avoid log(0) or log(1)
        loss = -(1 / m) * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    @staticmethod
    def log_loss_derivative(y_pred, y_true):
        """
        Calculates the derivative of the Log Loss cost function with respect to predictions.

        Parameters:
        - y_pred: Predicted probabilities.
        - y_true: True labels (0 or 1).

        Returns:
        - Gradient of the loss with respect to predictions.
        """
        epsilon = 1e-15  # Small value to avoid division by zero
        m = y_true.shape[1]
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Clip values to avoid division by zero
        loss_derivative = -(1 / m) * (y_true / y_pred - (1 - y_true) / (1 - y_pred))
        return loss_derivative