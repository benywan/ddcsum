import os
import sys
from setuptools import find_packages, setup

from ddcsum import __version__

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: ddcsum requires Python version >= 2.7.0...")

data_files = []

requires = [
    'slowaes',
    'ecdsa',
    'pbkdf2',
    'requests',
    'jsonrpclib',
    'six',
    'appdirs',
    'keyring==10.4.0',
    'lbryschema==0.0.15',
]

console_scripts = [
    'ddcsum = ddcsum.main:main',
]

base_dir = os.path.abspath(os.path.dirname(__file__))

setup(
    name="ddcsum",
    version=__version__,
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
    package_data={'ddcsum': ['wordlist/*.txt']},
    entry_points={'console_scripts': console_scripts},
    description="Lightweight DDCScrd Wallet",
    author="DDCS Inc.",
    author_email="hello@lbry.io",
    license="GNU GPLv3",
    url="https://ddcs.io",
    long_description="""Lightweight DDCScrd Wallet""",
    zip_safe=False
)
