"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
import sys
import subprocess
from setuptools import setup
from plistlib import Plist


def generate_plist(plist_file):
    """Read plist from file and set CFBundleVersion to HEAD commit hash"""
    try:
        commit_hash = subprocess.check_output(
                ['git', 'rev-parse', '--short', 'HEAD']).strip()
    except Exception, e:
        print >> sys.stderr, ('Unable to get git commit hash for '
                'CFBundleVersion {0}'.format(e))
        commit_hash = 'none'

    plist = Plist.fromFile(plist_file)
    plist.update(dict(
        CFBundleVersion=commit_hash,
    ))
    return plist

APP = ['main.py']

DATA_FILES = ['gui', 'common', 'data_manager', 'tasks', 'data/English.lproj', 'data/Credits.html', 'data/MacTimeLog Help']

OPTIONS = {'argv_emulation': True, 'iconfile': 'data/iconset.icns',
           'plist': generate_plist('Info.plist'),
           'packages': ['objc', 'durus']}

for i in os.listdir('.'):
    if i.endswith('.py'):
        DATA_FILES.append(i)


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['pyobjc-framework-Cocoa', 'py2app', 'durus==3.1'],
    name='MacTimeLog',
    author='Artem Yunusov'
)
