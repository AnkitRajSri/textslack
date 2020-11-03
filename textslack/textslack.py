import re
import pandas as pd
import nltk
nltk.download('brown')
nltk.download('names')
nltk.download('universal_tagset')
nltk.download('average_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, regexp_tokenize
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.corpus import stopwords
from textblob import TextBlob
import string
from collections import Counter
from normalise import normalise

from sklearn.base import TransformerMixin, BaseEstimator

class TextSlack(BaseEstimator, TransformerMixin):
    def __init__(self, variety='BrE', user_abbrevs={}, lang='english'):
        try:
            self.variety = variety
            self.user_abbrevs = user_abbrevs
            self.lang = lang
            if self.lang in stopwords.fileids() and self.lang in SnowballStemmer.languages:
                self.stop_words = stopwords.words(lang)
            else:
                raise LanguageNotFoundException('{} is currently not supported by textslack.'.format(self.lang), 'Keep checking for support in the future updates.')
            self.lemmatizer = WordNetLemmatizer()
            self.stemmer = SnowballStemmer(lang, ignore_stopwords=True)
            
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))
            
    def fit(self, X, y=None):
        return self

    def transform(self, X, *_):
        if isinstance(X, pd.Series):
            return X.apply(self._preprocess_text)
        elif isinstance(X, list):
            return [self._preprocess_text(x) for x in X]
        else:
            return self._preprocess_text(X)

    def _preprocess_text(self, text):
        if self.lang == 'english':
            normalised_text = self._normalise(text)
            normalised_text = re.sub(' +', ' ', normalised_text)
            words = regexp_tokenize(normalised_text.lower(), r'[A-Za-z]+')
            removed_punct = self._remove_punct(words)
            removed_stopwords = self._remove_stopwords(removed_punct)
            return self._lemmatize(removed_stopwords)
        else:
            words = word_tokenize(text.lower())
            removed_punct = self._remove_punct(words)
            removed_stopwords = self._remove_stopwords(removed_punct)
            return ' '.join([w for w in removed_stopwords])

    def _normalise(self, text):
        try:
            return ' '.join(normalise(word_tokenize(text), variety=self.variety, user_abbrevs=self.user_abbrevs, verbose=False))
        except:
            return text

    def _remove_punct(self, words):
        return [w for w in words if w not in string.punctuation]

    def _remove_stopwords(self, words):
        return [w for w in words if w not in self.stop_words and len(w)>1]

    def _lemmatize(self, words):
        return ' '.join([self.lemmatizer.lemmatize(w, pos='v') for w in words])
    
    def _stem(self, words):
        return ' '.join([self.stemmer.stem(w) for w in words])
    
    def extract_nouns(self, text):
        try:
            if self.lang == 'english':
                processed_text = self._preprocess_text(text)
                pos_tags, _ = self._blob_features(processed_text)
                return ' '.join([w for w, p in pos_tags if p == 'NN'])
            else:
                raise LanguageNotFoundException('Sorry for the inconvenience, textslack is still learning {}.'.format(self.lang), 'Keep checking for support in the future updates.')
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))
    
    def extract_verbs(self, text):
        try:
            if self.lang == 'english':
                processed_text = self._preprocess_text(text)
                pos_tags, _ = self._blob_features(processed_text)
                return ' '.join([w for w, p in pos_tags if p == 'VB'])
            else:
                raise LanguageNotFoundException('Sorry for the inconvenience, textslack is still learning {}.'.format(self.lang), 'Keep checking for support in the future updates.')
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))
      
    def extract_adjectives(self, text):
        try:
            if self.lang == 'english':
                processed_text = self._preprocess_text(text)
                pos_tags, _ = self._blob_features(processed_text)
                return ' '.join([w for w, p in pos_tags if p == 'JJ'])
            else:
                raise LanguageNotFoundException('Sorry for the inconvenience, textslack is still learning {}.'.format(self.lang), 'Keep checking for support in the future updates.')
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))
    
    def extract_adverbs(self, text):
        try:
            if self.lang == 'english':
                processed_text = self._preprocess_text(text)
                pos_tags, _ = self._blob_features(processed_text)
                return ' '.join([w for w, p in pos_tags if p == 'RB'])
            else:
                raise LanguageNotFoundException('Sorry for the inconvenience, textslack is still learning {}.'.format(self.lang), 'Keep checking for support in the future updates.')
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))
    
    def sentiment(self, text):
        try:
            if self.lang == 'english':
                processed_text = self._preprocess_text(text)
                _, polarity = self._blob_features(processed_text)
                return 'pos' if polarity > 0.0 else 'neg' if polarity < 0.0 else 'neu'
            else:
                raise LanguageNotFoundException('Sorry for the inconvenience, textslack is still learning {}.'.format(self.lang), 'Keep checking for support in the future updates.')
        except LanguageNotFoundException as e:
            print(str(e))
            print('Details: {}'.format(e.details))

    def _blob_features(self, text):
        blob = TextBlob(text)
        return blob.tags, blob.polarity
    
    def word_occurances(self, word, text):
        word_count_dic = dict(Counter([w for w in word_tokenize(text)]))
        return [c for w, c in word_count_dic.items() if w==word][0]
    
class LanguageNotFoundException(Exception):
    def __init__(self, message, details=None):
        self.message = message
        self.details = details
    def __str__(self):
        return str(self.message)