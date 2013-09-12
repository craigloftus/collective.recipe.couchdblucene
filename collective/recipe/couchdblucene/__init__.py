# -*- coding: utf-8 -*-

import glob
import os
import shutil
import subprocess
import zipfile

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        if not 'location' in options:
            options['location'] = os.path.join(buildout['buildout']['directory'], 'lib', 'couchdb-lucene')

        self.options = options

    def install(self):
        """Installer"""
        options = self.options
        os.chdir(options['download'])
        # Call Maven to build couchdb-lucene
        subprocess.call('mvn')
        # If a path to the zip file is not provided, then look for it
        if not 'zip' in options:
            options['zip'] = glob.glob(os.path.join(options['download'], 'target', '*.zip'))[0]
        # Create directory for extracted files
        target_dir = options['location']
        # Temporary directory
        tmp_dir = '/tmp/'
        # Unzip the produced archive
        with zipfile.ZipFile(options['zip']) as zip_file:
            # Extract
            zip_file.extractall(tmp_dir)
            # Find the run member
            run_member = next(_ for _ in zip_file.namelist() if _.endswith('run'))
            run_path = os.path.join(tmp_dir, run_member)
            # Make the extracted run file executable
            os.chmod(run_path, 0777)
            # Move from the tmp directory to the target directory
            shutil.move(os.path.join(tmp_dir, zip_file.namelist()[0][:-1]), target_dir)
        return [target_dir]

    def update(self):
        pass
