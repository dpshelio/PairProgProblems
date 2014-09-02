#Databases

What's a database? we will learn it today by using sqlite and a dataset of almost 8000 records, with information of the different airports. But first, let's get some basic information with a simple example:

To import the data in sqlite is very easy, for example if I would have a file with the following fields:

```
#id, name, surname, age, country
1, William, Shakespeare, 320, England
2, Miguel, De Cervantes, 346, Spain
...
```
Once we open sqlite,

```shell
$ sqlite3
```
We would need to define the data fields for the table in the database as follows:

```sqlite
create table writers (id integer, name text, surname text, age integer, country text);
.separator ","
.import writers.csv writers
```

Now, we can search the data using the power of the database, for example:

```sqlite
select * from writers;
select * from writers where country == 'Spain';
select count(*) from writers where age > 345;
select name from writers where country == 'England' and age > 1000;
select surname from writers where surname like '%pear%';
```

#Problem

Your first task is to download the `airports.dat` file and understand what each column contain, [openglight](http://openflights.org/data.html) provides us with the data.
So, following the above examples, create a table for the airports information and extract the following data:

* How many airports are in South Africa?
* How many airports has 'sand' in their name?
* which airports are just 10 degrees apart from the equator?
* which airports are above closer to the pole?
* which countries have airports at the Greenwich meridian?
* which cities have aiports in a 10 degrees x 10 degrees at the [antipodes](http://en.wikipedia.org/wiki/Antipodes) of [Hermanus](http://en.wikipedia.org/wiki/Hermanus)?
* ... and of [Gran Canaria](http://en.wikipedia.org/wiki/Gran_Canaria) (David's place)?
(check them in [this interactive map](http://www.antipodesmap.com/))
* Do any other question you can think of!

Want to learn more? Check [Software Carpentry](http://software-carpentry.org/v5/novice/sql/index.html) lessons about databases.
