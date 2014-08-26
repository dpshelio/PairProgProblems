#Problem 6

We've recenltly discovered a huge dataset from an old magnetometer stored in some boxes, the data is saved in films and the institute is making huge efforts to digitalised this amazing data.  The digitalisation team will create one file by day, and we need to store these files in some hierarchical way that will make it easier to find.

Our task is to create a directory structure to save data from the new discovered instrument (you name it) using the following directory structure:

`instrument/YYYY/MM/DD/file`

So, the tree of the directory should look like:
```
instrument
  |- ...
  |- 1995
  |    |- 01
  |    |   |- 01
  |    |   |- ...
  |    |   |- 31
  |    |- ...
  |    |-12
  |       |- ...
  |- 1996
  |- ...
```

* We have to create such structure for the years 1889 - 2015
* Have in mind that the number of days are different between months
* Some years has one day less... how do you know which ones? [This may help](http://www.wikihow.com/Calculate-Leap-Years)

Not silly questions:
* why no dump all the files in the same directory with a name like: `instrument_YYYYMMDD.dat` ?
