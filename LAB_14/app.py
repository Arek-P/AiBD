from textblob import TextBlob
from typing import List

def hello(name):
    output = f'Hello {name}'
    return output


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    return word in text
    
def bubble_sort(lst: List[int]):
    
	l = len(lst)
	for i in range(l):
		change = False
		for j in range(l-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
				change = True
		if not change:
			return lst
	return lst
