from distutils.core import setup
import py2exe

setup(console=[{ "script": "bundlefiles_test.py"}],
    options={"py2exe": {
        "bundle_files": 2,
        "verbose": 4}})
