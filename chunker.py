import nltk.chunk
import nltk.tag
import nltk.corpus
import itertools

def iob_train(chunk_sents):
    tag_sents = [nltk.chunk.tree2conlltags(tree) for tree in chunk_sents]
    return [[(t, c) for (w, t, c) in chunk_tags] for chunk_tags in tag_sents]

def get_iob_chunker():
   train_chunks = iob_train(nltk.corpus.conll2000.chunked_sents('train.txt'))
   u_chunker = nltk.tag.UnigramTagger(train_chunks)
   ub_chunker = nltk.tag.BigramTagger(train_chunks, backoff=u_chunker)
   return nltk.tag.TrigramTagger(train_chunks, backoff=ub_chunker)

class TagChunker(nltk.chunk.ChunkParserI):
    def __init__(self, chunk_tagger):
        self._chunk_tagger = chunk_tagger

    def parse(self, tokens):
        (words, tags) = zip(*tokens)
        chunks = self._chunk_tagger.tag(tags)
        wtc = itertools.izip(words, chunks)
        lines = [' '.join([w, t, c]) for (w, (t, c)) in wtc if c]
        return nltk.chunk.conllstr2tree('\n'.join(lines))

    def chunk(self, tokenized_str):
        tagged = [nltk.tag.str2tuple(t) for t in tokenized_str.split()]
        tree = self.parse(tagged)

        phrases = []
        for subtree in tree.subtrees():
            if subtree.label() == u'S':
                continue
            phrases.append([subtree.label(), subtree.leaves()])
        return phrases
