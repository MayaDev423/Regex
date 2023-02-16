# TODO: YOUR REGEX FUNCTIONS GO HERE
import re
#example - write function to recognize name
#capital letter followed by lowercase letters

def validate_variable(value):
    valueRE = re.compile('[a-zA-Z_]{1}[a-zA-Z0-9_]') #takes string and turns into regular expression. restrict to only one uppercase. 1 or more lowercase
    match = valueRE.match(value) #match value

    if match:
        return True
    else:
        return False


def validate_domain(value):
    valueRE = re.compile('([a-z]{1}[a-z0-9_]*[.]+)+[com|ca|org]')
    match = valueRE.match(value) 
    if match:
        return True
    else:
        return False

print(validate_domain('google.ca')       ) # True
print(validate_domain('smile.amazon.com')) # True
print(validate_domain('unicef.org')      ) # True
print(validate_domain('google.uk')       ) # False

def validate_phone(value):
    valueRE = re.compile('([0-9]{3}[-]{1})?([(]{1}[0-9]{3}[)]{1})?([0-9]{3}[-]{1}[0-9]{4})') 
    match = valueRE.match(value) #match value
    if match:
        return True
    else:
        return False

print(validate_phone('721-8668')     ) # True
print(validate_phone('905-721-8668') ) # True
print(validate_phone('(905)721-8668')) # True
print(validate_phone('9057218668')   ) # False
    
