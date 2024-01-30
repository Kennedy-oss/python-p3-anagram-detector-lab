# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        anagrams = []
        for candidate in words:
            candidate_lower = candidate.lower()
            if candidate_lower != self.word and sorted(candidate_lower) == self.sorted_word:
                anagrams.append(candidate)
        return anagrams

