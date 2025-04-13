import json

option = input("How do you want to search via (atomic number / atomic name) ")



def elements():
    with open("elements.json") as f:
      elements_json = f.read()
    
    elements = json.loads(elements_json)
    if option == "atomic number":
        element_no = int(input("Enter the atomic number of the element you want to access: "))
        if element_no <= 118:
            print("The element is",elements[str(element_no)])
        else:
            print("Invalid atomic number")


    elif option == "atomic name":
        e_n = input("Enter element name ").title()
        e_symbol = input("Enter element symbol ").title()
        e_name = e_symbol + " " + e_n
       
        for e in iter(elements):
            
            if e_name ==elements[e]:
                x = e
        print("The atomic number is ",x)
        
    else:
        print("Invalid work")

elements()
