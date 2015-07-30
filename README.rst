==========================
 An Adama service example
==========================


This repository contains an initial demo of an Adama_ service.

It wraps `The Haiti Earthquake Database`_ into a web service.


.. _The Haiti Earthquake Database: https://nees.org/dataview/spreadsheet/haiti


Using adamalib in Docker
========================

This repository includes a ``Dockerfile`` and a ``docker-compose.yml``
file, which allows a zero installation version of ``adamalib``.

The only requirements are Docker_ and `docker-compose`_:

.. code-block:: bash

   $ git clone https://github.com/DesignSafe-CI/adama_example
   $ cd adama_example
   $ docker-compose build
   $ docker-compose up

Navigate to http://localhost:8889 and access the Jupyter_ notebook
with password ``designsafe``.  The notebook ``Demo.ipynb`` contains the
actual example.

**Note**: If you are running on a Mac with ``boot2docker``, substitute
``localhost`` by the output of:

.. code-block:: bash

   $ boot2docker ip


License
=======

Free software: MIT license

.. _Adama: https://github.com/Arabidopsis-Information-Portal/adama
.. _Docker: https://docs.docker.com/installation/#installation
.. _docker-compose: https://docs.docker.com/compose/install/
.. _Jupyter: http://ipython.org/
