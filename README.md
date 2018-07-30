# Log Analysis Project

The program for log analysis performs queries on a fictional news webpage database to find out the most read Articles and Authors, and to analyze access errors.
The _newsdata.zip_ database contains 3 tables: LOG, AUTHORS and ARTICLES. Below are the fields for each table:
- LOG: path, ip, method, status, time, id;
- AUTHORS: name, bio, id;
- ARTICLES: author, title, slug, lead, body, time, id.

Over the tables registers the application will run SQL queries to answer the following questions:
1) The 3 most popular ARTICLES
2) Authors of the most popular articles
3) Days when errors from requests are more then 1%

# Requirements
Before running the program, make sure to have installed _Python_, _VirtualBox_, _Vagrant_, _PostgreSQL_, and to import _newsdata.sql_ file into PostgreSQL. When using the _Vagranfile_ from the link below, python and PostgreSQL will be installed automatically.

- For Windows users, please install [Git Bash](https://git-scm.com/downloads) to have a Unix-style terminal.
- Install the virtual machine [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (platform package)
- Install [Vangrant](https://www.vagrantup.com/downloads.html) software
- Log in on Github and fork the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository to have Vagrant configuration file
- Clone vagrant repository to your local machine
```sh
$git clone http://github.com/<username>/fullstack-nanodegree-vm fullstack
```
- Run the virtual machine
```sh
$cd fullstack
$vagrant up
$vagrant ssh
$cd /vagrant
```
The `/vagrant` directory is where the files will be shared with the local machine
- Log in on Github and fork the [log-analysis](https://github.com/nulladams/log-analisys) repository
- Clone the repository to your local machine
```sh
$git clone http://github.com/<username>/log-analisys log-analysis
$cd log-analysis
```
- Unzip _newsdata.zip_ and import _newsdata.sql_ to PostgreSQL database system
```sh
$psql -d news -f newsdata.sql
```
or just `psql -d news` if the data has already been loaded.
Now we reach the point to execute the log analysis application. Proceed to _Running_ for more information.

- To stop the virtual machine
```sh
$exit
$vagrant halt
```

# Running
The program can be run in two ways:

1) Executable program:
```
Make the file log_analisys.py executable: sudo chmod x+ log-analisys.py
Run: ./log_analisys.py
```

2) Run using python3:
```
Run: python3 log_analisys.py
```
The output will be a file with the name _results.txt_, with the queries results.

# License
[MIT](https://choosealicense.com/licenses/mit/)
