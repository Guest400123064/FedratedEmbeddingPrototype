import os, pickle, argparse
import numpy as	np
import pandas as pd


def _cli_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input"
        , help="Single SICK raw file, read in .tsv format"
        , type=str
    )
    parser.add_argument(
        "output"
        , help="Output processed SICK file in .csv format"
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
        dt_sick = pd.read_csv(
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

        # Sentence to lowercase
        dt_sick["sentence_A"] = dt_sick["sentence_A"].str.lower()
        dt_sick["sentence_B"] = dt_sick["sentence_B"].str.lower()
        
        # Recode factors: 
        #   relationship direction & dataset partition
        dt_sick.replace(
            {
                "entailment_label": {
                    "CONTRADICTION": -1
                    , "NEUTRAL": 0
                    , "ENTAILMENT": 1
                },

                "SemEval_set": {
                    "TEST": 0
                    , "TRAIN": 1
                    , "TRIAL": 2
                }
            }
            , inplace=True
        )

        # Compute label from relatedness and direction
        #   Max score is 5, so normalize by dividing by 5
        dt_sick["similarity_label"] = (
            dt_sick["relatedness_score"] * dt_sick["entailment_label"]
        ) / 5.0

        # Save file in HDF format
        print(f"[ INFO ] :: Dumping processed .csv SICK to <{fo}>")
        dt_sick.to_csv(fo)

    return 0


if __name__ == "__main__":
    pars = _cli_parser()
    args = pars.parse_args()
    _raw2pickle(args.input, args.output, args.force)
