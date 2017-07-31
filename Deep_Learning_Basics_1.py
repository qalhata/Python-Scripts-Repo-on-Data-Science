# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:58:38 2017

@author: Shabaka
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ''''''''''Coding the Forward Propagation (FP) Algorithm ''''''''#

weights = {'node_1': np.array([4, -5]), 'node_0': np.array([2, 4]),
           'output': np.array([2, 7])}

input_data = [3, 5]

# Calculate node 0 value: node_0_value
node_0_value = (input_data * weights['node_0']).sum()

# Calculate node 1 value: node_1_value
node_1_value = (input_data * weights['node_1']).sum()

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_value, node_1_value])

# Calculate output: output
output = (hidden_layer_outputs * weights['output']).sum()

# Print output
print(output, 'is the basic FP output from model')

# ''''''' Apply the Rectified Linear Activation Function '''''''''''''#

# NOTE: The activation function is very useful for tuning model weights ''#


def relu(input):
    '''Define relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(input, 0)

    # Return the value just calculated
    return(output)

# Calculate node 0 value: node_0_output
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)

# Calculate node 1 value: node_1_output
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_output, node_1_output])

# Calculate model output (do not apply relu)
model_output = (hidden_layer_outputs * weights['output']).sum()

# Print model output
print(model_output, 'is the FP_ReLU predicted quantity of transactions')


# ''''''''''' Apply Network to many observations/rows of data '''''''#

# Define predict_with_network()
def predict_with_network(input_data_row, weights):

    # Calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (weights['output'] * hidden_layer_outputs).sum()
    model_output = relu(input_to_final_layer)

    # Return model output
    return(model_output)


# Create empty list to store prediction results
results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))

# Print results
print(results)


# ''''''''''''' Behaviour of a Multi Layer Neural Network ''''''''#

def predict_with_network(input_data):
    # Calculate node 0 in the first hidden layer
    node_0_0_input = (input_data * weights['node_0_0']).sum()
    node_0_0_output = relu(node_0_0_input)

    # Calculate node 1 in the first hidden layer
    node_0_1_input = (input_data * weights['node_0_1']).sum()
    node_0_1_output = relu(node_0_1_input)

    # Put node values into array: hidden_0_outputs
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])

    # Calculate node 0 in the second hidden layer
    node_1_0_input = (hidden_0_outputs * weights['node_1_0']).sum()
    node_1_0_output = relu(node_1_0_input)

    # Calculate node 1 in the second hidden layer
    node_1_1_input = (hidden_0_outputs * weights['node_1_1']).sum()
    node_1_1_output = relu(node_1_1_input)

    # Put node values into array: hidden_1_outputs
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])

    # Calculate model output: model_output
    model_output = (weights['output'] * hidden_1_outputs).sum()

    # Return model_output
    return(model_output)

output = predict_with_network(input_data)
print(output)


# ''' Calculating Model Errors  - Consideration of weight effects''''###

# '''''''' Test Case - Bank Transactions Predictions '''''''##

# ''''''' Coding how weight changes affects accuracy ''''#'''''###
