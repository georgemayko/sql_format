# SQL_FORMAT

A simple way to format your single line SQL query into a multi-line SQL Query.

# How to use

## Install as PIP dependency (PIP instalation is required [see](https://pypi.org/project/pip/))

Download the file file with extension .whl. In the actual version [here](/dist/sql_format-0.0.1-py3-none-any.whl)

Navigate to the folder you download  the file and execute this statement:

``` console
foo@bar:~$ pip install --user sql_format-0.0.1-py3-none-any.whl
``` 
This will install the sql_format as a cli app and install all dependencies. 

## Running

Execute the statement above on your terminal;

``` console
foo@bar:~$ sql_format "select 1 from dual"

SELECT 1 
FROM dual
``` 

## Usage

``` console
foo@bar:~$ sql_format --help

Usage: sql_format [OPTIONS] SQL

  Format your single line SQL Query into Multi-line SQL

Arguments:
  SQL  Your SQL query to be formatted, remember to pass it into quotes(single
       or double)  [required]
``` 

The SQL argument must contain quotes(single or double). Examples:

``` sql
"SELECT 1 FROM DUAL"
```
Or
``` sql
'SELECT 1 FROM DUAL'
```

# Development 

## Tech Stack

1. Python
2. Typer (cli framework)
3. Request (lib for HTTP requests)
4. Poetry (dependency management)

## Running tests
```  console
$ poetry run pytest
```

# Resources

This app was inpired on the  blog post of [Vlad Mihalcea](https://twitter.com/vlad_mihalcea) where he shows the same service using bash script.
[https://vladmihalcea.com/format-sql-command-line/] (https://vladmihalcea.com/format-sql-command-line/)

## Third-Part Dependencies

[SQL Format](https://sqlformat.org/) provides an API to format the SQL query. As a free API it has some request number limitations (500 requests per hour for a single IP [see details](https://sqlformat.org/api/#usage) ).

