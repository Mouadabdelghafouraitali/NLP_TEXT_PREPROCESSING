import libs

from nltk_helper import nltk_helper
from huggingface_helper import huggingface_helper
from spacy_helper import spacy_helper

# SpaCy : https://github.com/explosion/spaCy
# https://iq.opengenus.org/text-preprocessing-in-spacy/

arabic_text = "ربما بدأ أحد أهم التطورات التي حققتها الرياضيات العربية في هذا الوقت مع عمل الخوارزمي ، أي بدايات " \
              "الجبر. من المهم أن نفهم مدى أهمية هذه الفكرة الجديدة. لقد كان ابتعادًا ثوريًا عن المفهوم اليوناني " \
              "للرياضيات ، والذي كان أساسًا الهندسة. كان الجبر نظرية موحدة سمحت بأن يتم التعامل مع الأرقام المنطقية " \
              "والأرقام غير المنطقية والمقادير الهندسية وما إلى ذلك على أنها أشياء جبرية. لقد أعطى الرياضيات مسارًا " \
              "جديدًا بالكامل للتطور أوسع بكثير من حيث المفهوم إلى ما كان موجودًا من قبل ، ووفر وسيلة للتطور " \
              "المستقبلي للموضوع. جانب آخر مهم لإدخال الأفكار الجبرية هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم " \
              "تحدث من قبل. "

english_text = "Perhaps one of the most significant advances made by Arabic mathematics began at this time with the " \
               "work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how " \
               "significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics " \
               "which was essentially geometry. Algebra was a unifying theory which allowed rational numbers, " \
               "irrational numbers, geometrical magnitudes, etc., to all be treated as algebraic objects. It gave " \
               "mathematics a whole new development path so much broader in concept to that which had existed before, " \
               "and provided a vehicle for the future development of the subject. Another important aspect of the " \
               "introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a way " \
               "which had not happened before"



print("*" * 10)
print("1 - NLTK")
print("2 - Huggingface")
print("3 - SpaCy")
print("*" * 10)
selected = int(input("Select one of the following : "))

if selected == 1:
    print("1 - Regular Expression")
    print("2 - Tokenization")
    print("3 - Character Encoding")
    print("4 - Part of Speech Tagging")
    print("5 - Chunking")
    print("6 - Stemming")
    print("7 - Lemmatization")
    nltk_obj = nltk_helper(arabic_text, english_text)
    selected_method = int(input("Select one of the following : "))
    if selected_method == 1: nltk_obj.regular_expression()
    if selected_method == 2: nltk_obj.tokenization(),
    if selected_method == 3: nltk_obj.character_encoding(),
    if selected_method == 4: nltk_obj.part_of_speech_tagging(),
    if selected_method == 5: nltk_obj.chunking(),
    if selected_method == 6: nltk_obj.stemming(),
    if selected_method == 7: nltk_obj.lemmatization()

if selected == 2:
    print("1 - Normal Tokenization")
    huggingface_obj = huggingface_helper(arabic_text, english_text)
    selected_method = int(input("Select one of the following : "))
    if selected_method == 1: huggingface_obj.tokenization()

if selected == 3:
    print("1 - Regular Expression")
    print("2 - Tokenization")
    print("3 - Character Encoding")
    print("4 - Part of Speech Tagging")
    print("5 - Chunking")
    print("6 - Stemming")
    print("7 - Lemmatization")
    spacy_obj = spacy_helper(arabic_text, english_text)
    selected_method = int(input("Select one of the following : "))
    if selected_method == 1: spacy_obj.regular_expression()
    if selected_method == 2: spacy_obj.tokenization(),
    if selected_method == 4: spacy_obj.part_of_speech_tagging(),
    if selected_method == 5: spacy_obj.chunking(),
    if selected_method == 6: spacy_obj.stemming(),
    if selected_method == 7: spacy_obj.lemmatization()
