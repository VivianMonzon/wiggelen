"""
Wiggelen, working with wiggle tracks in Python.

.. todo:: Specify region(s) to use (same as filter?), possibly with a BED file.
.. todo:: Conversion to BigWig.
.. todo:: Connect with numpy/pandas.

.. Copyright (c) 2012 Leiden University Medical Center <humgen@lumc.nl>
.. Copyright (c) 2012 Martijn Vermaat <m.vermaat.hg@lumc.nl>
.. Copyright (c) 2012 Jeroen Laros <j.f.j.laros@lumc.nl>

.. Licensed under the MIT license, see the LICENSE file.
"""


from .wiggle import walk, zip_, fill, write


# On the event of a new release, we update the __version_info__ package
# global and set RELEASE to True.
# Before a release, a development version is denoted by a __version_info__
# ending with a 'dev' item and RELEASE is set to False.
#
# We follow a versioning scheme compatible with setuptools [1] where the
# __version_info__ variable always contains the version of the upcomming
# release (and not that of the previous release), post-fixed with a 'dev'
# item. Only in a release commit, this 'dev' item is removed (and added
# again in the next commit).
#
# [1] http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version

RELEASE = False

__version_info__ = ('0', '1', 'dev')


__version__ = '.'.join(__version_info__)
__author__ = 'LUMC, Martijn Vermaat, Jeroen Laros'
__contact__ = 'm.vermaat.hg@lumc.nl'
__homepage__ = 'http://www.humgen.nl'


__all__ = ['walk', 'zip_', 'fill', 'write']
