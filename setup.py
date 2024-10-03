# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# setup.py
# Copyright (C) 2024 Fracpete (fracpete at waikato dot ac dot nz)

from setuptools import setup


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="pymeka",
    description="Python3 wrapper for Meka, the multi-label/multi-target extension to Weka.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/fracpete/pymeka",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
    license='GNU General Public License version 3.0 (GPLv3)',
    package_dir={
        '': 'src'
    },
    packages=[
        "meka",
        "meka.core",
    ],
    package_data={
        "meka": ["lib/*"],
    },
    include_package_data=True,
    version="0.0.1",
    author='Peter "fracpete" Reutemann',
    author_email='fracpete@waikato.ac.nz',
    install_requires=[
        "jpype1",
        "numpy",
        "packaging",
        "configurable-objects",
        "simple-range",
        "requests",
    ],
)
