pyramid_starter_seed
====================

This is a Pyramid starter seed project integrated with the Yeoman workflow (concat and minification assets, grunt-uncss, cdnify-scripts and more).

Prerequisites
-------------

* Nodejs (you can manage and install different node versions using NVM)
* python virtualenv
* Pyramid

Installation
------------

Open your shell and digit::

    $ git clone git@github.com:davidemoro/pyramid_starter_seed.git
    $ cd pyramid_starter_seed
    $ YOUR_VIRTUALENV_PYTHON_PATH/bin/python setup.py develop
    $ cd pyramid_starter_seed/webapp
    $ bower install
    $ npm install


How to run
----------

Come back to the first level dir of pyramid_starter_seed (where .ini file lives)::

    $ cd ../..

Devel mode::

    $ YOUR_VIRTUALENV_PYTHON_PATH/bin/pserve development.ini
    
Production mode::

    $ YOUR_VIRTUALENV_PYTHON_PATH/bin/pserve production.ini

Links
-----

* http://davidemoro.blogspot.it/    [still writing blog post]
