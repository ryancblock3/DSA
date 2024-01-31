# Strings

## String Slicing

index is an integer matching a specifc position in a strings sequence of characters.

index starts at 0

Slice Notation - my_str[start:end]

my_str = 'Boggle'

my_str[0:3] = 'Bog' - Notice how the second g isnt added becuase it will return index 0, 1, and 2. Ends at string 3

Negative numbers can alsso be use 

my_str = 'Jane Doe?!'
my_str[0:-2] = 'Jane Doe' removing the last two characters

Python creates a new string object when slicing, does not change the value of the original string.

Variables can be uses in place of literals
my_string[x:y]


my_str is 'http://en.wikipedia.org/wiki/Nasa/'
| Expression            | Result                                    | Description                                       |
|------------------------|-------------------------------------------|---------------------------------------------------|
| `my_str[10:19]`        | `wikipedia`                               | Returns the characters in indices 10-18.          |
| `my_str[10:-5]`        | `wikipedia.org/wiki/`                     | Returns the characters in indices 10-28.          |
| `my_str[8:]`           | `n.wikipedia.org/wiki/Nasa/`              | Returns all characters from index 8 until the end.|
| `my_str[:23]`          | `http://en.wikipedia.org`                  | Returns every character up to index 23.           |
| `my_str[:-1]`          | `http://en.wikipedia.org/wiki/Nasa`        | Returns all but the last character.               |

Slice notation also provides for a third argument known as the stride

Stride determines incrementation of the index after reading each element.

## Advanced String Formatting

Field Width - Defines the minumum number of characters that must be inserted into the string

{name:16}

Alignment Character determind how a value should be aligned within the width of the field

![img of string alignmnets](./images/Screenshot%202024-01-31%20at%204.13.09 PM.png)

Fill Character is used to pad a replacement field when the inserted string is smaller than the field width.

![using fill characters to pad tables](./images/Screenshot%202024-01-31%20at%204.17.48 PM.png)

Floating-point precision is used when you need to set the precision of a floating-point number

f'{1.725:.1f} indicates a precision of 1 so the resulting string would be 1.7

## String Methods

replace(old, new) - returns a copy of the string with all occurrences of the substring old replaced by the new.

replace(old, new, count) only replaces the first count occurences of old.

find(x) - returns the index of the first occurence of item x in the string

find(x, start) - same as find x but begins index start

find(x, start, end) - same as above but also define ending point

rfind(x) - same as find(x) but searches in reverse

count(x) - returns the number of times x occurs in the string

String can be compared using relational operators such as <, <=, >, and >= as well as equality operatiors such as == and != and membership operators (in, not in) and idenity operators (is, is not)

isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.

isdigit() -- Returns True if all characters are the numbers 0-9.

islower() -- Returns True if all cased characters are lowercase letters.

isupper() -- Returns True if all cased characters are uppercase letters.

isspace() -- Returns True if all characters are whitespace.

startswith(x) -- Returns True if the string starts with x.

endswith(x) -- Returns True if the string ends with x.

capitalize() -- First character capatalized the rest remain the same

lower() -- all character lowercased

upper() -- all characters uppercased

strip() -- returns the string with leading and trailing whitespace removed

title() -- first letter of each word capitalized

## Splitting and Joining Strings

split() splits a string into a list of tokens where each token is a substring that formas a part of a larger string

A separator is a character or sequence of characters that indicats where to split the string into tokens.

join() string method performs the inverse of split by joining a list of string to create a single string.