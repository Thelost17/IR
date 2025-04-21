#AIM : TEXT SUMMARIZATION ALGORITHM

import nltk
nltk.download('punkt')  # Download necessary tokenizer data

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Sample text for summarization
text = """
Information Retrieval is a field concerned with searching for relevant documents
within a large dataset. Text summarization is the process of reducing a document's
length while maintaining its main points. Extractive methods identify and extract
key sentences, while abstractive methods generate summaries in their own words.
"""

# Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Summarize using LSA (Latent Semantic Analysis)
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 2)  # Number of sentences in summary

# Print the summary
print("Summary:")
for sentence in summary:
    print(str(sentence))
