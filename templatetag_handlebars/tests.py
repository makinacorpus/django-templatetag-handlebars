from django.template import Context, Template
from django.test import TestCase


class TemplateTagTest(TestCase):
    def test_rendering(self):
        """
        Tests that {{}} tags are well escaped.
        """
        t = Template("""
            {% load i18n templatetag_handlebars %}
            
            <head>
                {% handlebars_js %}
            </head>
            
            {% tplhandlebars "tpl-testing" %}
                {% trans "with translation" %}
                <p>{{name}}</p>
                {{{rawname}}}
                {# works with comments too #}
            {% endtplhandlebars %}
            """)
        c = Context()
        rendered = t.render(c)
        self.failUnless('handlebars.js"></script>' in rendered)
        self.failUnless('<script id="tpl-testing" type="text/x-handlebars-template">' in rendered)
        self.failUnless('{{name}}' in rendered)
        self.failUnless('{{{rawname}}}' in rendered)
        self.failUnless('with translation' in rendered)
        # HTML should not be escaped
        self.failUnless('<p>' in rendered)
        self.failUnless('</p>' in rendered)
        # Those should not be rendered :
        self.failUnless('{% trans %}' not in rendered)
        self.failUnless('comments' not in rendered)
