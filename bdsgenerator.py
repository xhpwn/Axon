#!/usr/bin/env python2

'''
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +                                                                   +
    +    @Axon                                                          +
    +    @author Anubhav Saxena (xhpwn), |anubhav@saxena.xyz|           +
    +    @desc Generates datasets of biased data                        +
    +                                                                   +
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

import random

def weatherset(): # Generates weather data for 52 weeks 

def generate(biasRatio): # Generates data with specified biasRatio

    dataset = [0] * 0
    
    negative = 10 - biasRatio

    while negative > 0: # Appends 0s to datasets for negative outcomes 
        dataset.append(0)
        negative -= 1

    while biasRatio > 0: # Appends 1s to datasets for positive outcomes
        dataset.append(1)
        biasRatio -= 1

    random.shuffle(dataset)

    print dataset

# Test for randomly generated datasets with specific bias
def test():
    passed = 0
    tests, testScraper = 5, 5

    while testScraper > 0:
        if generate(5) != generate(5):
            passed += 1
        testScraper -= 1

    print "%d tests passed out of %d" % (passed, tests)

generate(4)
