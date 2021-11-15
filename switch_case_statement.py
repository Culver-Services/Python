# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: Kessler Culver",
        "1009": "Employee Name: Mitch Chadwick",  
        "1010": "Employee Name: Dr. Patrick",
    }
    '''The first argument will be returned if the match found and
        nothing will be returned if no match found'''
    return switcher.get(ID, "nothing")

# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))
