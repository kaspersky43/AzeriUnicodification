# AzeriUnicodification
Original URL: https://www.kaggle.com/c/azerbaijani-unicodification

How this works:

First run main1.py to train the model--from input.csv to create dictionary,txt which will have unicode,ascii table for each row. 

Secondly run main2.py to denormalize the input entry row by row (id,token MUST be included in the first row) and it would generate output.csv from input.csv according to the lookups on the dictionary.txt
