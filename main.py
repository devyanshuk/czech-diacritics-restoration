#global
import argparse
from Diacriticrestoration.OneHotEncoder import OneHotEncoder

#local
from Diacriticrestoration.train import Train
from Diacriticrestoration.test import Test
from Diacriticrestoration.dataset import Dataset

def main(args):

    encoder = OneHotEncoder()

    train = Train(oneHotEncoder=encoder, dataset=Dataset(path=args.trainPath), modelPath=args.modelPath)

    if args.useTrainedModel:
        train.loadModel()
    else:
        train.trainModel()
    
    test = Test(model=train.model, 
                oneHotEncoder=encoder,
                wordCache=train.wordCache,
                dataset=None if not args.testFromFile else Dataset(url=args.testUrl, path=args.testPath))

    if args.testFromFile:
        test.performPredictionsFromTestDataset()
    else:
        test.performPredictionsFromSTDIN()
        



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--useTrainedModel", nargs='?', default=None, help="Use already trained model")
    parser.add_argument("--modelPath", nargs='?', default="train.model", type=str, help="Model file path")
    parser.add_argument("--trainPath", nargs='?', default="train.txt", type=str, help="Train file path")
    parser.add_argument("--testPath", nargs='?', default="diacritics-etest.txt", type=str, help="Test file path")
    parser.add_argument("--testUrl", nargs='?', default="https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl124/data", type=str, help="Test data url" )
    parser.add_argument("--testFromFile", nargs='?', default=None, type=str, help="Test using input from a file" )

    args = parser.parse_args([] if "__file__" not in globals() else None)

    main(args)