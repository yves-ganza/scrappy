# Scrappy

An automated Outlook email sign-in with 2Factor authentication capabilities.

## How to run it?
Assumptions:
  - You have an outlook email account
  - You have 2Factor Authentication with sms enabled (Not really necessary but the script is capable of handling it)
  - You really want to know how this script works
  
Prerequisites:
  - Python 3.9
  - firefox browser - https://www.mozilla.org/en-US/firefox/new (Support for more coming soon)
  - geckodriver (https://github.com/mozilla/geckodriver/releases)
  - Packages (Provided)
  - .env file with 
     * EMAIL 
     * PASSWORD 
     * DIGITS - Last 4 digits of the phone number associated with the 2FA
     * SERVER_URL
  - You also need a server that's capable of sending and receiving sms (Contact me for more info ...)
