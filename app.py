from logger import tracker
from exceptions import user_inputs
from weather import search_weather, view_search_history, clear_history


print("-----------------------------")
print("  Welcome to Weather Client  ")
print("-----------------------------")

tracker.info("the system started!")

while True:

    print("1 Search wheather")
    print("2 view search history")
    print("3 clear History")
    print("4 exit")

    choice = user_inputs()

    if choice == 1:
        search_weather()
    elif choice == 2:
        view_search_history()
    elif choice == 3:
        clear_history()
    elif choice == 4:
        tracker.info("the user exit the application!")
        break
    