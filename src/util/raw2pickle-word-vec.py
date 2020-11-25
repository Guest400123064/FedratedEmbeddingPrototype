import os, pickle, argparse
import numpy as	np


def _cli_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input"
        , help="Single embedding file, read in binary format"
        , type=str
    )
    parser.add_argument(
        "output"
        , help="Output embedding file in pickle format"
        , type=str
    )
    parser.add_argument(
        "-f", "--force"
        , help="Force overwrite if previous file exists."
        , action="store_true"
    )

    return parser


def _raw2pickle(fi, fo, force=False):

    dic_emb = dict()
    if (os.path.exists(fo) and not force):
        print(f"[ WARN ] :: Embedding <{fo}> file exists, "
               "skipped (use <-f> to overwrite)")
    else:
        print(f"[ INFO ] :: Reading raw embedding from <{fi}>")
        with open(fi, "rb") as f:
            for line in f:
                fields = line.split()
                w = fields[0].decode("utf-8")
                v = [float(x) for x in fields[1:]]
                dic_emb[w] = np.fromiter(v, dtype=np.float)

        print(f"[ INFO ] :: Dumping pickle embedding to <{fo}>")
        with open(fo, "wb") as f:
            pickle.dump(dic_emb, f, protocol=pickle.HIGHEST_PROTOCOL)

    return 0


if __name__ == "__main__":
    pars = _cli_parser()
    args = pars.parse_args()
    _raw2pickle(args.input, args.output, args.force)
