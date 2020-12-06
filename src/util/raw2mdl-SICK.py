import os, pickle, argparse
import numpy as	np
import pandas as pd


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

    if (os.path.exists(fo) and not force):
        print(f"[ WARN ] :: Corpus SICK <{fo}> file exists, "
               "skipped (use <-f> to overwrite)")
    else:
        print(f"[ INFO ] :: Reading raw SICK file from <{fi}>")
        dt_sick_raw = pd.read_csv(
            fi
            , sep='\t'
            , index_col=0
            , usecols=[
                "pair_ID"
                , "sentence_A"
                , "sentence_B"
                , "entailment_label"
                , "relatedness_score"
                , "SemEval_set"
            ]
        )

        print(f"[ INFO ] :: Dumping HDF5 SICK to <{fo}>")

    return 0


dt_sick_raw = pd.read_csv(
    "../../data/corpus/raw/SICK.txt"
    , sep='\t'
    , index_col=0
    , usecols=[
        "pair_ID"
        , "sentence_A"
        , "sentence_B"
        , "entailment_label"
        , "relatedness_score"
        , "SemEval_set"
    ]
)


if __name__ == "__main__":
    pars = _cli_parser()
    args = pars.parse_args()
    _raw2pickle(args.input, args.output, args.force)
