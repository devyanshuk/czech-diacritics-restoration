
### Czech language diacritics restoration using Python and sklearn

```
usage: main.py [-h] [-u] [-mp MODEL_PATH] [-tp TRAIN_PATH]
               [-e EVALUATION_TEST_PATH] [-d DEVELOPMENT_TEST_PATH]
               [-url TEST_URL] [-tf TEST_FILE [TEST_FILE ...]] [-a] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -u, --use_trained_model
                        Use already trained model
  -mp MODEL_PATH, --model_path MODEL_PATH
                        Model file path
  -tp TRAIN_PATH, --train_path TRAIN_PATH
                        Train file path
  -e EVALUATION_TEST_PATH, --evaluation_test_path EVALUATION_TEST_PATH
                        Evaluation Test file path
  -d DEVELOPMENT_TEST_PATH, --development_test_path DEVELOPMENT_TEST_PATH
                        Development Test file path
  -url TEST_URL, --test_url TEST_URL
                        Test data url
  -tf TEST_FILE [TEST_FILE ...], --test_file TEST_FILE [TEST_FILE ...]
                        Test using input from atleast one file
  -a, --all_tests       Perform tests on the development and evaluation test sets
  -p, --print_results   Print diacritisized result to standard output
```

#### Examples

1) ##### Use already trained model to perform all tests from file downloaded from the default URL and print results to stdout:

	```
	$ python3 main.py -u -a -p
	```

2)  ##### Use already trained model to perform tests from console input:

	```
	$ python3 main.py -u
	```

3) ##### Train a model and perform tests from a file downloaded from the default URL:

	```
	$ python3 main.py --test_file "diacritics-etest.txt"
	```
    
4) ##### Train a model form a given text file and test using a given text file and print diacritisized text:

	```
	$ python3 main.py --train_path="train.txt" --test_file "diacritics-etest.txt" -p
	```