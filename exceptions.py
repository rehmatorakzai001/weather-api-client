from logger import tracker
def user_inputs():
    try:
        choice = int(input("enter your choice ").strip())
        tracker.info("choice entered!")
        return choice
    except ValueError:
        print("enter the correct value")
        tracker.warning(f"invalid input {choice} ")

def input_city():
    try:
        city_name = input("enter the city name: ").strip()
        tracker.info(f"city {city_name} is enterd ")
        return city_name
    except:
        print("the city is not exists: ")
        tracker.warning("City not exists!")