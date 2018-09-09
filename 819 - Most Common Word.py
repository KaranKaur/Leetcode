"""

Given a paragraph and a list of banned words, return the most frequent word that
 is not in the list of banned words.  It is guaranteed there is at least one word
 that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.
 Words in the paragraph are not case sensitive.  The answer is in lowercase.

"""
import re
from collections import Counter
def most_comm_word(paragraph, banned):
    ban = set(banned)

    words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
    allowed = [word for word in words if word not in ban]
    return Counter(allowed).most_common(1)[0][0]

