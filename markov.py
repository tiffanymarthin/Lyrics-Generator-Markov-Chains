class MarkovLyrics:
    def __init__(self):

        self.chain = {
            ""
        }

        self.chain = {}

    def populateMarkovChain(self, lyrics):
        for line in lyrics:
            words = line.split(" ")

            for i in range(len(words) - 1):
                word = words[i]

                if word in self.chain:
                    next_word = words[i + 1]
                    self.chain[word].append(next_word)
                else:
                    next_word = words[i + 1]
                    self.chain[word] = [next_word]

    def generateLyrics(selfself, length=500):
        n = self.

data = ["I am Tiffany", "I am an engineer", "I like to code"]
m = MarkovLyrics()
m.populateMarkovChain(data)
print(m.chain)