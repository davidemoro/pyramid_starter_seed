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

Clone pyramid_starter_seed
--------------------------

Fetch pyramid_starter_seed, personalize it and then clone it!

This is still a TODO feature, so it doesn't work at this time.

Pyramid starter seed can be fetched, personalized and released with another name.
So other developer can build and release their own starter templates without having
to write a new package template generator.

It should speed up the process of creation of new more evoluted packages based on
Pyramid, also people that are not keen on writing their own paster templates.

If you want to release or just rename pyramid_starter_seed you'll have to call
a console script named `pyramid_starter_seed_clone` with the following syntax::

    $ YOUR_VIRTUALENV_PYTHON_PATH/bin/pyramid_starter_seed_clone new_template

and you'll get as a result a perfect renamed clone `new_template`.
Obviously you'll have to call this command outside the root directory of
pyramid_starter_seed.

It might not work in some corner cases just in case you choose a new package
name that contains reserved words or the name of a dependency of your plugin.

As result you'll get also a new console script named `new_template_clone`, so it 
sounds like a viral extension mechanism.

Links
-----

* http://davidemoro.blogspot.com/2014/09/pyramid-starter-seed-yeomam-part-1.html
