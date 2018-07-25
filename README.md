# Log Analisys Project

The program for log analisys performs queries on a database to find out the most read Articles and Authors, and to analize access errors to the webpage.

# Requirements
It is necessary the installation of _python3_ programming language (version 3) and _PostgreSQL_ database system. Besides, before running the application, is necessary to import the data from _newsdata.sql_ database.

# Running

Connecting to the database:
```
1 - Unzip newsdata.zip file
2 - Load newsdata.sql into the database and connect: "psql -d news -f newsdata.sql".
3 - Or just: "psql -d news", if the data has already been loaded.
```

The program can be run in two ways:

- Executable program:
```
1 - Make the file log_analisys.py executable: sudo chmod x+ log-analisys.py
2 - Run: ./log_analisys.py
```

- Run using python3:
```
1 - Run: python3 log_analisys.py
```
The output will be a file with the name _results.txt_, with the queries results.

# License
[MIT](https://choosealicense.com/licenses/mit/)
