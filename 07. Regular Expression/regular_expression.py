# Write  a program to find check if a string has only octal digits. Given string ['789','123','004']

import re
sent = ['789', '123', '004']
patt = r'^[0-7]+$'
for s in sent:
    if re.match(patt, s):
        print(f"{s} is an octal digit")
    else:
        print(f"{s} is not an octal digit")


# Extract the user id, domain name and suffix from the following email addresses.
# emails  =  """zuck@facebook.com
# sunder33@google.com
# jeff42@amazon.com"""

import re 
email = input("Enter email addresses: ")
patt = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'
matches = re.findall(patt, email)
for match in matches:
    user_id, domain, suffix = match
    print(f"User ID: {user_id}, Domain: {domain}, Suffix: {suffix}")


# Split the following irregular sentence into proper words
# sentence = """A, very   very; irregular_sentence"""  
# expected outout : A very very irregular sentence

import re
sentence = input("Enter a sentence: ")
patt = r'[^\w\s]+|\_+|\s+'
words = re.split(patt, sentence)
words = [word for word in words if word]
print(" ".join(words))

# Clean up the following tweet so that it contains only the user’s message. That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# desired_output = 'Good advice What I would do differently if I was learning to code today'

import re
tweet = input("Enter a tweet: ")
patt = r'RT\s+@[\w]+:|cc:\s+@[\w]+|https?://\S+|#\w+|@\w+|[^\w\s]'
cleaned_tweet = re.sub(patt, '', tweet)
cleaned_tweet = re.sub(r'\s+', ' ', cleaned_tweet).strip()
print(cleaned_tweet)

'''
Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Code to retrieve the HTML page is given below:
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text  # html text is contained here
desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 
'This is a new sentence without a paragraph break, in bold italics.']
'''

import re
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text
patt = r'>([^<]+)<'
matches = re.findall(patt, html_text)
matches = [match.strip() for match in matches if match.strip()]
print(matches)

'''
Given below list of words, identify the words that begin and end with the same character. 
civic
trust
widows
maximum
museums
aa
as
'''

import re
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
patt = r'^(?P<first_char>\w).*(?P=first_char)$'
matching_words = [word for word in words if re.match(patt, word)]
print("Words that begin and end with the same character:", matching_words)