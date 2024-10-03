Introduction
============

*pymeka* allows you to use `Meka <https://github.com/Waikato/meka>`__ from within Python3.

The library uses the `jpype <https://github.com/jpype-project/jpype>`__ library for starting up,
communicating with and shutting down the Java Virtual Machine in which the Meka processes get executed.

Links:

* Looking for code?

  * `Project homepage <https://github.com/fracpete/pymeka>`__
  * `Example code <https://github.com/fracpete/pymeka-examples>`__


Requirements
============

The library has the following requirements:

* Python 3 (does not work with Python 2)

 * jpype (required)

* OpenJDK 11 (or later)

Uses:

* Meka (1.9.8)

Contents
========

.. toctree::
   :maxdepth: 2

   install
   docker
   examples

API
===

.. toctree::
   :maxdepth: 4

   meka
