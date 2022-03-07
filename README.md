# DEI-Collections

Tools for analyzing diverse holdings within a library's collections and for making some collection development recomendations based on that information.  Tools seen here were originally developed for Sierra libraries but can be adapted for others, and [the Booklist Holdings Comparison](https://github.com/jmgold/DEI-Collections/blob/main/Booklist_Holdings_Comparison.ipynb) can be used regardless of ILS.

Tools were developed with the assistance of the Minuteman Library Networks' DEI reports team, and Kate Wolfe in particular, as well as input from Anna Mickelsen of the Springfield Public Library.

There are 3 main tools we have developed, and which are represented in this repository.

##### SQL Queries

A set of SQL queries that parse LC subject headings to sort our titles into various DEI related topics.  These were all designed to work with the report builder tool built into our intranet site, but will work for any Sierra library so long as you fill out the variables when indicated by '[]' characters.  Currently there are 4 such reports

[Diversity analysis](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/diversity%20analysis.sql) Gathers the count/percentage of holdings that falls into each DEI topical segment

[Collection Development](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/collection%20development%20by%20diversity.sql) Gathers various circulation performance metrics for the items within each DEI segment

[Popular Titles](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/popular%20titles%20dei.sql) Identifies the most popular titles in a given area.

[Popular Titles: Unowned](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/popular%20titles%20unowned%20dei.sql) Identifies the most popular titles in the consortia that are not owned by a given location

##### Data Studio Dashboard

[Python script](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/DEI%20Dashboard.py) used to run a version of [the diversity analysis report](https://github.com/jmgold/DEI-Collections/blob/main/Sierra%20SQL/diversity%20analysis.sql) and load the data into a Google sheet.  That sheet is then used as a data source for an interactive dashboard built in Google's Data Studio

##### Booklist Holdings Comparison

[Python script running in Google Colab](https://github.com/jmgold/DEI-Collections/blob/main/Booklist_Holdings_Comparison.ipynb).  This script will allow you to quickly compare your holdings (loaded as a csv or Excel file) to a list of titles from an external source to provide the overlapping and absent titles.  Script using a fuzzy string matching algorithm in order to address data differences between the two lists such as alternate spellings of names or the inclusion/exclusion of subtitles.  Script was originally built for the use case of comparing holdings to a list of suggested diverse titles but can be used any time two lists of books need to be compared.
