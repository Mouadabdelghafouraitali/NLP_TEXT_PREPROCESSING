import re
import spacy


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
