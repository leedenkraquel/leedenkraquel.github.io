---
layout: project
type: project
image: images/fashion-mnist-sprite.png
title: Hand Crafted Neural Network
permalink: projects/Neural Network
date: 2022-03-10
labels:
  - Python
  - Numpy
  - Neural Networks
  - Machine Learning
summary: A simple neural network without the use of common machine learning libraries.
---

I created a neural nework from scratch. This neural network recognizes articles of clothing from the [fashion mnist dataset](http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/). The significance of this simple neural network classifier is that it is constructed without the use of famous libraries such as Keras, Scikit Learn, Pytorch, etc.

# The Fashion MNIST Dataset
The MNIST Fashion dataset includes 70,000 samples of 28x28 grayscale images of clothing articles. Each of these samples are labeled as one of ten classes. The classes are as follows:

0 - T-shirt/top

1 - Trouser

2 - Pullover

3 - Dress

4 - Coat

5 - Sandal

6 - Shirt

7 - Sneaker

8 - Bag

9 - Ankle Boot

# The Neural Network
The simple neural network contained only one hidden layer. The input is a 784x1 array representing the pixels in a flattened sample image. This hidden layer has a size between 1 and 29 neurons. The hidden layer uses a relu function as it's non-linear function. This prevents the values of the weights from dipping below zero. The neural network outputs a 10x1 array which represented a set probabilities that the neural network uses as its prediction for the label of the sample. The output layer uses a softmax function to make sure the probabilities in the output all sum to one.

<img class = "ui fliud image" src = "../images/BadNeuralNetwork.png">

# Feature Engineering 
Before handing the dataset into the neural network, the data has to be flattened from a 28x28 grayscale image to a 784x1 array of number which represents the value of each pixel.

<img class = "ui medium floated left image" src = "../images/NeuronOptimization.png">

Of the 70,000 samples, 60,000 samples were used as a training set and the remaining 10,000 samples were considered the clean testing set. The clean testing set is important to analyze the neural network using data that it has never seen before. 

# Hyperparameter Optimization
The hyperparameters in a machine learning model are the set of numbers that can be changed to heighten the efficiency and quality of training within the model. The hyperparameters in the neural network include learning rate, batch size, max epochs, and hidden layer shape. Learning rate controls the magnitude of the weight adjustments for each epoch of training. The batch size determines the number of samples that the neural network trains on at a time. The max epochs determines the maximum number of times the neural network is trained. The hidden layer shape determines the number of neurons in the hidden layer. The learning rate was tuned between 0.01 and 1e-10 in intervals of a magnitude of 1/10. The batch size was tuned between 1 and 500 samples at a time in intervals of 10. The max epochs was tuned between 10 and 10000 epochs with intervals of 1000. The hidden layer shape was tuned between 1 and 29 neurons with intervals of 1.

The hyperparameters were optimized by hand, evaluating the cross entropy loss over time as the network trained. After trying each value for the hyperparameters, the best values were found. The best hyperparameters were found to be the following:
> Learning Rate: 1e-10

> Batch Size: 100

> Max Epochs: 6000

> Hidden Layer Shape: 25+

The learning rate of 1e-10 prevented the neural network from becoming unstable while training but allowed the weights to still be updated at a good enough pace to save time with epochs. The batch size turned out to be 100 simply because my system could not process any larger batch sizes. The best number of max epochs turned out to be 6000 as any epochs beyond that would not have a noticable effect on loss. Lastly, the number of hidden layers did not seem to significantly change the rate that the loss changed, but significantly increased the accuracy of the predictions as the number of neurons surpassed 25.

<img class = "ui medium floated right image" src = "../images/NeuronOptimizationPred.png">

# Evaluation
The neural network was able to successfully classify the sample 96% of the time. However, I observed some patterns: 
> High rates of confusion between the sandal (5th) class and the sneaker (7th) class. They would often get swapped with a higher bias to predict a sandal over a sneaker. 

> Confusion between the pullovers (2nd) class, coats (4th) class, and shirts (6th) class. But the networks with greater neurons begin to grow a stronger capability of telling the difference between these two. 

> Extreme accuracy in all the other classes which could be seen as overfitting.

# Neural Network Class
class NeuralNetwork():
    
    def __init__(self, inputs, hidden, outputs):
        """
        Initialize a simple neural network with a single hidden layer.
        This method randomly initializes the parameters of the model,
        saving them as private variables.
        
        Each layer is parameterized by a weight matrix and a bias vector; 
        a useful trick is store the weights and biases for a layer together,
        as a single matrix.
        
        Args:
            inputs: int, input dimension
            hidden: int, number of hidden neurons
            outputs: int, number of output neurons
        Returns:
            None
        """
        
        # Initialize the weights and biases of the neural network as
        # private variables. Store a weight matrix for each layer. 
        
        self.w1 = np.random.random((inputs, hidden))
        self.w2 = np.random.random((hidden, outputs))
        self.b1 = np.zeros((1, hidden))
        self.b2 = np.zeros((1, outputs))
        
    def loss(self, y_true, y_pred):
        """
        Compute categorical cross-entropy loss function. 
        
        Sum loss contributions over the outputs (axis=1), but 
        average over the examples (axis=0)
        
        Args: 
            y_true: NxD numpy array with N examples, D outputs (one-hot labels).
            y_pred: NxD numpy array with N examples, D outputs (probabilities).
        Returns:
            loss: array of length N representing loss for each example.
        """
        # WRITE ME
        
        lec = 1e-10
        return -np.mean(-y_true * np.log(np.clip(y_pred, lec, 1 - lec)) + (1 - y_true) * (1 - np.log(np.clip(y_pred, lec, 1 - lec)))) / y_pred.shape[0]
        
    def evaluate(self, X, y):
        """
        Make predictions and compute loss.
        Args:
            X: NxM numpy array where n-th row is an input.
            y: NxD numpy array with N examples and D outputs (one-hot labels).
        Returns:
            loss: array of length N representing loss for each example.
        """
        # WRITE ME
        
        return self.loss(y, self.predict(X))

    def predict(self, X):
        """
        Make predictions on inputs X.
        Args:
            X: NxM numpy array where n-th row is an input.
        Returns: 
            y_pred: NxD array where n-th row is vector of probabilities.
        """
        # WRITE ME
        
        if self.b1.shape[0] != X.shape[0]:
            self.b1 = np.zeros((X.shape[0], self.b1.shape[1]))
        if self.b2.shape[0] != X.shape[0]:
            self.b2 = np.zeros((X.shape[0], self.b2.shape[1]))
        
        self.h1 = relu(np.dot(X, self.w1) + self.b1) 
        #print("h1", self.h1, self.h1.shape)
        self.output_layer = np.dot(self.h1, self.w2) + self.b2
        y_pred = softmax(self.output_layer)
        #print("shape of neural network:", self.w1.shape, self.h1.shape, self.w2.shape, self.output_layer.shape)
        #print("predictions", self.output_layer, self.output_layer.shape)
        #print("sum of predictions", np.sum(self.output_layer, axis=1))
        return y_pred
        
    def train(self, X, y, lr=0.0001, max_epochs=10, x_val=None, y_val=None):
        """
        Train the neural network using stochastic gradient descent.
        
        Args:
            X: NxM numpy array where n-th row is an input.
            y: NxD numpy array with N examples and D outputs (one-hot labels).
            lr: scalar learning rate. Use small value for debugging.
            max_epochs: int, each epoch is one iteration through the train data.
            x_val: numpy array containing validation data inputs.
            y_val: numpy array containing validation data outputs.
        Returns:
            history: dict with the following key, value pairs:
                     'loss' -> list containing the training loss at each epoch
                     'loss_val' -> list for the validation loss at each epoch
        """
        # WRITE ME
        
        batch_size = 100
        history = {
            "loss": [],
            "loss_val": []
        }
        
        for i in np.arange(max_epochs):
            for b in np.arange(0, X.shape[0], batch_size):
                loss = self.evaluate(X[b : b + batch_size], y[b : b + batch_size])  
                #print("loss:", loss, loss.shape)
                if x_val is not None and y_val is not None:
                    loss_val = self.evaluate(x_val, y_val)
                    history.update({
                        "loss": np.append(history.get("loss"), loss),
                        "loss_val": np.append(history.get("loss_val"), loss_val)
                    })
                else:
                    history.update({
                        "loss": np.append(history.get("loss"), loss)
                    })

                w2_delta = (y[b : b + batch_size] - self.predict(X[b : b + batch_size]))
                #print("w2_delta:", w2_delta, w2_delta.shape)
                w1_delta = np.dot(w2_delta, np.transpose(self.w2))
                #print("w1_delta", w1_delta, w1_delta.shape)
                self.w2 += lr * np.dot(np.transpose(self.h1), w2_delta)
                self.b2 += lr * w2_delta
                self.w1 += lr * np.dot(np.transpose(X[b : b + batch_size]), w1_delta)
                self.b1 += lr * w1_delta
        
        return history
    
    def get_output(self):
        """
        Getter for private variable of interest
        
        Args:
            None
        Returns:
            output_layer: NxD array where n-th row is vector of probabilities.
        """
        return self.output_layer