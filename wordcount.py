from mrjob.job import MR
import re

word_regex = re.compile(r"\b\w+\b") #RE to findall words in a string

class analyze_MR(MR):


if __name__ == "__main__":
    analyze_MR.run()
