{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AUAI Summer-Python Basic (1)\n",
    "* reference 1 https://docs.python.org/3.6/library/\n",
    "* reference 1 https://www.w3schools.com/python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Hello World\n",
    "* using print()\n",
    "* line comment with #\n",
    "* Docstring with '''...''' or \"\"\"...\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello world\n"
     ]
    }
   ],
   "source": [
    "# this is the first comment\n",
    "print('Hello world')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: Vaiable \n",
    "* Numbers, Strings, Lists, Tuples, Sets, Dictionaries\n",
    "* 2 integer 3.75 floating point \n",
    "* String with single/double quotes '' \"\"\n",
    "* Constructors int(), float(), complex(), and str()\n",
    "* List with square brackets [,,]  [\"cat\", \"dog\"]\n",
    "* Tuples with round brackets (,,,)\n",
    "* Dictionary with {\"a\"=\"cat\", \"b\"=\"dog\"} dict(a=\"cat\", b=\"dog\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2.5\n",
      "cat\n"
     ]
    }
   ],
   "source": [
    "x = 2\n",
    "y = 2.5\n",
    "z = 'cat'\n",
    "print(x)\n",
    "print(y)\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Formatted output\n",
    "* \"%2d\", \"%.2f\" % a\n",
    "* '%s %s'  %  ('one' , 'two')\n",
    "* '{} {}'.format('one', 'two')\n",
    "* print (..., end='\\t')  print (..., end=' ') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "one two\n",
      "one two\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print('%s %s'  %  ('one' , 'two'))\n",
    "print('{} {}'.format('one', 'two'))\n",
    "print()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Loop\n",
    "* using range function as range(start, stop, step)\n",
    "* range(3)\n",
    "* range(1,10)\n",
    "* for x in [1, 2, 3]:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "for x in range(0,3):\n",
    "    for y in range(1,10):\n",
    "        for z in range(1,4):\n",
    "            m = x*3+z\n",
    "            print ('%d*%d=%2d' % (m,y,m*y), end='\\t')      \n",
    "        print ()\n",
    "    print ()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: List functions\n",
    "* append()\tAdds an element at the end of the list\n",
    "* reverse()\tReverses the order of the list\n",
    "* sort()\tSorts the list\n",
    "* len()  returns the number of items"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['John', 'Mary', 'Lisa', 'abhik']\n",
      "['abhik', 'Lisa', 'Mary', 'John']\n"
     ]
    }
   ],
   "source": [
    "a = ['John', 'Mary', 'Lisa']\n",
    "a.append(\"abhik\")\n",
    "print(a)\n",
    "list.reverse(a)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6: if condition, while condition\n",
    "* if condition: ....\n",
    "* while condition: ....\n",
    "* Equals: a == b\n",
    "* Not Equals: a != b\n",
    "* Less than: a < b\n",
    "* Less than or equal to: a <= b\n",
    "* Greater than: a > b\n",
    "* Greater than or equal to: a >= b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the greater is b\n"
     ]
    }
   ],
   "source": [
    "a = 2; b = 3\n",
    "if a>b :\n",
    "    print(\"The greater is a\")\n",
    "else:\n",
    "    print(\"the greater is b\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7: Boolean Values, Null objects, Ellipsis  \n",
    "* False and True\n",
    "* Null\n",
    "* ..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8: Operators\n",
    "*Logical Operators or / and / not\n",
    "*Identity Operators is / is not\n",
    "*Membership Operators in / not in\n",
    "*Bitwise Operators & AND/|OR /^\tXOR\t/~ NOT\t"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
