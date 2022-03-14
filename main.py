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

    if args.use_trained_model:
        train.loadModel()
    else:
        train.trainModel()
    
    test = Test(model=train.model, 
                oneHotEncoder=encoder,
                wordCache=train.wordCache,
                dataset=None)
    

    if args.test_file is not None:
        accuracies = []
        for file in args.test_file:
            test.dataset = Dataset(url=args.test_url, path=file)
            accuracy = test.performPredictionsFromTestDataset(printResults=args.print_results)
            accuracies.append(f"dataset {file}, accuracy: {(100 * accuracy):.2f}")
        for accuracy in accuracies:
            print(accuracy)
    else:
        test.performPredictionsFromSTDIN()
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--use_trained_model", action="store_true", help="Use already trained model")
    parser.add_argument("-mp", "--model_path", action="store", default="train.model", type=str, help="Model file path")
    parser.add_argument("-tp", "--train_path", action="store", default="train.txt", type=str, help="Train file path")
    parser.add_argument("-e", "--evaluation_test_path", action="store", default="diacritics-etest.txt", type=str, help="Evaluation Test file path")
    parser.add_argument("-d", "--development_test_path", action="store", default="diacritics-dtest.txt", type=str, help="Development Test file path")
    parser.add_argument("-url", "--test_url", action="store", default="https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl124/data", type=str, help="Test data url" )
    parser.add_argument("-tf", "--test_file", action="store", nargs='+', help="Test using input from atleast one file" )
    parser.add_argument("-a", "--all_tests", action="store_true", help="Perform tests on the development and evaluation test sets")
    parser.add_argument("-p", "--print_results", action="store_true", help="Print diacritisized result to standard output")

    args = parser.parse_args([] if "__file__" not in globals() else None)
    if args.all_tests:
        args.test_file = [args.evaluation_test_path, args.development_test_path]
    main(args)