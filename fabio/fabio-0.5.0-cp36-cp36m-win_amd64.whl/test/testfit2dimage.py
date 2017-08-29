# coding: utf-8
#
#    Project: FabIO X-ray image reader
#
#    Copyright (C) 2010-2016 European Synchrotron Radiation Facility
#                       Grenoble, France
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

"""Test for FabIO reader for Fit2D binary images
"""
# Get ready for python3:
from __future__ import with_statement, print_function, division, absolute_import

__authors__ = ["Jérôme Kieffer"]
__contact__ = "jerome.kiefer@esrf.fr"
__license__ = "MIT"
__copyright__ = "2016-2016 European Synchrotron Radiation Facility"
__date__ = "27/07/2017"

import unittest
import sys
import os
import numpy

if __name__ == '__main__':
    import pkgutil
    __path__ = pkgutil.extend_path([os.path.dirname(__file__)], "fabio.test")
from .utilstest import UtilsTest


logger = UtilsTest.get_logger(__file__)
fabio = sys.modules["fabio"]
from fabio.fit2dimage import fit2dimage


class TestFit2DImage(unittest.TestCase):
    """ A few random clicks to make a test mask """

    def setUp(self):
        """
        download images
        """
        self.filename = UtilsTest.getimage("fit2d.f2d.bz2")[:-4]
        self.tiffilename = UtilsTest.getimage("fit2d.tif.bz2")[:-4]

    def test_read(self):
        """ Check it reads a mask OK """
        i = fit2dimage()
        i.read(self.filename)
        self.assertEqual(i.dim1, 25)
        self.assertEqual(i.dim2, 28)
        self.assertEqual(i.bpp, 4)
        self.assertEqual(i.bytecode, numpy.float32)
        self.assertEqual(i.data.shape, (28, 25))

    def test_match(self):
        """ test edf and msk are the same """
        i = fabio.open(self.filename)
        j = fabio.open(self.tiffilename)
        i.read(self.filename)
        self.assertEqual(i.data.shape, j.data.shape)
        diff = j.data - numpy.flipud(i.data)
        sumd = abs(diff).sum(dtype=float)
        self.assertEqual(sumd, 0)

    def test_mask(self):
        img = fabio.open(UtilsTest.getimage("Pilatus1M.f2d.bz2"))
        cbf = fabio.open(UtilsTest.getimage("Pilatus1M.cbf.bz2"))
        msk = fabio.open(UtilsTest.getimage("Pilatus1M.msk.bz2"))
        diff = abs((img.data).astype("int32") - cbf.data)
        self.assertEqual(diff.sum(), 0)
        diff = abs((msk.data).astype("int32") - img.header["data_mask"].astype("int32"))
        self.assertEqual(diff.sum(), 0)


def suite():
    loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
    testsuite = unittest.TestSuite()
    testsuite.addTest(loadTests(TestFit2DImage))
    return testsuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
