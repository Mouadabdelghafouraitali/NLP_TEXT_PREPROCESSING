# NLP_TEXT_PREPROCESSING
Text preprocessing using NLTK, Huggingface, and spaCy libraries.

Run the `main.py`, a list of choice will appear, select one of the following : 

1 - NLTK

2 - Huggingface

3 - spaCy


The `nltk_helper` class contain the following methods : 


`regular_expression():` There's a lot of regular expressions to test, but we went with one of them, this method will return all English words that end with "ry" and all Arabic words that end with "ة".

`tokenization():` Break the English and Arabic text into words

`character_encoding():` Encoding text with the utf-8 as variable-width characters encoding

`part_of_speech_tagging():` A part-of-speech tagger, or POS-tagger, processes a sequence of words and attaches a part of the speech tag to each word
NOTE: Arabic text will always return (NNP) which is a proper noun, singular phrase, if you want to understand what each speech tag mean, please visit :  https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

`chunking():` Chunking is a process of extracting phrases from unstructured text, which means analyzing a sentence to identify the constituents(Noun Groups, Verbs, verb groups, etc.)

`stemming():` Stemming words and get the word singular if it is plural

`lemmatization():` Process of grouping together the different inflected forms of a word, so they can be analyzed as a single item.


----------------------

The `huggingface_helper` class contain the following methods : 


`tokenization():` Break the English and Arabic text into words

(Work with this library is still in progress)

----------------------

The `spacy_helper` class contain the following methods : 

This class contains the same methods as `nltk_helper` have, but using spaCy library instead of nltk
Note : spaCy doesn't contain any function for stemming as it relies on lemmatization only.
Source : "https://stackabuse.com/python-for-nlp-tokenization-stemming-and-lemmatization-with-spacy-library

