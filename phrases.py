import sys
import os
sys.path.append(os.path.abspath("./model/"))
import Link
import Category
import Demo
import SettingsManager
import Entry


#import data
DATA_PATH = "./data/"
FILE_LIST = os.listdir(DATA_PATH)
#FILE_LIST.pop(0) #.DS_store
#print(FILE_LIST)

def load_entries():
    category_list = []
    for file in FILE_LIST:
        data = open(DATA_PATH + file).readlines()
        entry_list = []
        for line in data:
            line_split = line.split(",")
            #print(line_split)
            entry = Entry.Entry(line_split[0], line_split[1], line_split[2], line_split[3])
            entry_list.append(entry)
        category = Category.Category(file, entry_list)
        category_list.append(category)
    return category_list

category_list = load_entries()
print(len(category_list))




if __name__ == "__main__":
    #initialize some stuff
    settings = SettingsManager.SettingsManager()
    print(settings.getFluentLang())



    end = False
    message = ""
    while not end:
        command = input(message)

    def make_categories():
        categories = []
        for path in FILE_LIST:
            categories.append(Category("hi", 4))
        return categories
    


