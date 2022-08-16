---
layout: essay
type: essay
title: What are Neural Networks?
date: 2022-08
labels:
  - Machine Learning
  - Artificial Intelligence
summary: Since the creation of the computer in 1946, engineers have been innovating and improving on the basic design to the point where these computers are incomparable to those of the past. In the past, computers were considered to be tools to assist people in making complex calculations so that they might to their job better. In more recent years, we have developed computers to the point were we can expect them to do much more complex calculations. The most desirable of which is making decisions.
---

# Machines can Learn!
Since the creation of the computer in 1946, engineers have been innovating and improving on the basic design to the point where these computers are incomparable to those of the past. In the past, computers were considered to be tools to assist people in making complex calculations so that they might to their job better. In more recent years, we have developed computers to the point were we can expect them to do much more complex calculations. The most desirable of which is making decisions.

<img class="ui small floated left image" src="../images/eniac-computer.jpg" />

# Why is Machine Learning Important?
Intelligence is defined as the ability to gain and apply new skills and knowledge. For millennia humans have developed new skills and obtained new knowledge in the pursuit of better living standards in the world. People have learned to discovered forms of medicine, tricked rocks to think, and traveled to the moon. Imagine the limits that can be broken by computers. In the world, there are many things that we do that take years of practice, predicting whether a tumor is cancerous, driving through rush hour traffic, or defining all the possible solutions to a board game. Computers have allowed us to make these processes much faster and more reliable. From mammograms and x-rays to [bots](https://openai.com/five/) that beat professional video game players at their own game, computers have grown to do revolutionary things.

# How to Machines Learn?
Engineers have learned that nature can provide us with innovations like velcro which was created by [mimicking burrs of plants](https://www.microphotonics.com/biomimicry-burr-invention-velcro/). Computer engineering makes no exception. Humans have discovered mathematics and made computers that can do it much faster. Just as humans are able to quickly discover patterns in the world, computers should likewise recognize the patterns rapidly. 

<img class="ui small floated right rounded image" src="../images/honeycomb-pattern.jpg" />

Whether you know it or not, the patterns we see in the world are geometrically defined as a repeated sequence of numbers, shapes, colors, etc. Often these sequences are able to be described mathematically. That is where computers come in. By translating problems into an abstraction of math, we can make predictions using data collected from the problem. This abstraction allows computers use mathematical models to solve many different prediction based problems. So there we have it, the goal of modern machine learning (ML) is to find mathematical models that make good predictions. Essentially the same as statistics aside from some minor qualifications that I will not mention in this essay.

# A Deeper Dive
ML can be used to rapidly solve problems that scientists, engineers, doctors, and many other professionals might not be able to, or at least not as quickly. Take the example of a physician who gets a visit by a patient who is having issues breathing. This issue could be caused by tons of medical issues and a doctor will usually default to the patients medical history to assist with finding out what is wrong. If the medical history does not paint a clear enough picture, the doctor will continue to run further tests. These tests often include temperature and blood pressure readings, perhaps how often the patient has been coughing, the type of coughs they have, etc. From there, the doctor will make an estimate of what is affecting the patient. Using the same information as a doctor, the computer could generate a model and compare newly collected information to help classify what kind of illness the patient has. 

<img class="ui medium centered rounded image" src="../images/machine-learning-training.PNG" />

So what is the difference if the doctor and the computer still need to collect the same data? For the doctor, being able to diagnose patients with the correct ailment takes years of practice and experience to do at a high level, but the learning period for a computer is much shorter and cheaper.

# Then What is a Neural Network?
Before we can get into what a neural network is, we must first talk about the simpler approaches to ML. There are many types of ML models. They can be descibed under two umbrella terms, supervised and unsupervised. Supervised learning models use an approach defined by the use of labeled datasets while unsupervised models analyze and cluster unlabeled data. Within these two types, there are also subtypes defined by the problem they need to solve. Regression and classification problems are examples of problems that usually use supervised learning to solve. Unsupervised learning is generally used when clustering and associating data. Within these terms, there are many other terms that describe algorithms which solve the problem. These algorithms are things like [linear or logistic regression](https://towardsdatascience.com/introduction-to-regression-analysis-9151d8ac14b3#:~:text=In%20statistical%20modeling%2C%20regression%20analysis,%2C%20or%20'features'), [forest classifiers](https://towardsdatascience.com/understanding-random-forest-58381e0602d2), and [support vector machines](https://towardsdatascience.com/support-vector-machines-svm-c9ef22815589). Each of these algorithms are complex in their own right, but can be considered single neuron models. By stacking these single neuron models, we get an artificial neural network.

<img class="ui medium centered rounded image" src="../images/neural-network-essay.jpg" />

A complex combination of other calculations that work together to solve a problem. Neural networks can take many shapes and forms. One neural network that can be described easily is known as a simple neural network. The basic structure of a simple neural network is a set of input nodes known together as the input layer which connect to a set of secondary nodes known as a hidden layer. The hidden layer is then connected to the output layer, which is made of a set of nodes that provide an output to the user. Each of these nodes is connected to each other node in the adjascent layer with things called weights. The structure of neural networks vary greatly, but this is the simplest structure for a simple neural network. Neural network structures quickly become immensely complex as the network gains nodes and layers.

# Real World Examples
Throughout the world, machine learning is used in daily life. By speaking to Siri, watching Netflix, browsing the internet, and checking your Facebook, you are fueling the modern age of ML. Your data is being collected used to train models to help improve their understanding of the world and the people in it.
