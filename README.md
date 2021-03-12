# DocSearch App

The goal of this exercise is to create a working program to search a set of documents for the given search term or phrase (single token), and return results in order of relevance.
Relevancy is defined as number of times the exact term or phrase appears in the document.
Create three methods for searching the documents:
•	Simple string matching
•	Text search using regular expressions
•	Preprocess the content and then search the index

Prompt the user to enter a search term and search method, execute the search, and return results.

This project is built in Python.

How to Run:
1.  Clone repository
2.  Make sure you python3 installed
3.  Go to terminal
    ```bash
    $ python3 main.py
    ```
4.  Enter the dataset options(1 for Url, 2 for the files stored in the directory)
5.  Enter search term
5.  Enter search method (1 for string match, 2 for regex, or 3 for indexed or 4 for All above)

The program returns the number of match and the time to execute the search

