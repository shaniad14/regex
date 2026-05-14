# Import modules
import re
import pyperclip

# Get text from clipboard
text = pyperclip.paste()

 #PHONE NUMBER REGEX 

phoneRegex = re.compile(r'''
(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-)?                 # separator
    \d{3}                   # first 3 digits
    (\s|-)                  # separator
    \d{4}                   # last 4 digits
)
''', re.VERBOSE)