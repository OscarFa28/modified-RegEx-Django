# modified-regEx-Django
This is a modified version of RegEx in a full-stack Django project.
Users will be able to upload their .txt file through the Django app's web interface, and this file will be read and used for the operations.
This version includes the following operations:

abcd: Simple search.
[a-z]bc, a[C-H]d, [4-7]34: Letter and number ranges within square brackets.
[abgs]cd, a[gd], df[ds]fa: Sets of letters within square brackets.
*: Wildcard valid for any letter. For example, ab*d matches any string like "abad," "abbd," "abcd," etc.
ab?cd: The letter immediately before the "?" sign may or may not appear in the found match.
abc | fg*i: The "|" operator functions as a logical "or." The text can match either the left or the right string.
a{5}cd: Repetition operator. The letter "a" repeats 5 times, resulting in the pattern "aaaaacd."
It offers the option to "search" and "search and replace." Additionally, it incorporates two flags, i.e., "g" and "i."

If the "g" flag is set, it means that the search or search and replace operation should be performed for all matches within the text, not just the first one.
If the "i" flag is set, it means that our operations will be case-insensitive, i.e., they will treat uppercase and lowercase letters equally.
To simplify, only one operator will be used per query, except for the "|" operator, where each string can have its operator. Also, queries will only use alphanumeric characters, i.e., a-z, A-Z, 0-9.
