import re
import spacy
from collections import Counter

#from spacy_nlp_tools.simple_nlp import nlp


class spacy_helper:
    def __init__(self, arabic_text, english_text):
        self.nlp = spacy.load('en_core_web_sm')
        self.arabic_text = arabic_text
        self.english_text = english_text

    # Source : https://spacy.io/usage/rule-based-matching
    def regular_expression(self):
        doc = self.nlp(self.english_text)
        expression_en = r"[Ee](ssentially|\.?) ?[Gg](eometry|\.?)"
        expression_ar = r"[أ](ساسًا|\.?) ?[ا](لهندسة|\.?)"
        for match in re.finditer(expression_en, doc.text):
            start, end = match.span()
            span = doc.char_span(start, end)
            if span is not None:
                print("Found match:", span.text)

    # Source : https://spacy.io/usage/spacy-101#annotations-token
    def tokenization(self):
        doc = self.nlp(self.english_text)  # OR self.arabic_text
        for token in doc:
            print(token.text)

    # Source : https://spacy.io/usage/linguistic-features
    def part_of_speech_tagging(self):
        doc = self.nlp(self.english_text)  # OR self.arabic_text
        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                  token.shape_, token.is_alpha, token.is_stop)

    def chunking(self):
        doc = self.nlp(self.english_text)  # OR self.arabic_text
        # Analyze syntax
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
        # Find named entities, phrases and concepts
        for entity in doc.ents:
            print(entity.text, entity.label_)
        # OUTPUT : Noun phrases: ['the most significant advances', 'Arabic mathematics', 'this time', 'the work',
        # 'al-Khwarizmi', 'namely the beginnings', 'algebra', 'It', 'this new idea', 'It', 'a revolutionary move',
        # 'the Greek concept', 'mathematics', 'essentially geometry', 'Algebra', 'a unifying theory',
        # 'rational numbers', 'irrational numbers', 'geometrical magnitudes', 'algebraic objects', 'It',
        # 'mathematics', 'a whole new development path', 'concept', 'a vehicle', 'the future development',
        # 'the subject', 'Another important aspect', 'the introduction', 'algebraic ideas', 'it', 'mathematics',
        # 'itself', 'a way']
        # Verbs: ['make', 'begin', 'understand', 'be', 'allow', 'treat', 'give', 'exist',
        # 'provide', 'allow', 'apply', 'happen']
        # Arabic NORP
        # al-Khwarizmi GPE
        # Greek NORP

    def stemming(self):
        print(
            "spaCy doesn't contain any function for stemming as it relies on lemmatization only, reference : "
            "https://stackabuse.com/python-for-nlp-tokenization-stemming-and-lemmatization-with-spacy-library")

    # Source: http://www.nltk.org/api/nltk.stem.html?highlight=lemmatizer
    def lemmatization(self):
        doc = self.nlp(self.english_text)  # OR self.arabic_text
        for word in doc:
            print(word.text + '  ===>', word.lemma_)
        # OUTPUT :
        """Perhaps  ===> perhaps
        one  ===> one
        of  ===> of
        the  ===> the
        most  ===> most
        significant  ===> significant
        advances  ===> advance
        made  ===> make 
        by  ===> by
        Arabic  ===> arabic
        mathematics  ===> mathematic
        began  ===> begin
        at  ===> at
        this  ===> this
        time  ===> time
        with  ===> with
        the  ===> the
        work  ===> work
        of  ===> of
        al  ===> al
        -  ===> -
        Khwarizmi  ===> Khwarizmi
        ,  ===> ,
        namely  ===> namely
        the  ===> the
        beginnings  ===> beginning
        of  ===> of
        algebra  ===> algebra
        .  ===> .
        It  ===> it
        is  ===> be
        important  ===> important
        to  ===> to
        understand  ===> understand
        just  ===> just
        how  ===> how
        significant  ===> significant
        this  ===> this
        new  ===> new
        idea  ===> idea
        was  ===> be
        .  ===> .
        It  ===> it
        was  ===> be
        a  ===> a
        revolutionary  ===> revolutionary
        move  ===> move
        away  ===> away
        from  ===> from
        the  ===> the
        Greek  ===> greek
        concept  ===> concept
        of  ===> of
        mathematics  ===> mathematic
        ,  ===> ,
        which  ===> which
        was  ===> be
        essentially  ===> essentially
        geometry  ===> geometry
        .  ===> .
        Algebra  ===> Algebra
        was  ===> be
        a  ===> a
        unifying  ===> unifying
        theory  ===> theory
        that  ===> that
        allowed  ===> allow
        rational  ===> rational
        numbers  ===> number
        ,  ===> ,
        irrational  ===> irrational
        numbers  ===> number
        ,  ===> ,
        geometrical  ===> geometrical
        magnitudes  ===> magnitude
        ,  ===> ,
        etc  ===> etc
        .  ===> .
        ,  ===> ,
        to  ===> to
        all  ===> all
        be  ===> be
        treated  ===> treat
        as  ===> as
        algebraic  ===> algebraic
        objects  ===> object
        .  ===> .
        It  ===> it
        gave  ===> give
        mathematics  ===> mathematic
        a  ===> a
        whole  ===> whole
        new  ===> new
        development  ===> development
        path  ===> path
        so  ===> so
        much  ===> much
        broader  ===> broad
        in  ===> in
        concept  ===> concept
        to  ===> to
        that  ===> that
        which  ===> which
        had  ===> have
        existed  ===> exist
        before  ===> before"""

    """def word_frequency(self):
        doc = nlp(self.english_text)
        # remove stopwords and punctuations
        words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]
        word_freq = Counter(words)
        common_words = word_freq.most_common(len(self.english_text.split(' ')))
        print(common_words)
        # OUTPUT :
        [('important', 4), ('mathematics', 4), ('algebra', 2), ('new', 2), ('concept', 2), ('allowed', 2), 
        ('numbers', 2), ('algebraic', 2), ('development', 2), ('developments', 1), ('Arabic', 1), ('time', 1), 
        ('began', 1), ('work', 1), ('Al', 1), ('Khwarizmi', 1), ('i.e.', 1), ('beginnings', 1), ('understand', 1), 
        ('idea', 1), ('revolutionary', 1), ('departure', 1), ('Greek', 1), ('basis', 1), ('geometry', 1), 
        ('unification', 1), ('theory', 1), ('rational', 1), ('irrational', 1), ('geometric', 1), ('expressions', 1), 
        ('etc', 1), ('treated', 1), ('objects', 1), ('gave', 1), ('completely', 1), ('course', 1), ('broader', 1), 
        ('existed', 1), ('provided', 1), ('means', 1), ('future', 1), ('subject', 1), ('aspect', 1), ('introducing', 
        1), ('ideas', 1), ('applied', 1), ('way', 1)] """
