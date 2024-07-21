import os


restaurant_list = []

def show_program_name():
    print("PRESS FLAVOR") 


def return_to_menu():
    input("\nPress Enter to return to the menu ")
    main()  


def show_subtitles(text):
    os.system('clear')
    print(text)
    print()


def invalid_option():
    show_subtitles('Invalid option!')
    return_to_menu()


def show_options():
    print("1. Register restaurant")
    print("2. List restaurants")
    print("3. Activate restaurant")
    print("4. Exit\n")


def register_restaurant():
    show_subtitles('Restaurant registration')
    restaurant_name = input('Enter with the retaurant name: ')
    restaurant_list.append(restaurant_name)
    print('Successsfully registered!')
    return_to_menu()


def list_restaurants():
    show_subtitles('Listing restaurants')
    for restaurant in restaurant_list:
        print(restaurant)
    return_to_menu()


def finishing_app():
    show_subtitles('Finishing app...')


def choose_option():
    try:
        chosen_option = int(input("Choose an option: "))
        match chosen_option:
            case 1:
                register_restaurant()
            case 2:
                list_restaurants()
            case 3:
                print("\nActivate restaurant")
            case 4:
                finishing_app()
            case _:
                invalid_option()
    except:
        invalid_option()


def main():
    os.system("clear")
    show_program_name()
    show_options()
    choose_option()


if __name__ == "__main__":
    main()
