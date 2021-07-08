import functools
import operator

import torchtext
import spacy
from nltk import word_tokenize, Counter
from torchtext.data import get_tokenizer


class pytorch_helper:

    def __init__(self, arabic_text, english_text):
        self.arabic_text = arabic_text
        self.english_text = english_text

    def nltk_tokenizer(self):
        return [token for token in word_tokenize(self.english_text)]

    # Source : https://www.programmersought.com/article/3642848944/
    def freq(self):
        TEXT = torchtext.legacy.data.Field(
            tokenize=get_tokenizer("basic_english"),
            lower=True,
            batch_first=True,
            init_token='<bos>',
            eos_token='<eos>',
            fix_length=len(self.english_text)
        )
        TEXT.build_vocab(word_tokenize(self.english_text))
        vocab = TEXT.vocab
        print(vocab.freqs)
