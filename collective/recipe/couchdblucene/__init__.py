# -*- coding: utf-8 -*-

import os
import subprocess

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        pass

    def install(self):
        """Installer"""
        os.chdir('parts/couchdb-lucene-download')
        subprocess.call('mvn')

