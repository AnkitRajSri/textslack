# textslack
A text cleaning pipeline to perform text cleaning, along with additional functionalities for sentiment, pos extraction, and word count.

After pip install, please follow the below step to access the functionalities:
* from textslack.textslack import TextSlack
* slack = TextSlack()

Below are the key functionalities currently available in the all the versions:

1. transform(text): normalises and cleans unstructured text
2. extract_nouns(text): cleans text to keep only nouns
3. extract_verbs(text): cleans text to keep only verbs
4. extract_adjectives(text): cleans text to keep only adjectives
5. extract_adverbs(text): cleans text to keep only adverbs
6. sentiment(text): returns a string as sentiment
7. word_occurances(word, text): returns frequency of a word mentioned in the text

v.0.1.2 update: transform method can now be used on an entire pandas dataframe column.

Please refer the below medium article for a detailed explanation of textslack functionalities.
https://medium.com/analytics-vidhya/text-processing-made-easy-with-textslack-4214ae6bc67a
