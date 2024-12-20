Installation
============

Since **pymeka** is based on `python-weka-wrapper3 <https://github.com/fracpete/python-weka-wrapper3>`__,
you can follow the instructions there to install the infrastructure:

https://fracpete.github.io/python-weka-wrapper3/install.html

Once python-weka-wrapper3 has been installed successfully, you can install pymeka.


PyPI
----

Installing the latest published version from PyPI.org is done as follows:

```bash
pip install pymeka
```


Github
------

If you want to install the latest source code, then execute the following:

```bash
pip install git+https://github.com/fracpete/pymeka.git
```


Meka Java binaries
------------------

The first time that the JVM is being launched (using `meka.core.jvm.start()`), the Meka binaries will
get downloaded and decompressed automatically.

If you want to override the default URL, e.g., for using a snapshot, you can set the `MEKA_URL`
environment variable. For example for using a snapshot:

```bash
MEKA_URL=https://adams.cms.waikato.ac.nz/snapshots/meka/meka-snapshot.zip
```

If you want to install from a local zip file (snapshot or release archive), then you can do that as well:

```bash
MEKA_URL=/some/where/meka-snapshot.zip
```
