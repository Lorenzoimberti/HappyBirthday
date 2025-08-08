import datetime
import json
from selenium import webdriver
import time

eleNM = None

def wish_birth(name, personalizedText):
    if personalizedText is not None:
        return personalizedText
    #This is Italian :)
    return "Buon compleanno " + name



# use to return names of contacts having their birthday on current date.
def getJsonData(file, attr1, attr2, attr_val1, attr_val2):
    # Load the file's data in 'data' variable
    data = json.load(file)
    retv = []

    # If the attributes' value conditions are satisfied, 
    # append the name into the list to be returned.
    for i in data:
        if (i[attr1] == attr_val1 and i[attr2] == attr_val2):
            retv.append(i)
    return retv


# Opening the JSON file (birthdays.json) in read only mode.
data_file = open("birthdays.json", "r")
namev = []
print("Script Running")

# This function will keep rerunning at
# 11:59pm a day before the birthday and break out at 12:00am.
while True:
    try:
        datt = datetime.datetime.now()
        namev = getJsonData(data_file, "name", "birth_month", "birth_date",
                            str(datt.month), str(datt.day))

    except json.decoder.JSONDecodeError:
        continue
    if (namev != []):
        break

chropt = webdriver.ChromeOptions()

# adding userdata argument to ChromeOptions object
chropt.add_argument("user-data-<LOCATION TO YOUR CHROME USER DATA>")

# Creating a Chrome webdriver object
driver = webdriver.Chrome(executable_path="<LOCATION TO CHROME WEBDRIVER>",options=chropt)
driver.get("https://web.whatsapp.com/")

# delay added to give time for all elements to load
time.sleep(10)

print(namev)

# Finds the chat of your contacts (as in the namev list)
for inp in namev:
    try:
        eleNM = driver.find_element_by_xpath('//span[@title ="{}"]'.format(inp))
    except Exception as ex:
        print(ex)
        continue
    # Simulates a mouse click on the element
    eleNM.click()

    while (True):
        # Finds the chat box element
        eleTF = driver.find_element_by_class_name("_13mgZ")
        # Writes the message
        personalizedText = inp["personalizedText"]
        if (personalizedText is not None):
            eleTF.send_keys(wish_birth(None, personalizedText))
        else:
            nickname = inp["nickname"]
            if (nickname is not None):
                eleTF.send_keys(wish_birth(nickname, None))
            else:
                eleTF.send_keys(wish_birth(inp["name"], None))
        # Finds the Send button
        eleSND = driver.find_element_by_class_name("_3M-N-")
        # Simulates a click on it
        eleSND.click()
        break