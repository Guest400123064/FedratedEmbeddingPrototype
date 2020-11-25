import numpy as np
from sklearn.decomposition import TruncatedSVD


def _weighted_avg(
    corpus_raw: np.ndarray
    , mat_word_vec: np.ndarray
    , mat_word_w: np.ndarray
) -> np.ndarray:

    n_samples = corpus_raw.shape[0]
    dim_emb = mat_word_vec.shape[1]
    corpus_emb = np.zeros((n_samples, dim_emb))
    for i, s, w in enumerate(zip(corpus_raw, mat_word_w)):
        corpus_emb[i, :] = (w.dot(mat_word_vec[s, :]) / 
            np.count_nonzero(w))

    return corpus_emb


def _corpus_pc(
    corpus_emb: np.ndarray
    , rm_npc: int=1
) -> np.ndarray:

    svd = TruncatedSVD(
        n_components=rm_npc
        , n_iter=7
        , random_state=0
    )
    svd.fit(corpus_emb)
    return svd.components_


def _remove_pc(
    corpus_emb: np.ndarray
    , rm_npc: int=1
) -> np.ndarray:

    pc = _corpus_pc(corpus_emb, rm_npc)
    return corpus_emb - corpus_emb.dot(pc.T).dot(pc)


def sif(
    corpus_raw: np.ndarray
    , mat_word_vec: dict
    , mat_word_w: dict
    , rm_npc: int
) -> np.ndarray:

    emb = _weighted_avg(corpus_raw, mat_word_vec, mat_word_w)
    if (rm_npc > 0):
        emb = _remove_pc(emb, rm_npc)
    return emb
