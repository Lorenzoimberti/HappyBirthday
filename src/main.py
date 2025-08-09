import datetime
import json
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = None
try:
    # Generate birthday message
    def wish_birth(name, personalized_text):
        if personalized_text:
            return personalized_text
        return f"Buon compleanno {name}"  # It's Italian :)

    # Reads JSON and filters by attributes (with int conversion check)
    def get_json_data(path, attr1, attr2, val1, val2):
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        filtered = []
        for item in data:
            try:
                # Convert to int for safe comparison
                val1_item = int(item.get(attr1, -1))
                val2_item = int(item.get(attr2, -1))
                if val1_item == val1 and val2_item == val2:
                    filtered.append(item)
            except (ValueError, TypeError):
                # Skip if not convertible to int
                continue
        return filtered

    print("Script running...")

    # Wait until there are birthdays today
    namev = []
    while True:
        now = datetime.datetime.now()
        namev = get_json_data("birthdays.json", "birth_month", "birth_date",
                              now.month, now.day)
        if namev:
            break
        time.sleep(60)  # Check every minute

    # Configure Selenium with Chrome profile
    chropt = webdriver.ChromeOptions()
    chropt.add_argument(r"--user-data-dir=YOUR_USER_DATA_DIR")

    service = Service(r"YOUR CHROMEDRIVER PATH")
    driver = webdriver.Chrome(service=service, options=chropt)

    driver.get("https://web.whatsapp.com/")
    # Wait until the page is ready, i.e., search bar is visible
    wait = WebDriverWait(driver, 30)
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))

    print("Contacts found:", [c['name'] for c in namev])

    # Send the message to each contact
    for contact in namev:
        try:
            contact_name = contact["name"]
            ele_nm = driver.find_element(By.XPATH, f'//span[contains(@title, "{contact_name}")]')
            ele_nm.click()

            time.sleep(1)

            # Find the chat input box
            ele_tf = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')

            # Determine the text to send
            message = wish_birth(
                contact.get("nickname") or contact.get("name"),
                contact.get("personalizedText")
            )

            # Send message plus Enter key
            ele_tf.send_keys(message + Keys.ENTER)
            time.sleep(2)

            print(f"Message sent to: {contact['name']}")

        except Exception as ex:
            print(f"Error with {contact.get('name')}: {ex}")
            continue

    print("All messages sent.")
finally:
    if driver:
        driver.quit()
