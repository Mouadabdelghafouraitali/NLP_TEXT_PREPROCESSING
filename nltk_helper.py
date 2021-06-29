import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


# NLTK : https://github.com/nltk/nltk


class nltk_helper:

    def __init__(self, arabic_text, english_text):
        self.arabic_text = arabic_text
        self.english_text = english_text

    # Source : https://www.nltk.org/book/ch03.html

    def regular_expression(self):
        # Find all words that ends with "ry"
        print(nltk.Text(nltk.word_tokenize(self.english_text)).findall(r"<.*ry>"))
        # Find all words that ends with "ة"
        print(nltk.Text(nltk.word_tokenize(self.arabic_text)).findall(r"<.*ة>"))

    # Break the text into words
    # Source : https://www.nltk.org/api/nltk.tokenize.html

    def tokenization(self):
        print(word_tokenize(self.english_text))
        print(word_tokenize(self.arabic_text))

    # There are a list of variable-width characters encoding such as utf-8, unicode_escape ...
    # Source : http://www.nltk.org/book_1ed/ch03.html

    def character_encoding(self):
        return print([word.encode('utf-8').decode() for word in nltk.word_tokenize(self.arabic_text)]
                     + [word.encode('utf-8').decode() for word in nltk.word_tokenize(self.english_text)])

    # A part-of-speech tagger, or POS-tagger, processes a sequence of words-
    # and attaches a part of the speech tag to each word
    # NOTE : arabic text will always return (NNP) which is proper noun, singular phrase
    # Source : https://www.nltk.org/book/ch05.html

    def part_of_speech_tagging(self):
        print(pos_tag(nltk.word_tokenize(self.english_text)))

    # The basic technique for entity detection is chunking, which segments and labels multi-token sequences This rule
    # says that an NP chunk should be formed whenever the chunker finds an optional determiner (DT) followed by any
    # number of adjectives (JJ) and then a noun (NN). Using this grammar, we create a chunk parser
    #  Source : https://www.nltk.org/book/ch07.html

    def chunking(self):
        # Meaning of DT, JJ and NN : https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(pos_tag(nltk.word_tokenize(self.english_text)))
        # e.g. mathematics/NNS ==> which mean the Mathematics word is plural
        print(result)

    # Stemming words and get it singular if the word is plural
    # Source : https://www.nltk.org/api/nltk.stem.html

    def stemming(self):
        porter = PorterStemmer()
        # NOTE : for the arabic text, we can use ARLSTem2 instead of PorterStemmer
        stemmed = [porter.stem(word) for word in word_tokenize(self.english_text)]
        print(stemmed)

    # Source: http://www.nltk.org/api/nltk.stem.html?highlight=lemmatizer

    def lemmatization(self):
        wnl = WordNetLemmatizer()
        lemmatized = [wnl.lemmatize(word) for word in word_tokenize(self.english_text)]
        # Unfortunately, the majority of words have been returned unchanged because they can't found in WordNet
        # Unfortunately, the arabic words is not found in WordNet either
        print(lemmatized)
