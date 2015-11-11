'''this is for the user defined exceptions'''

class Empty_Input_Error(Exception):
      # for empty input error
      def __str__(self):
	  return "Invalid input"
