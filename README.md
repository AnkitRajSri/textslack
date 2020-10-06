# textslack
A text cleaning pipeline to perform text cleaning, along with additional functionalities for sentiment, pos extraction, and word count.

After pip install, please follow the below step to access the functionalities:
* from textslack import textslack

Below are the key functionalities currently available:

1. transform(text): normalises and cleans unstructured text
2. extract_nouns(text): cleans text to keep only nouns
3. extract_verbs(text): cleans text to keep only verbs
4. extract_adjectives(text): cleans text to keep only adjectives
5. extract_adverbs(text): cleans text to keep only adverbs
6. sentiment(text): returns a string as sentiment
7. word_occurances(word, text): returns frequency of a word mentioned in the text