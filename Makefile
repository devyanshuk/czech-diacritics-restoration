DTEST = diacritics-dtest.txt
ETEST = diacritics-etest.txt
RM = rm -f

USE_TRAINED_MODEL = -u
TEST_ALL = -a
PYTHON = python3
EXEC_FILE = main.py

.PHONY: all clean

all: 
	$(PYTHON) $(EXEC_FILE) $(USE_TRAINED_MODEL) $(TEST_ALL)

clean: 
	$(RM) $(DTEST) $(ETEST)