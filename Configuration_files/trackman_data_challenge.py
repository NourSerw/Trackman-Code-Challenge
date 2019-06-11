'''
File done by Nour Al-Rahman Al-Serw for Trackman's code challenge on the 11th of June 2019
'''

import json
import sys
import re
import string
import os.path

stack_array = []

# Main function
def main():
    global stack_array
    # At the moment I'm using a hardcoded json file to test the functionality
    query_file = "games.nulls"  # name of said file
    stack_array.append(query_file)
    # if check_if_exists(query_file):
    #     get_table_dependency(query_file)
    iterate_req()


# Function to check if the file exists
def check_if_exists(query_file):
    try:
        with open(query_file, 'r') as fh:
            return True
    except FileNotFoundError:
        return False


# Heavy work function to retieve the depencies
def get_table_dependency(query_file):
    global stack_array
    if (os.path.exists(query_file)):
        with open(query_file) as json_file:
            data = json.load(json_file)
            table_names = data['query']['L'][0]['M']['from']['S']
            # table_names = table_names.split(table_names," on ")[]
            table_names = table_names.split(" on ", 1)[0]
            array_of_from_query = re.split("\\s", table_names)
            for el in array_of_from_query:
                if "." in el:
                    el = el + ".json"
                    # if (check_if_exists(el)) :
                    #     stack_array.append(el.replace('.json', ''))
                    # else:
                    #     stack_array.pop(el)
                    stack_array.append(el.replace('.json', ''))
        # if check_if_exists(stack_array[-1] + ".json"):
        #     get_table_dependency(stack_array[-1] + ".json")
        # print(stack_array)
    else:
        print("leaf node")



def iterate_req():
    while(len(stack_array) != 0):
        element = stack_array.pop()
        print(element)
        get_table_dependency(element + '.json')


main()