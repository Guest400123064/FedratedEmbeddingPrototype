import os, pickle, argparse
import numpy as	np


def _cli_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input"
        , help="Single recipe, read in binary format"
        , type=str
    )
    parser.add_argument(
        "output"
        , help="Output corpus pickle file in standard structure"
        , type=str
    )
    parser.add_argument(
        "-f", "--force"
        , help="Force overwrite if previous file exists."
        , action="store_true"
    )

    return parser


def _raw2pickle(fi, fo, force=False):
    if (os.path.exists(fo) and not force):
        print(f"[ WARN ] :: Recipe-1M <{fo}> file exists, "
               "skipped (use <-f> to overwrite)")
    else:
        print(f"[ INFO ] :: Reading recipe from <{fi}>")
        rec, ing = np.array([], dtype=object), np.array([], dtype=object)
        with np.load(fi, allow_pickle=True) as raw_kb:
            rec, ing = raw_kb["recipes"], raw_kb["ingredients"]

        corpus = list()
        for r in rec:
            if (len(r) > 0):
                corpus.append(ing[r])
        corpus = np.array(corpus, dtype=object)
        
        print(f"[ INFO ] :: Dumping pickle recipe-1M to <{fo}>")
        with open(fo, "wb") as f:
            pickle.dump(corpus, f, protocol=pickle.HIGHEST_PROTOCOL)
        
    return 0

if __name__ == "__main__":
    pars = _cli_parser()
    args = pars.parse_args()
    _raw2pickle(args.input, args.output, args.force)
