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

#  EMAIL REGEX 
# This regex looks for email addresses

emailRegex = re.compile(r'''
(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    \.[a-zA-Z]{2,}          # .com .ca .org etc.
)
''', re.VERBOSE)

# Find all matches
phoneMatches = phoneRegex.findall(text)
emailMatches = emailRegex.findall(text)

# Store final results
allMatches = []

# Add phone numbers to list
for number in phoneMatches:
    allMatches.append(number[0])


# Add emails to list
for email in emailMatches:
    allMatches.append(email[0])

# Copy results back to clipboard
if len(allMatches) > 0:
    result = '\n'.join(allMatches)
    pyperclip.copy(result)