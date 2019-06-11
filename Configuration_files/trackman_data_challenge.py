'''
File done by Nour Al-Rahman Al-Serw for Trackman's code challenge on the 11th of June 2019
'''

import json
import sys
import re
import os.path

stack_array = []
depth = 0
ascii_tree = ''
query_file = str(sys.argv[1])


# Main function
def main():
    global stack_array
    stack_array.append((query_file, 0))
    iterate_req()


#Traversers through the json files and json tags to find the dependencies
def get_table_dependency(query_tuple):
    global stack_array #To disallow the creation of a local variable with the same name
    file_name = query_tuple[0]+'.json'

    if (os.path.exists(file_name)): #If loop to find if said file exists
        with open(file_name) as json_file:
            data = json.load(json_file)
            table_names = data['query']['L'][0]['M']['from']['S']
            # table_names = table_names.split(table_names," on ")[]
            table_names = table_names.split(" on ", 1)[0] #Remove text characters after the word on
            array_of_from_query = re.split("\\s", table_names)
            for el in array_of_from_query:
                if "." in el:
                    el = el + ".json"
                    newDepth = query_tuple[1] + 1 #Set the depth for the table(s)
                    stack_array.append((el.replace('.json', ''), newDepth))
                    # I used a stack as a data structure to store the tables and dependent tables with elements
                    # full of tuples. Each tuple has two elements: the table and the depth





def iterate_req():
    global ascii_tree
    while(len(stack_array) != 0):

        element = stack_array.pop()
        element_string = ''.join(element[0])
        if element[1] == 0:
            ascii_tree = element_string + '\n'
        else:
            ascii_tree += '\t' * element[1] + '|' + '\n'
            ascii_tree += '\t' * element[1] + '|' + '+' + element_string + '\n'

        get_table_dependency(element)


main()
file = open(query_file + ".txt", "w") #Write file to .txt file
file.write(ascii_tree)
file.close()
