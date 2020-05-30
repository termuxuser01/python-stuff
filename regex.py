import re

# re.search() returns match object if True and None if False
# we use raw strings as patterns to differentiate them from the pattren to be matched

print(re.search(r'LOG', 'LOGS'))
print(re.search(r'LOG', 'SOME LOG'))

print(re.search(r'LOG', 'NOT A MATCH'))

# match only at the start of the string
print(re.search(r'^LOG', 'LOG HERE'))
print(re.search(r'^LOG', 'SOME LOG'))

# only match at the end of the string

print(re.search(r'LOG$', 'SOME LOG'))
print(re.search(r'LOG$', 'SOME LOGS'))

# match numbers and dashes and return the mathced string

pattern = r'[0123456789-]+'
str1 = 'the phone number is 1234-567-890'

print(re.search(pattern, str1).group())

# match email
pattern = r'\S+@\S+'
str1 = 'my email is email.123@test.com'

print(re.search(pattern, str1).group())


# ^: Marks the start of the string
# $: Marks the end of the string
# \b: Marks the start or end of a word
# \S: Marks any character that's not a whitespace, including characters like * or $

# match a phone number using \d as a part of a group

pattern = r'the phone number is ([\d-]+)'
str1 = '37: the phone number is 1234-567-890'

match = re.search(pattern, str1)

print(match.group())
print(match.group(1))

# match yes or no case insensitive

pattern = re.compile(r'The answer to question (\w+) is (yes|no)', re.IGNORECASE)
str1 = 'Naturally, the answer to question 3b is YES'
# str1 = r'something that has nothing to do!'

match = pattern.search(str1)

if match:
    print(match.groups())
else:
    print('string did not match')

# match all pairs of cities with state abreviations, note that city names start with an uppercase, followed by a delimiting 
# character then two capital letters signifyin the state

pattern = re.compile(r'([A-Z][\w\s]+?).([A-Z]{2})')
str1 = 'the jackalopes are the team of Odessa,TX while the knights are native of Corvallis OR and the mud hens come from Toledo.OH; the whitecaps have their base in Grand Rapids,MI'

print(pattern.search(str1).groups())

# get all resaults
res = list(pattern.finditer(str1))

for x in res:
    print(x.group())


# \d: Marks any digit (0 to 9).
# \s: Marks any character that's a whitespace, including tabs and other whitespace special characters. Note that this is the reverse of \S, which was introduced in the previous recipe.
# \w: Marks any letter (this includes digits, but excludes characters such as periods).
# .: (dot): Marks any character.
# {n} match n repetitions

# The special characters can be reversed if they are case swapped. For example, the reverse of the ones we used are as follows:

# \D: Marks any non-digit.
# \W: Marks any non-letter.
# \B: Marks a position that's not at the start or end of a word. For example, r'thing\B' will match things but not thing.

# you can also give groups names which makes them easier to work with

pattern = re.compile(r'(?P<city>[A-Z][\w\s]+?).(?P<state>[A-Z]{2})')

match = pattern.search(str1)

print(match)

# get a dict with named matches
print(match.groupdict())

# get match by name
print(match.group('city'))

