#global
import argparse

#local
from Diacriticrestoration.train import Train
from Diacriticrestoration.test import Test
from Diacriticrestoration.dataset import Dataset
from Diacriticrestoration.OneHotEncoder import OneHotEncoder

def main(args):

    encoder = OneHotEncoder()

    train = Train(oneHotEncoder=encoder, dataset=Dataset(path=args.train_path), modelPath=args.model_path)

    if args.use_trained_model is not None:
        train.loadModel()
    else:
        train.trainModel()
    
    test = Test(model=train.model, 
                oneHotEncoder=encoder,
                wordCache=train.wordCache,
                dataset=None if args.test_from_file is None else Dataset(url=args.test_url, path=args.test_path))

    if args.test_from_file is not None:
        test.performPredictionsFromTestDataset()
    else:
        test.performPredictionsFromSTDIN()
        



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--use_trained_model", action="store", nargs='*', help="Use already trained model")
    parser.add_argument("--model_path", action="store", default="train.model", type=str, help="Model file path")
    parser.add_argument("--train_path", action="store", default="train.txt", type=str, help="Train file path")
    parser.add_argument("--test_path", action="store", default="diacritics-etest.txt", type=str, help="Test file path")
    parser.add_argument("--test_url", action="store", default="https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl124/data", type=str, help="Test data url" )
    parser.add_argument("-f", "--test_from_file", action="store", nargs='*', help="Test using input from a file" )

    args = parser.parse_args([] if "__file__" not in globals() else None)

    main(args)