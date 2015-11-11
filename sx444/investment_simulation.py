'''this module includes a class to generate the results of the investments and present them.'''
import matplotlib.pyplot as plt
import numpy as np
import re

class simulation(object):
      '''this class is to simulate the investment and generate the results '''

      def __init__(self, positions_str, num_trials):
          ''' this is a constructor that represents the positions'''

	  self.positions_str = positions_str 
	  position_list = re.findall(r'[0-9]+', self.positions_str)
	  position_numbers = []
          for i in range(len(position_list)): 
	      position = int(position_list[i])
              position_numbers.append(position)
	  self.positions = position_numbers
	 
	  # set the size of each investment
	  position_value = []
          for i in range(len(self.positions)):
              position_value.append(1000 / self.positions[i]) # set the size of each investment
	  self.position_value = position_value

          self.num_trials = int(num_trials)
          
      def simulate_one_day(self, position):
          '''this is to simulate the outcome of one day of investment'''
 	  cumu_ret = 0
	  for i in range(position): 
	      random_number = np.random.uniform(0, 1, 1)
	      if random_number <= 0.51:
                 cumu_ret = cumu_ret + (1000 / position) * 2
          return cumu_ret
              

      def repeat_and_present(self):
          '''this is to repeat the investment certain times and present the results''' 
 
          cumu_ret = np.zeros((len(self.positions), self.num_trials))
	  daily_ret = np.zeros((len(self.positions), self.num_trials))
	  for i in range(len(self.positions)):
	      for trial in range(self.num_trials):
              	  cumu_ret[i, trial] = self.simulate_one_day(self.positions[i])
                  daily_ret[i, trial] = (cumu_ret[i, trial] / 1000) - 1

          # start to write output
          output_file = open('results.txt', 'w') 
          for i in range(len(self.positions)):
	      # present the plots
	      plt.figure()
	      plt.title('Results of invest $1000 in instrument of $' + str(self.positions[i]))
	      plot_data = daily_ret[i, :]
	      plt.hist(plot_data, 100, range = [-1, 1])
	      plt.xlabel('Daily return')
  	      plt.ylabel('Frequency')
	      plt.gcf()
	      plot_filename = 'histogram plot results of $' + str(self.positions[i]) + '_pos.pdf'
	      plt.savefig(plot_filename)
	     
	      # present the mean and standard deviation
              means = np.mean(daily_ret[i, :])  # calculate the expected value of the daily return
              stds = np.std(daily_ret[i, :])  # calculate the standard deviation of the daily return
	      output_file.write("Position: " + str(self.positions[i]) + " mean: " + str(means) + " standard deviation: " + str(stds) + '\n')
          output_file.close()

