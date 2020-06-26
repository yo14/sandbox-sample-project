# sandbox-sample-project
Place to trial and error some skills

note for:<br> <code>pip install flask-mysqldb</code> <br>
If having error like:  <br><code>ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.</code><br><br>Solution: <br><code>sudo apt-get install python-pip python-dev libmysqlclient-dev</code> <br> outside of virtual environtment.
<br></br>
<br>Make database and a table for submit-form project<br>
<pre>
mysql> CREATE DATABASE employee_data;
Query OK, 1 row affected (0,00 sec)

mysql> USE employee_data;
Database changed
mysql> CREATE TABLE employee(name varchar(20), age integer);
Query OK, 0 rows affected (0,55 sec)

mysql> SELECT * FROM employee;
Empty set (0,00 sec)
</pre>

<br><br>
Making session<br>
Need: session<br>
<pre>
from flask import Flask, render_template, request, session
</pre>
<br>
Implement:
<pre>
session['username'] = 'username'
</pre>
<br>
For protection to session, use 
<pre>
app.config['SECRET_KEY'] = os.urandom(24)
</pre>
<br>
Don't forget to import:
<pre>
import os
</pre>
<br>
We'll add password field, so we alter the table
<pre>
mysql> alter table employee 
    -> add password varchar(255);
Query OK, 0 rows affected (0,60 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> describe employee;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| name     | varchar(255) | YES  |     | NULL    |       |
| age      | int(11)      | YES  |     | NULL    |       |
| password | varchar(255) | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
3 rows in set (0,00 sec)

mysql> 
mysql> truncate table employee;
Query OK, 0 rows affected (0,21 sec)
</pre>







