Project Descriptions: source code file for reporting from news database,
you will find a python code file for queries with plain text file for the result of the quires.

what you need to run the source code file:
1. install python 3.
2. if you are on windows you need a linux virtual box and vagrant 'the links below to download'. 
3. newsdata.sql file 'The Database'.
Note: In the links section below download the 3 requirements first then do the steps one by one.

How to install linux in the virtualbox using vagrant:
1. After downloading open your terminal cd change your directory
to vagrant directory and run 'vagrant up' to installations linux.
2. Then run 'vagrant ssh' to log into linux.
3. Put 'newsdata.sql' this file into the vagrant directory.
4. load the data into your vagrant directory using: 'psql -d news -f newsdata.sql' command 
what this command means:
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands
in the downloaded file, creating tables and populating them with data. 
5. To connect to your DB using: psql -d news (news is your database name).
6. To exploration the data use:  '\dt' dispaly tables and '\d table' shows the database schema for that particular table.
and select statements to display table data. 

The database includes three tables:
    The authors table includes information about the authors of articles.
    The articles table includes the articles themselves.
    The log table includes one entry for each time a user has accessed the site.

How to run the source code file:
1. save the Queries.py file with same folder of the DB in vagrant file.
2. In your terminal log into VB using 'vagrant ssh' then cd to /vagrant.
4. cd into DB directory that you have been saved.
5. run the file: python Queries.py or python3 Queries.py.

File source code explanation:
The news database is running PostgreSQL, so to connect the python file with DB we need to import psycopg2, 
then there are 3 quires variables with 1 functions to execute each quires with DB connection line 'psycopg2.connect("dbname=news")',
and object to execute quires and print lines to print the result of the quires. you can add new query variable and execute with 
'execute_query(yourQueryVariable)' function.

Text file:
you will find the output of each query in this file and the sql query with create view to
run this query in your DB and use this views for any others query in future.
views name are : 
1. for most articles views 'qmostartview'.
2. for popular authors 'qpopaut'.
3. for day that lead more than 1% of requests errors 'qdayerror'.

Database Link to download:
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Vagrant Link to download:
https://github.com/udacity/fullstack-nanodegree-vm

virtualbox link to download:
https://www.virtualbox.org/

