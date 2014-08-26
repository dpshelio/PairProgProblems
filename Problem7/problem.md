#The Unofficial PPC Problem!

You have probably seen one of those motivational messages:
````
If a = 1, b = 2, c = 3 etc, all the way to z = 26:
Then
hardwork = 8 + 1 + 18 + 4 + 23 + 15 + 18 + 11 = 98%
knowledge = 11 + 14 + 15 + 23 + 12 + 5 + 4 + 7 + 5 = 96%
but
attitude = 1 + 20 + 20 + 9 + 20 + 21 + 4 + 5 = 100%

Saying that having the right attitude will get you 100% of the way.
````

####Are there any other words that correspond to 100%?
Look in this very small (300 word) dictionary file and see if you can find other words that add up to 100!

**HINT**:
All letters in ASCII are represented internally as numbers, sometimes called ordinals. You can use
this feature so that you can easily get a number from a letter, but be careful! The numbers do not
start from 1, so you will need to use an offset.

[Extra info about the ASCII representation](http://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html)

This list only contains words written in all lowercase, to make the conversion a little easier.
Uppercase and lowercase letters have different ASCII values.

The following function names may help a little bit:

* EXCEL has a `CODE()` function
* Python has an `ord()` function
* MATLAB allows one to get the number by subtracting a letter from another letter (and you can
use this to great effect!)


P.S. This example is a artificial dictionary, which has a higher proportion (about 7.6%) of words with this property.
In a much larger dictionary (of [58110 words](http://www.mieliestronk.com/wordlist.html) ), only 657 had this property, or about 1.1%.
