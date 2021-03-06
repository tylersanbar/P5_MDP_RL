# P5_supplement.py
# -----------
# Reference: this code base is adapted from ai.berkeley.edu, see the license information as follows:
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).



######################
# Student Information #
######################
## Write your name and your partner name here


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    #Prefer the close exit (+1), risking the cliff (-10)
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = -5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    #Prefer the close exit (+1), but avoiding the cliff (-10)
    answerDiscount = .3
    answerNoise = .2
    answerLivingReward = -2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #Prefer the distant exit (+10), risking the cliff (-10)
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = -2
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #Prefer the distant exit (+10), avoiding the cliff (-10)
    answerDiscount = .8
    answerNoise = .2
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #Avoid both exits and the cliff (so an episode should never terminate)
    answerDiscount = 1
    answerNoise = 0
    answerLivingReward = 200
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    #Epsilon 1 got as far as second tile on bridge
    #Epsilon 0 got stuck on first tile of bridge in loop
    answerEpsilon = None
    answerLearningRate = None
    return 'NOT POSSIBLE'
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import P5_supplement
    for q in [q for q in dir(P5_supplement) if q.startswith('question')]:
        response = getattr(P5_supplement, q)()
        print('  Question %s:\t%s' % (q, str(response)))
