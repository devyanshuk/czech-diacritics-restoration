
### Czech language diacritics restoration using Python and sklearn

```
usage: main.py [-h] [-u [USE_TRAINED_MODEL [USE_TRAINED_MODEL ...]]]
[--model_path MODEL_PATH] [--train_path TRAIN_PATH]
[--test_path TEST_PATH] [--test_url TEST_URL]
[-f [TEST_FROM_FILE [TEST_FROM_FILE ...]]]

optional arguments:
-h, --help 			show this help message and exit
-u, --use_trained_model  	Use already trained model
--model_path MODEL_PATH 	Model file path
--train_path TRAIN_PATH 	Train file path
--test_path  TEST_PATH		Test file path
--test_url TEST_URL 		Test data url
-f, --test_from_file		Test using input from a file
```

#### Examples

1) ##### Use already trained model to perform tests from file downloaded from the default URL:

	```
	$ python3 main.py -u -f
	```

2)  ##### Use already trained model to perform tests from console input:

	```
	$ python3 main.py -u
	```

3) ##### Train a model and perform tests from file downloaded from the default URL:

	```
	$ python3 main.py --test_from_file
	```

4) ##### Train a model and perform tests from a text file:

	```
	$ python3 main.py --test_from_file --test_path="test.txt"
	```
    
5) ##### Train a model form a given text file and test using a given text file

	```
	$ python3 main.py --train_path="train.txt" --f --test_path="test.txt"
	```
