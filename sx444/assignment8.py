'''author: Siyi Xie(sx444)'''
'''This is the main program to accept the input from users and call other modules to properly generate the results'''
   
import numpy as np
import matplotlib.pyplot as plt
import investment_simulation 
from user_defined_exceptions import *
import re

def conduct_simulation():
    '''this is to accept the input from the user, call other modules to generate the outputs'''

    while True:
        try:
    	    # accept the positions input from the user
	    positions_str = raw_input("You can choose the positions: (example: [1, 10, 100, 1000])")
	    if positions_str == 'quit':
	       return
	    if positions_str == '':  
	       raise Empty_Input_Error
	    break
	except Empty_Input_Error:
	    continue

    while True:
	try:
    	    # accept the number of trials input from the user
    	    num_trials = raw_input("how many times to randomly repeat the test? (example: 10,000)")
	    if num_trials == 'quit':
 	       return
	    if num_trials == '':
	       raise Empty_Input_Error 
	    break
        except Empty_Input_Error:
	    continue

    simulate = investment_simulation.simulation(positions_str, num_trials)
    simulate.repeat_and_present()
  

if __name__ == "__main__":
   try:
       conduct_simulation()
   except KeyboardInterrupt:
          pass
   except EOFError:
	  pass
   except TypeError:
	  pass
