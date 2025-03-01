# your code goes here!
class Anagram():
    def __init__(self,word):
        self.word=word.lower()
        self.sorted_word=sorted(self.word)

    def match (self,words):
        return [word for word in words if sorted(word.lower()) == self.sorted_word and word.lower() != self.word]

        pass
        pass

