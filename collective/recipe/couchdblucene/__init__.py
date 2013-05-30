# -*- coding: utf-8 -*-

import os
import subprocess
import zipfile

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        pass

    def install(self):
        """Installer"""
        filename = 'couchdb-lucene-0.10.0-SNAPSHOT-dist.zip'
        os.chdir('parts/couchdb-lucene-download')
        subprocess.call('mvn')
        os.chdir(os.path.join(os.getcwd(), os.path.pardir, os.path.pardir))
        tar_file = zipfile.ZipFile(os.path.join(os.getcwd(), 'parts', 'couchdb-lucene-download', 'target', filename))
        tar_file.extractall('lib')
        os.chmod(os.path.join('lib', 'couchdb-lucene-0.10.0-SNAPSHOT', 'bin', 'run'), 0777)

    def update(self):
        pass

