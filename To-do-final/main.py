from Mmenu import *
for _ in iter(lambda: True, False):
    #print("\n")
    menu=m_menu
    choice=menu()
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        reorder()
    elif choice == 4:
        remove()
    elif choice == 5:
        break
    else:
        print ("Try again")
