

# divdate: division based date/time building for Python

divdate is a Python module to build date and datetime object using the division operator.

## Installation

```
pip install divdate
```

## Usage example

Say you want to build a date object in python,
but you don't feel like using these weird constructors/factories with those confusing things called arguments.
Use `divdate`! It just feels so natural!

```python
>>> from divdate import ddate
>>> d = ddate/2015/11/25
>>> d.year
2015
>>> d.month
11
>>> d.day
25
>>> import datetime
>>> isinstance(d, datetime.date)
True
```

You also want time? Microseconds? No problem, m'am, sir.

```python
>>> d = ddate/2015/11/25/16/34/12/21343
>>> d.hour
16
>>> d.minute
34
>>> d.second
12
>>> d.microsecond
21343
>>> isinstance(d, datetime.datetime)
True
```

## FAQ

### Isn't this a bit silly?

Yes, it is. Please proceed with googling funny pictures of cats.


