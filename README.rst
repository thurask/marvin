README
======
    
A Python 2/3 script that opens a specific/random entry on the SCP Foundation wiki.

If you don't know what that is, `give it a shot <http://www.scp-wiki.net>`__.

Requirements
------------

Python 2.7 or Python 3.2+. Everything is inside the standard library.

To install, get it from pip:

::

    > pip install scp-marvin
    
Note: this command may be different depending on your system. Research beforehand.

Alternatively, just clone the git repo/download the source and install with setuptools:

::

    > python setup.py install
    
Once you've done that, access it through the ``marvin`` command.

Command Line Arguments
----------------------

Help
~~~~

::

    > marvin -h

    usage: marvin [-h] [-v] [-r] [scp]

    Opens an SCP entry on the SCP Foundation wiki.

    positional arguments:
      scp            SCP entry ID

    optional arguments:
      -h, --help     show this help message and exit
      -v, --version  show program's version number and exit
      -r, --random   Open a random entry

    http://github.com/thurask/marvin

Examples
~~~~~~~~

::

    > marvin 173
    
    > marvin scp-2998
    
    > marvin 789-j
    
would open `SCP-173 <http://www.scp-wiki.net/scp-173>`__, `SCP-2998 <http://www.scp-wiki.net/scp-2998>`__ and `SCP-789-J <http://www.scp-wiki.net/scp-789-j>`__, respectively.

::

    > marvin -r
    
would open a random article.

License
-------
Copyright 2015 Thurask <thuraski@hotmail.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the LICENSE file for more details.
