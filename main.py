"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Kopová
email: barborakopova20@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#Registered users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#Asking for username and password
username = input("username: ")
password = input("password: ")
print("-" * 40)

#Checking registered users
if username in users and users[username] == password:
    print("Welcome to the app,", username)

    #Choosing between 3 texts
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
    
    selection = input("Enter a number btw. 1 and 3 to select: ")
    print("-" * 40)

    #Checking inserted number
    if not selection.isdigit() or not (1 <= int(selection) <= 3):
        print("invalid input, terminating the program...")
        exit()

    selected_text = TEXTS[int(selection) - 1]

    #Counting and printing text statistics
    words = selected_text.split()
    word_count = len(words)
    titlecase_count = sum(1 for word in words if word.istitle())
    uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
    lowercase_count = sum(1 for word in words if word.islower())
    numeric_count = sum(1 for word in words if word.isdigit())
    numeric_sum = sum(int(word) for word in words if word.isdigit())

    print("There are ", word_count, "words in the selected text.")
    print("There are ", titlecase_count, "titlecase words.")
    print("There are ", uppercase_count, "uppercase words.")
    print("There are ", lowercase_count, "lowercase words.")
    print("There are ", numeric_count, "numeric strings.")
    print("The sum of all the numbers ", numeric_sum)
    print("-" * 40)

    #Counting lenghts of words
    word_lenghts = {}
    clean_words = [word.strip(".,!?") for word in words]

    for word in clean_words:
        lenght = len(word)
        word_lenghts[lenght] = word_lenghts.get(lenght, 0) + 1

    #Creating graph for word lenghts
    print("{:<3} | {:<15} | {:<2}".format("LEN", "OCCURENCES", "NR."))
    print("-" * 40)

    for lenght, count in sorted(word_lenghts.items()):
        print("{:<3} | {:<15} | {:<2}".format(lenght, "*" * count, count))

else:
    print("unregistered user, terminating the program...")
    exit()

