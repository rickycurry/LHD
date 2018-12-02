import sys
import os
sys.path.append(os.path.abspath("./model/"))
import Link
import Category
import Demo
import SettingsManager
import Entry
from googletrans import Translator
import webbrowser


#import data
DATA_PATH = "./data/"
FILE_LIST = os.listdir(DATA_PATH)
#FILE_LIST.pop(0) #.DS_store
#print(FILE_LIST)

def load_entries():
    category_dict = {}
    for file in FILE_LIST:
        data = open(DATA_PATH + file).readlines()
        entry_list = []
        for line in data:
            line_split = line.split(",")
            #print(line_split)
            entry = Entry.Entry(line_split[0], line_split[1], int(line_split[2]), int(line_split[3]))
            entry_list.append(entry)
        entry_list.sort(key=lambda x: (x.up-x.down), reverse=True)
        category = Category.Category(file, entry_list)
        category_dict[category.title] = category
    return category_dict

category_dict = load_entries()
#print(category_dict["Greetings"].entries[0].transcript)

def translate(entry, settings):
    translator = Translator()
    #trans_obj = translator.translate(entry.transcript, dest="it").text
    trans_obj = translator.translate(entry.transcript, dest=settings.getFluentLang()).text
    return trans_obj

def print_entry(category_name, settings, num):
    category = category_dict[category_name]
    entry = category.entries[num]
    #print(entry.url)
    webbrowser.open_new(entry.url + "&modestBranding=1&rel=0" + "&showinfo=0")
    print(entry.transcript)
    print(translate(entry, settings))

def handle_command(command, settings, end):
    if command == "language":
        message = input("Please select a language to switch to: ")
        settings.setFluentLang(message)
        message = "Language switched to " + message + ". Please enter a command: "
    elif command == "upvote":
        message = "Your vote has been registered. Enter a command: "
    elif command == "downvote":
        message = "Your vote has been registered. Enter a command: "
    elif command == "quit" or command == "exit":
        message = "Goodbye!"
        end = True
    elif command == "greetings":
        print_entry("Greetings", settings, 0)
        message = input("Another? y/n ")
        if message == "y":
            print_entry("Greetings", settings, 1)
        message = "Enter a command: "
    elif command == "food":
        print_entry("Food", settings, 0)
        message = "Enter a command: "
    elif command == "weather":
        print_entry("Weather", settings, 0)
        message = "Enter a command: "
    elif command == "directions":
        print_entry("Directions", settings, 0)
        message = "Enter a command: "
    else:
        message = "Enter a command: "
    return settings, message, end


#print(translate(category_dict["Greetings"].entries[0], SettingsManager.SettingsManager()))

if __name__ == "__main__":
    #initialize some stuff
    settings = SettingsManager.SettingsManager()
    #settings.setFluentLang(input("Set default language: "))
    #print(settings.getFluentLang())


    end = False
    message = "Enter a command: "
    while not end:
        command = input(message)
        settings, message, end = handle_command(command, settings, end)

    quit()