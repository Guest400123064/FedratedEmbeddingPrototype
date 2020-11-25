import os, pickle
import numpy as	np


class WordEmbedding(object):

    UNK = "__UNK__"

    def __init__(self, fi):

        self._dic_tok_vec = dict()
        self._mat_tok_vec = np.array([], dtype=float)
        
        self._map_tok2idx = dict()
        self._map_idx2tok = np.array([], dtype=object)

        self._read_pickle(fi)
        self._proc_pickle()
        return

    def _read_pickle(self, fi):

        with open(fi, "rb") as f:
            self._dic_tok_vec = pickle.load(f)
            self._dic_tok_vec[self.UNK] = np.array(
                list(self._dic_tok_vec.values())
            ).mean(axis=0)
        return

    def _proc_pickle(self):

        self._mat_tok_vec = np.array(
            list(self._dic_tok_vec.values())
            , dtype=float
        )
        self._map_idx2tok = np.array(
            list(self._dic_tok_vec.keys())
            , dtype=object
        )
        self._map_tok2idx = dict(
            zip(self._map_idx2tok, 
                range(self._map_idx2tok.shape[0]))
        )
        return

    def tok2idx(self, w) -> int:
        
        return self._map_tok2idx.get(
            w, self._map_tok2idx.get(self.UNK)
        )

    def idx2tok(self, i) -> str:

        if (-1 < i and i < len(self._map_idx2tok)):
            return self._map_idx2tok[i]
        return self.UNK

    def get_emb_tok(self, w):

        return self._dic_tok_vec.get(
            w, self._dic_tok_vec.get(self.UNK)
        )

    def get_emb_idx(self, i):

        if (-1 < i and i < len(self._dic_tok_vec)):
            return self._mat_tok_vec[i, :]
        return self._dic_tok_vec.get(self.UNK)

    def to_matrix(self):

        return self._mat_tok_vec

    def to_dictionary(self):

        return self._dic_tok_vec
