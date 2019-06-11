# Trackman Code Challenge

This is the README file as intended by the requirements and is divided into three sections.

Description of approach taken:

The approach taken has been divided into three parts which are:
	1. Create a function to check if the file given to said script does exist within the directory or not.
	2. If it does exists then parse the JSON file using the json python library down to the "from tag".
	3. Using recursive methods try and find every dependency of tables found using a stack.

Language used: Python 3.7

Instructions on how to use:
	1. Make sure the script is in the same directory as the .json files.
	2. Navigate to the folder containing both the .json files and the script
	3. Run the python file and pass in the argument with it as well. So for example it will look something like this 
		"python trackman_data_challenge.py games.nulls"

Then a .txt file will appear on the same directory with the ascii written inside of it.
