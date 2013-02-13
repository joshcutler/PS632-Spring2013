# Web scraping

Today we're working with web scraping tools, and Beautiful Soup in particular. We'll use two political examples: election ads and White House petitions. 

The [White House petition site](https://petitions.whitehouse.gov/petitions) is actually [open source](https://github.com/WhiteHouse/petitions). 

Make sure everyone understands:

- loops
- accessing the web page
- `clean_html`
- `re.search()`
- opening and closing a CSV 

# Regular expressions

The Python documentation has a [helpful guide](http://docs.python.org/2/howto/regex.html) on regexp but it's a little complicated for beginners.

The main things to take away from it are the explanation of metacharacters and:

- `\d` Matches any decimal digit; this is equivalent to the class `[0-9]`.
- `\D` Matches any non-digit character; this is equivalent to the class `[^0-9]`.
- `\s` Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.
- `\S` Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.
- `\w` Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`.
- `\W` Matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`

Another useful list is [here](http://www.upriss.org.uk/python/session7.html):

- `.`  Any single character except a newline
- `^` The beginning of the line or string
- `$`  The end of the line or string
- `*`  Zero or more of the last character
- `+`  One or more of the last character
- `?`  Zero or one of the last character
- `{5,10}`   Five to ten times the previous character
