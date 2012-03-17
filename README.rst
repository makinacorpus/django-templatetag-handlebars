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

    {% load templatetag_handlebars %}

    <head>
    {% handlebars_js %}
    ...
    </head>

* Call the template tag, and write your Handlebars template :

::

    {% tplhandlebars "tpl-infos" %}
        {{total}} {% trans "result(s)." %}
        <p>{% trans "Min" %}: {{min}}</p>
        <p>{% trans "Max" %}: {{max}}</p>
    {% endtplhandlebars %}

* The following block with end-up in your page :

::

    <script id="tpl-infos" type="text/x-handlebars-template">
        {{total}} result(s).
        <p>Min: {{min}}</p>
        <p>Max: {{max}}</p>
    <script>

* Render it, client-side, as usual using ``Handlebars.js`` API :

::

    var properties = {
        total: 10,
        min: 4,
        max: 5
    };

    var template = Handlebars.compile($('#tpl-infos').html()),
        rendered = template(properties);

* Your rendered string is ready, and waiting to be inserted in your DOM :)

::

    10 result(s).
    <p>Min: 4</p>
    <p>Max: 5</p>


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

* `django-handlebars <https://github.com/yavorskiy/django-handlebars>`_, by Sergii Iavorskyi, which focuses on server-side Handlebars rendering.
* `django-handlebars <https://bitbucket.org/chrisv/django-handlebars>`_, by Chris Vigelius, with templates in separate files, and served in one block.

=======
LICENSE
=======

    * Lesser GNU Public License
    * ``Handlebars.js`` is released under the MIT license - Copyright 2011 Yehuda Katz
