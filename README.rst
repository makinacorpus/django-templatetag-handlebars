*django-templatetag-handlebars* allows you to embed `Handlebars.js <http://handlebarsjs.com>`_ 
templates in your django templates.

Most of the template tag code comes from `Miguel Araujo's verbatim snippet <https://gist.github.com/893408>`_. 

=======
INSTALL
=======

::

    pip install django-templatetag-handlebars

=====
USAGE
=====

* Add ``templatetag_handlebars`` to your ``INSTALLED_APPS``

* Add the HTML header :

::

    <head>
    {% include "templatetag_handlebars/head.html" %}
    ...
    </head>

* Call the template tag :

::

    {% load templatetag_handlebars %}
    
    {% tplhandlebars "tpl-infos" %}
        {{total}} {% trans "result(s)." %}
        <p>{% trans "Min" %}: {{min}}</p>
        <p>{% trans "Max" %}: {{max}}</p>
    {% endtplhandlebars %}

* Render your block as usual using ``Handlebars.js`` API :

::

    var properties = {
        total: 10,
        min: 5,
        max: 4
    };

    var template = Handlebars.compile($('#tpl-infos').html()),
        rendered = template(properties);


=======
AUTHORS
=======

    * Mathieu Leplatre <mathieu.leplatre@makina-corpus.com>
    * Miguel Araujo <https://github.com/maraujop>

|makinacom|_

.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com


Similar tools
=============

* `django-handlebars <http://pypi.python.org/pypi/django-handlebars>`_, by Chris Vigelius, 
   which focuses on server-side Handlebars rendering.

=======
LICENSE
=======

    * Lesser GNU Public License
    * ``Handlebars.js`` is released under the MIT license - Copyright 2011 Yehuda Katz
