def language_input():
    """
    This function will allow the user to select a language that the program will communicate in
    """
    language = int(input("Please select a language from the following options: \n"
                         "1. English \n"
                         "2. Français \n"
                         "3. Español \n"))
    while language < 1 or language > 3:
        language = int(input("Invalid choice. Please select a language from the following options: \n"
                             "1. English \n"
                             "2. Français \n"
                             "3. Español \n"))
    return language


def name_input(language):
    """
    This function requests a user to enter their name via an input prompt based on their selected language
    """
    if language == 1:
        user_name = input("Please enter your name: ")
        print("Hello " + user_name + "! How are you today?")
    elif language == 2:
        user_name = input("S'il vous plaît entrez votre nom: ")
        print("Bonjour " + user_name + "! Comment vas-tu aujourd'hui?")
    elif language == 3:
        user_name = input("Por favor, escriba su nombre: ")
        print("Hola " + user_name + "! Como estas hoy?")
    return user_name


name_input(language_input())