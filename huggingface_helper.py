# Huggingface : https://github.com/huggingface/transformers
# https://huggingface.co/transformers/preprocessing.html
import re

from transformers import AutoTokenizer


class huggingface_helper:
    def __init__(self, arabic_text, english_text):
        self.arabic_text = arabic_text
        self.english_text = english_text

    def tokenization(self):
        tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
        # Encode
        # We split the text by "," to get each sentence, we can use self.arabic_text as well
        encoded_inputs = tokenizer(self.english_text.split(","), padding=True, truncation=True, return_tensors="pt")
        print(encoded_inputs)
        # Decode
        for ids in encoded_inputs["input_ids"]:
            print(tokenizer.decode(ids))
