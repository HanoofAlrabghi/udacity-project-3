Project Descriptions: source code file for reporting from news database,
you will find a python code file for queries with plain text file for the result of the quries.

what you need to run the source code file:
1. install python 3.
2. if you are on windows you need a linux virtual box and vagrant. 
3. newsdata.sql file 'The Database'.

how to run the source code file:
1. save the Queries.py file with same folder of the DB.
2. In your terminal cd into DB directory.
3. run the file: python Queries.py or python3 Queries.py.

if you are in windows:
1. save the Queries.py file with same folder of the DB in vagrant file.
2. in your termianl cd to vagrant directory and run 'vagrant up' to installations linux.
3. run 'vagrant ssh' and 'cd /vagrant'.
4. cd into DB directory.
5. run the file: python Queries.py or python3 Queries.py.

File source code explanation:
The news database is running PostgreSQL, so to connect the python file with DB we need to import psycopg2 
and there are 3 functions for selec query each functions have a connection line to the DB 'psycopg2.connect("dbname=news")',
and object to execute query and print lines to print the result of the query. you can add new function to write another sql query.

Text file:
you will find the output of each query in this file and the sql query with create view to
run this query in your DB and use this views for any others query in future.
views name are : 
1. for most articles views 'qmostartview'.
2. for popular authors 'qpopaut'.
3. for day that lead more than 1% of requests errors 'qdayerror'.

