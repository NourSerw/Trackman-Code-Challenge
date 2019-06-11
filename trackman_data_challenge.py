'''
File done by Nour Al-Rahman Al-Serw for Trackman's code challenge on the 11th of June 2019
'''


#Main function
def main():
    #At the moment I'm using a hardcoded json file to test the functionality
    query_file = "./Configuration_files/games.nulls.json" #name of said file
    check_if_exists(query_file)


#Function to check if the file exists
def check_if_exists(query_file):
    try:
        with open(query_file, 'r') as fh:
            print("File exists")
            return True
    except FileNotFoundError:
        print("File not found")
        return False

main()