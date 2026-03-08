
"""
I chose to use The Odyssey by Homer (Translated by Samuel Butler). I'm taking a mythology class, so this has been on my mind lately, and
it's a really good, classic story that's super fun!

Source: https://www.gutenberg.org/cache/epub/1727/pg1727.txt (132,604 words)

Note: Since this is the entire text, it takes a little while to process. I promise it's working!
"""

import operator

# Function to fetch data
def fetch_text(raw_url):
  """
  Imports the needed libraries and attempts to return a string of the text at the given url.
  
  :param:
  raw_url (string): The url of the desired text

  :return:
  String: A string copying the text at the url with a matching format.
  """
  import requests
  from pathlib import Path
  import hashlib

  CACHE_DIR = Path("cs_110_content/text_cache")
  CACHE_DIR.mkdir(parents=True, exist_ok=True)

  def _url_to_filename(url):
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return CACHE_DIR / f"{url_hash}.txt"

  cache_path = _url_to_filename(raw_url)

  SUCCESS_MSG = "✅ Text fetched."
  FAILURE_MSG = "❌ Failed to fetch text."
  try:
    if not cache_path.exists():
      response = requests.get(raw_url, timeout=10)
      response.raise_for_status()
      text_data = response.text
      cache_path.write_text(text_data, encoding="utf-8")
    print(SUCCESS_MSG)
    return cache_path.read_text(encoding="utf-8")

  except Exception as e:
    print(FAILURE_MSG)
    print(f"Error: {e}")
    return ""

# Save the URL in a variable
ODYSSEY_URL = "https://www.gutenberg.org/cache/epub/1727/pg1727.txt"

# Fetch the text
odyssey_text = fetch_text(ODYSSEY_URL)

# Statistics about the data
def print_text_stats(text):
  """
  Analyzes a text and prints the number of characters, lines, and words in it.
  
  :param: 
  text (string): A string containing the desired text

  :return:
  print : Number of Charachters
  print : Number of lines
  print : Number of words

  Example
  >>> print_text_stats(chapter)
  Number of characters: 998
  Number of lines: 18
  Number of words: 190
  """
  num_chars = len(text)

  lines = text.splitlines()
  num_lines = len(lines)

  num_words = 0
  for line in lines:
    words_in_line = line.split()
    num_words_in_line = len(words_in_line)
    num_words += num_words_in_line

  print(f"Number of characters: {num_chars}")
  print(f"Number of lines: {num_lines}")
  print(f"Number of words: {num_words}")

# Function to get word counts
def get_word_counts(text):
  """
  Analyzes a text and returns a dictionary with each word and the number of times it's written.
  
  :param: 
  text (string): A string containing the desired text

  :return:
  dictionary: A dictionary containing each word with its appearance count

  Example:
  >>> print(get_word_counts(string))
  ['word': 2, 'string' : 1, 'text': 3]
  """
  word_counts = {}
  lines = text.splitlines()
  for line in lines:
    words = line.split()
    for word in words:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
  return word_counts

# the print_top_10_frequent_words will call the above get_word_counts() and print only the top 10 frequent words.
def print_top_10_frequent_words(text):
    """
    Prints out the top ten most common words in the given text with the amount of times they show up. 
    
    :param:
    text (string): A string containing the desired text

    :return:
    Print: The top ten most frequent words and their counts, with one per line.

    Example: 
    >>> print_top_10_frequent_words(string)
    the: 18
    a: 16
    you: 15
    and: 13
    an: 12
    not: 10
    our: 7
    one: 6
    i: 6
    is: 4

    """
    word_counts = get_word_counts(text)
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_10_words = list(sorted_word_counts.items())[:10]  # Get the top 10 words and counts
    for word, count in top_10_words:
        print(f"{word}: {count}")


# this is a test print
print_text_stats(odyssey_text)

# get the word counts
#
"""

Using spaCy for advanced text processing

"""

import spacy

nlp = spacy.load('en_core_web_sm')

def word_tokenization_normalization(text):
    """
    Takes a given text and removes all stop words and de-conjugates all of it. 

    :param:
    text (string): A string containing the desired text

    :return:
    list: A list containing each word in the string with no stop words and no word modifications
    """
    text = text.lower() # lowercase
    doc = nlp(text)     # loading text into model

    words_normalized = []
    for word in doc:
        if word.text != '\n' \
        and not word.is_stop \
        and not word.is_punct \
        and not word.like_num \
        and len(word.text.strip()) > 2:
            word_lemmatized = str(word.lemma_)
            words_normalized.append(word_lemmatized)

    return words_normalized


def word_count(word_list):
    """
    Takes a list of words and counts how many times each one appears. 
    
    :param:
    word_list (list): a list of strings

    :return:
    dictionary: A dictionary with each word and the amount of times it shows up in the list

    :example:
    >>> print(word_count(list))
    {'list': 2, 'thing': 2, 'string': 1, 'word': 3}
    """
    word_counts = {}
    for word in word_list:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
    return word_counts


def print_top_15_frequent_words(word_counts):
    """
    Prints out the top 15 most common words in a dictionary with the amount of times it shows up

    
    :param: 
    word_counts (dictionary): A dictionary of strings and integers

    :return:
    print: The 15 most common words with the amount of times they appear

    Example:
    >>> print_top_15_frequent_words(dict)
    bennet: 15
    know: 14
    say: 11
    bingley: 11
    visit: 11
    dear: 10
    mrs: 9
    wife: 7
    girl: 7
    man: 6
    good: 6
    daughter: 6
    long: 6
    come: 6
    little: 5
    """
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_15_words = list(sorted_word_counts.items())[:15]  # Get the top 15 words and counts
    for word, count in top_15_words:
        print(f"{word}: {count}")

def get_locations(text):
   text = text.lower()
   doc = nlp(text)

   nouns = ""

   for t in doc.ents:
      if t.label_ in ["GPE", "LOC"]:
         nouns = nouns + t.text + " "
   return nouns

normalized_o = word_tokenization_normalization(odyssey_text)
word_counts = word_count(normalized_o)
print_top_15_frequent_words(word_counts)

print("-----")

locations = get_locations(odyssey_text)
print_top_10_frequent_words(locations)


"""
Top 15 Analysis

These seem to make sense! There's plenty of common non-stop words like man, come, say and go, which seems logical.
The word house shows up a lot more than I was expecting, but I think it comes from Odysseus (Ulysses in this translation) traveling around
to the domains, or houses, of different people and gods. Ulysses, the main character, shows up a total of over 500 times when you put him
and his typo name together! Ship makes a lot of sense, because the whole story is him travelling around the Mediterranean by boat. God also makes
sense, because he's in a mythological place, where gods are behind pretty much anything that happens. Son and father also make sense, because
there's a lot of themes like that throughout the story.

Extra Analysis Note

I decided to make my extra analysis finding the most common locations in the story, since it's all about him traveling to different places
trying to get home! It... didn't work super well. The code seems totally funcitonal, so I think spacy just got confused by the old-timey
writing from this several thousand year old story. It got a few right, like sea and egypt, but it also added things like Autolycus (a person)
and ambrosia (a food). It also put the united states in there a bumch of times, since the text includes a few things that aren't part of it,
so it's probably the credit's and foreword's fault. Multi-word locations also get counted as separate things. It works pretty well though!
"""