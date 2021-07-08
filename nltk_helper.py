import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter
import pandas as pd


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

    def word_frequency(self):
        # sno = nltk.stem.SnowballStemmer('arabic') for the arabic text
        # Source : http://snowball.tartarus.org/
        english_snowball = nltk.stem.SnowballStemmer('english')
        arabic_snowball = nltk.stem.SnowballStemmer('arabic')
        # More info about Panda.DataFrame : https://www.geeksforgeeks.org/python-pandas-dataframe/
        english_data = pd.DataFrame(self.english_text.split(' '))
        arabic_data = pd.DataFrame(self.arabic_text.split(' '))
        words_english = english_data[0].apply(lambda x: english_snowball.stem(x))
        words_arabic = arabic_data[0].apply(lambda x: arabic_snowball.stem(x))
        print("English : {}".format(Counter(words_english)))
        print("Arabic : {}".format(Counter(words_arabic)))
        # OUTPUT :
        """English : 
        
        Counter({'of': 7, 'the': 7, 'to': 5, 'a': 5, 'mathemat': 4, 'it': 4, 'was': 4, 'which': 4, 
        'algebra': 3, 'signific': 2, 'this': 2, 'import': 2, 'new': 2, 'idea': 2, 'concept': 2, 'allow': 2, 'numbers,
        ': 2, 'be': 2, 'develop': 2, 'in': 2, 'that': 2, 'had': 2, 'perhap': 1, 'one': 1, 'most': 1, 'advanc': 1, 
        'made': 1, 'by': 1, 'arab': 1, 'began': 1, 'at': 1, 'time': 1, 'with': 1, 'work': 1, 'al-khwarizmi,': 1, 
        'name': 1, 'begin': 1, 'algebra.': 1, 'is': 1, 'understand': 1, 'just': 1, 'how': 1, 'was.': 1, 
        'revolutionari': 1, 'move': 1, 'away': 1, 'from': 1, 'greek': 1, 'essenti': 1, 'geometry.': 1, 'unifi': 1, 
        'theori': 1, 'ration': 1, 'irrat': 1, 'geometr': 1, 'magnitudes,': 1, 'etc.,': 1, 'all': 1, 'treat': 1, 
        'as': 1, 'objects.': 1, 'gave': 1, 'whole': 1, 'path': 1, 'so': 1, 'much': 1, 'broader': 1, 'exist': 1, 
        'before,': 1, 'and': 1, 'provid': 1, 'vehicl': 1, 'for': 1, 'futur': 1, 'subject.': 1, 'anoth': 1, 
        'aspect': 1, 'introduct': 1, 'appli': 1, 'itself': 1, 'way': 1, 'not': 1, 'happen': 1, 'befor': 1}) 
        
        Arabic : 
        Counter({'رياض': 4, '': 4, 'من': 4, 'كان': 4, 'تطور': 3, 'اهم': 2, 'مع': 2, 'مهم': 2, 'لقد': 2, 'مفهوم': 2, 
        'جبر': 2, 'سمح': 2, 'ارقام': 2, 'منطق': 2, 'الى': 2, 'على': 2, 'انه': 2, 'ربم': 1, 'بدء': 1, 'احد': 1, 
        'الت': 1, 'حقق': 1, 'عرب': 1, 'في': 1, 'هذا': 1, 'الو': 1, 'عمل': 1, 'خوارزم': 1, 'أي': 1, 'بدا': 1, 
        'جبر.': 1, 'أن': 1, 'نفهم': 1, 'مدى': 1, 'هذه': 1, 'فكر': 1, 'جديدة.': 1, 'ابتعاد': 1, 'ثور': 1, 'عن': 1, 
        'يونان': 1, 'والذ': 1, 'اساس': 1, 'هندسة.': 1, 'نظر': 1, 'موحد': 1, 'بان': 1, 'يتم': 1, 'تعامل': 1, 'غير': 1, 
        'مقادير': 1, 'هندس': 1, 'وما': 1, 'ذلك': 1, 'اشياء': 1, 'جبرية.': 1, 'اعطى': 1, 'مسار': 1, 'جديد': 1, 
        'كامل': 1, 'اوسع': 1, 'كثير': 1, 'حيث': 1, 'ما': 1, 'موجود': 1, 'قبل': 1, 'وفر': 1, 'سيل': 1, 'مستقبل': 1, 
        'موضوع.': 1, 'جانب': 1, 'اخر': 1, 'ادخال': 1, 'افكار': 1, 'هو': 1, 'تطبيق': 1, 'نفس': 1, 'طريق': 1, 'لم': 1, 
        'تحدث': 1, 'قبل.': 1}) 
 """
