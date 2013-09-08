# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath('.'))

language = 'en'

master_doc = 'index'
if language == 'ja':
    project = u'Python2.5から3.3で動作するツールの作り方'
else:
    project = u'How to make with Python2 to 3'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '1.0'
exclude_patterns = ['_build']
locale_dirs = ['locale']
pygments_style = 'sphinx'
extensions = [
    'sphinxjp.themecore',
    'sphinx.ext.todo',
    'sphinxcontrib.blockdiag',
    'sphinxcontrib.seqdiag',
]
todo_include_todos = True
html_logo = 'images/sphinx-logo.png'
html_static_path = ['_static']
html_use_index = False
html_theme = 's6'

# -- directive/role definition ------------------------------------------------>

from docutils.parsers.rst.directives.admonitions import Admonition
from sphinx.util.compat import make_admonition


class SpeechDirective(Admonition):
    css_class = 'speech'
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        title = u'[speech]'
        if self.arguments:
            title += self.arguments[0]

        if 'class' in self.options:
            self.options['class'].append(self.css_class)
        else:
            self.options['class'] = [self.css_class]

        ret = make_admonition(
            self.node_class, self.name, [title], self.options,
            self.content, self.lineno, self.content_offset, self.block_text,
            self.state, self.state_machine)
        ret[0].attributes['name'] = self.name
        return ret


def setup(app):
    app.add_stylesheet('custom.css')
    app.add_javascript('custom.js')
    app.add_directive('speech', SpeechDirective)
