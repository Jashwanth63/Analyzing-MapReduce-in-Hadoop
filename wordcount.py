from mrjob.job import MRJob as MR
import re

word_regex = re.compile(r"\b\w+\b") #RE to findall words in a string

class analyze_MR(MR):
    def mapper(self, _, line):
        diff_words = word_regex.findall(line)
        for words in diff_words:
            yield(words.lower(), 1)
    def reducer(self, words, counts):
        yield(words, sum(counts))


if __name__ == "__main__":
    analyze_MR.run()
