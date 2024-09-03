def m_menu():
    print ("1. Add Tasks\n2. View Tasks\n3. Re-order\n4. Remove Tasks\n5. Exit")
    x=int(input(">> "))
    return x
    
def add_task():
    task=str(input("Enter:\n"))
    try:
     with open('to_do_list.txt', 'a') as file:
        file.write(task + "\n")
    except IOError:
        print("Error: Could not write to the file.")
    print("\n")

def view_task():
    print ("***** Task Log *****")
    line_number = 1
    try:
        with open('to_do_list.txt', 'r') as file:
            for line in file:
                print(f"{line_number}. {line.strip()}")
                line_number += 1
    except IOError:
        print("Error: Could not read the file.")
    print ("\n********************")
        
def reorder():
    filename="to_do_list.txt"
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    task_no=int(input("\nEnter the task number: "))
    task = lines[task_no - 1]
    pos=int(input("\nEnter the order to be inserted at: "))
    lines.insert(pos, task + '\n')

    with open(filename, 'w') as file:
        file.writelines(lines)
    
    view_task()

def remove():
    filename = "to_do_list.txt"
    to_remove =int(input("Enter task no. to remove: "))
    print("\n")

    with open(filename, 'r') as file:  
        lines = file.readlines()

    del lines[to_remove - 1]

    with open(filename, 'w') as file:
        file.writelines(lines)
    view_task()