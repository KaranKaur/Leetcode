"""

Given two sentences words1, words2 (each represented as an array of strings), and
a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar,
and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

However, similarity is symmetric. For example, "great" and "fine" being similar is the
same as "fine" and "great" being similar.


Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence
like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].


#Time complexity is o(n+p) and space complexity is o(p),
where n = num of words to compare and p = num of word pairs.

"""

from collections import defaultdict

def similarity_words(words1, words2, pairs):
    if len(words1) != len(words2):
        return False
    words = defaultdict(set)
    for word1, word2 in pairs:
        words[word1].add(word2)
        words[word2].add(word1)

    for word1, word2 in zip(words1, words2):
        if word1 != word2 and word2 not in words[word1]:
            return False

    return True
