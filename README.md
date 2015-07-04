PhraseDetector
==============

Detect phrases in text for fun and profit!

Usage
-----

PhraseDetector has one usage: to chunk text into phrases.

Dependencies
------------

* [Python](http://python.org)
* [NTLK](http://nltk.org)
* [Flask](http://flask.pocoo.org)

Installation
------------

```bash
git clone https://github.com/cuzzo/PhraseDetector.git
pip install -r PhraseDetector/requirements.txt
python -m nltk.download conll2000
```

Interacting with the REST Service
---------------------------------

First, run the service:

```bash
bin/www
```

For clarity, to interact with the service, I'll use [HTTPie](https://github.com/jkbrzt/httpie). To install, run `pip install httpie`.

The chunking endpoint takes one parameter `text` which is a [Penn Treebank](https://en.wikipedia.org/wiki/Treebank) POS-tagged string.

```bash
http GET localhost:5000 text=="I/PRP like/VBP NLP/NNP"
```

The service will respond with:

```
[["NP", [["I", "PRP"]]], ["VP", [["like", "VBP"]]], ["NP", [["NLP", "NNP"]]]]
```

Getting POS-Tagged Text
-----------------------

NLTK provides several ways to POS-tag text. But the best way is probably via [Stanford's POS Tagger](http://nlp.stanford.edu/software/tagger.shtml), which correctly guesses the part of speech for words right 90% of the time--even when the words are unknown!

To get started, I've written a [Node Service for Stanford's POS Tagger](https://github.com/cuzzo/node-stanford-postagger).

Acknowledgements
----------------

* [Jacob Perkins's Chunk Extraction with NLTK](http://streamhacker.com/2009/02/23/chunk-extraction-with-nltk/) - The core of this service comes directly from his articles.

License
-------

PhraseDetector is free--as in BSD. Hack your heart out, hackers.
