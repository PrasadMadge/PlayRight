# https://saucelabs.com/resources/articles/selenium-tips-css-selectors

# id is #
# XPath: //div[@id='example']
# CSS: #example

# element type
# Xpath: //input or
# Css: =input

# Direct Child >
# XPath: //div/a
# CSS: div > a

# Child or Sub-Child
# XPath: //div//a
# CSS: div a

# Class .
# XPath: //div[@class='example']
# CSS: .example

# next sibling
#  targetting the first sibling and then next to it.
# XPATH: //input[@id='username']/following-sibling:input[1]
# CSS: #username + input

# attribute value
# XPATH: //input[@name='username']
# CSS: input[name='username']

# attribute chaining
XPATH: //input[@name='login'and @type='submit']
CSS: input[name='login'][type='submit']

# nth child
# <ul id = "recordlist">
# <li>Cat</li>
# <li>Dog</li>
# <li>Car</li>
# <li>Goat</li>
# </ul>

#recordlist li::nth-of-type(4)
#recordlist li::nth-child(4)
#recordlist *::nth-child(4)

# Sub-String Matches

# ^= Match a prefix
# CSS: a[id^='id_prefix_']
# A link with an “id” that starts with the text “id_prefix_”

# $= Match a suffix
# CSS: a[id$='_id_sufix']
# A link with an “id” that ends with the text “_id_sufix”

# *= Match a substring
# CSS: a[id*='id_pattern']


