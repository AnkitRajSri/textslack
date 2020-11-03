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

v.0.1.5 updates: 
1. transform method can now be used on a list and an entire pandas dataframe column.
2. textslack can perform basic text cleaning for some non-english languages as well, just pass the language while creating the object as shown below.
   
   slack = TextSlack(lang='spanish')

Please refer the below medium article for a detailed explanation of textslack functionalities.
https://medium.com/analytics-vidhya/text-processing-made-easy-with-textslack-4214ae6bc67a
