{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# AUAI Summer-Python Basic (2)\n",
    "* reference 1 https://docs.python.org/3.6/library/\n",
    "* reference 1 https://www.w3schools.com/python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: module and function definition\n",
    "* def func(a, b, c):\n",
    "* return value\n",
    "* Classes"
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
    "# Fibonacci numbers module fibo.py\n",
    "def fib(n):    # write Fibonacci series up to n\n",
    "    a, b = 0, 1\n",
    "    while b < n:\n",
    "        print b,\n",
    "        a, b = b, a+b\n",
    "\n",
    "def fib2(n):   # return Fibonacci series up to n\n",
    "    result = []\n",
    "    a, b = 0, 1\n",
    "    while b < n:\n",
    "        result.append(b)\n",
    "        a, b = b, a+b\n",
    "    return result"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: import module\n",
    "*import fibo\n",
    "*from fibo import fib, fib2\n",
    "*from fibo import *\n",
    "*import sys\n",
    "*import os\n",
    "*import io\n",
    "*import json\n",
    "*import re\n"
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
    "## Step 3: Reading Files\n",
    "* f = open('workfile')\n",
    "* with open('workfile') as f:\n",
    "* f.read()\n",
    "* f.readline()\n",
    "* f.close()\n",
    "* for line in f:"
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
    "## Step 4:  Writing Files\n",
    "* f = open('workfile', 'w')\n",
    "* with open('workfile') as f:\n",
    "* f.write()\n",
    "* f.close()"
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
    "## Step 5: import sys\n",
    "* sys.argv\n",
    "* sys.platform"
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
    "import sys\n",
    "print(sys.platform)\n",
    "print(sys.argv(1))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6: import os\n",
    "*os.getcwd() # Get current directory\n",
    "*os.chdir() # Change directory"
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
    "## Step 7: import io\n",
    "*io — Text, Binary, and Raw Stream I/O Tools\n",
    "*StringIO\n",
    "*BinaryIO\n",
    "*RawIO"
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
    "## Step 8:import json\n",
    "*json.loads()\n",
    "*json.dumps()\n",
    "*json.JSONEncoder().encode({\"foo\": [\"bar\", \"baz\"]})"
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
    "## Step 9:import re\n",
    "*re.search('(?<=abc)def', 'abcdef')\n",
    "*re.match(pattern, string)"
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
    "## Step 10:import csv\n",
    "*for row in csv.reader(csvfile, delimiter=',', quotchar='\"'): # 2\n",
    "*w =csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)\n",
    "*w.writerow()"
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
    "## Step 11:import math\n",
    "*math.sqrt()\n",
    "*math.exp() \n",
    "*math.ceil()\n",
    "*math.floor()"
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
