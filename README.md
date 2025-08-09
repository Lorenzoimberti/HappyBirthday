WhatsApp Birthday Wishes Automation

This Python script automates sending birthday wishes via WhatsApp Web using Selenium.

Features
--------
- Reads a JSON file with contacts' birthdays.
- Checks daily for contacts who have birthdays on the current date.
- Sends personalized or default birthday messages automatically.
- Uses a custom Chrome profile to maintain WhatsApp Web login session.
- Handles message sending with simulated keyboard input.

Requirements
------------
- Python 3.7+
- Selenium (install via pip)
- ChromeDriver compatible with your Chrome version
- Google Chrome browser

Setup
-----
1. Clone this repository or copy the script file.

2. Prepare your birthdays.json file with the following structure:

[
  {
    "name": "John Doe",
    "nickname": "Johnny",
    "birth_month": 8,
    "birth_date": 10,
    "personalizedText": "Happy Birthday, John! Have a great day!"
  },
  {
    "name": "Jane Smith",
    "birth_month": 8,
    "birth_date": 10
  }
]

- personalizedText is optional. If missing, the script sends "Buon compleanno {name}".

3. Update the script with your Chrome user data directory and chromedriver.exe path:

chropt.add_argument(r"--user-data-dir=YOUR_USER_DATA_DIR")
service = Service(r"YOUR CHROMEDRIVER PATH")

Make sure your Chrome profile is already logged into https://web.whatsapp.com/.

Usage
-----
Run the script:

python whatsapp_birthday_wishes.py

The script waits until it finds contacts whose birthdays are today, then automatically sends messages.

Notes
-----
- The script waits for WhatsApp Web elements to load before interacting.
- After sending messages, it waits a few seconds to ensure delivery before closing the browser.
- The default birthday message is in Italian: "Buon compleanno {name}".

Troubleshooting
---------------
- Ensure chromedriver.exe version matches your Chrome browser.
- XPath selectors might need updates if WhatsApp Web UI changes.
- Keep WhatsApp Web session active in the specified Chrome user profile.

License
-------
This project is provided as-is for educational purposes.
