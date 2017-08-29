#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Project: Fable Input Output
#             https://github.com/silx-kit/fabio
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
#bruker Unit tests

#built on testbrukerimage
19/01/2015
"""
from __future__ import print_function, with_statement, division, absolute_import
import unittest
import os
import numpy
if __name__ == '__main__':
    import pkgutil
    __path__ = pkgutil.extend_path([os.path.dirname(__file__)], "fabio.test")
from .utilstest import UtilsTest

logger = UtilsTest.get_logger(__file__)
from ..brukerimage import brukerimage
from .. import fabioutils

# this is actually a violation of the bruker format since the order of
# the header items is specified
# in the standard, whereas the order of a python dictionary is not
MYHEADER = {"FORMAT": '86',
            'NPIXELB': '2',
            'VERSION': '9',
            'HDRBLKS': '5',
            'NOVERFL': '4',
            'NCOLS': '256',
            'NROWS': '256',
            'WORDORD': '0'}

MYIMAGE = numpy.ones((256, 256), numpy.uint16) * 16
MYIMAGE[0, 0] = 0
MYIMAGE[1, 1] = 32
MYIMAGE[127:129, 127:129] = 65535
if not numpy.little_endian:
    MYIMAGE.byteswap(True)


OVERFLOWS = [
    ["%09d" % 4194304, ("%07d" % (127 * 256 + 127))],
    ["%09d" % 4194304, ("%07d" % (127 * 256 + 128))],
    ["%09d" % 4194304, ("%07d" % (128 * 256 + 127))],
    ["%09d" % 4194304, ("%07d" % (128 * 256 + 128))]
    ]


class TestBruker(unittest.TestCase):
    """basic test"""

    def setUp(self):
        """ Generate a test bruker image """
        self.filename = os.path.join(UtilsTest.tempdir, "image.0000")

        with open(self.filename, 'wb') as fout:
            wrb = 0
            for key, val in MYHEADER.items():
                fout.write((("%-7s" % key) + ':' + ("%-72s" % val)).encode("ASCII"))
                wrb = wrb + 80
            hdrblks = int(MYHEADER['HDRBLKS'])
            while (wrb < hdrblks * 512):
                fout.write(b"\x1a\x04")
                fout.write(b'.' * 78)
                wrb = wrb + 80
            fout.write(MYIMAGE.tostring())

            noverfl = int(MYHEADER['NOVERFL'])
            for ovf in OVERFLOWS:
                fout.write((ovf[0] + ovf[1]).encode("ASCII"))
            fout.write(b'.' * (512 - (16 * noverfl) % 512))

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        if os.path.exists(self.filename):
            os.unlink(self.filename)

    def test_read(self):
        """ see if we can read the test image """
        obj = brukerimage()
        obj.read(self.filename)
        self.assertAlmostEqual(obj.getmean(), 272.0, 2)
        self.assertEqual(obj.getmin(), 0)
        self.assertEqual(obj.getmax(), 4194304)


class TestBzipBruker(TestBruker):
    """ test for a bzipped image """
    def setUp(self):
        """ create the image """
        TestBruker.setUp(self)
        if os.path.isfile(self.filename + ".bz2"):
            os.unlink(self.filename + ".bz2")
        with fabioutils.BZ2File(self.filename + ".bz2", "wb") as wf:
            with open(self.filename, "rb") as rf:
                wf.write(rf.read())
        self.filename = self.filename + ".bz2"


class TestGzipBruker(TestBruker):
    """ test for a gzipped image """
    def setUp(self):
        """ Create the image """
        TestBruker.setUp(self)
        if os.path.isfile(self.filename + ".gz"):
            os.unlink(self.filename + ".gz")
        with fabioutils.GzipFile(self.filename + ".gz", "wb") as wf:
            with open(self.filename, "rb") as rf:
                wf.write(rf.read())
        self.filename = self.filename + ".gz"


class TestBrukerLinear(unittest.TestCase):
    """basic test, test a random array of float32"""
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.filename = os.path.join(UtilsTest.tempdir, "bruker.0000")
        self.data = numpy.random.random((500, 550)).astype("float32")

    def test_linear(self):
        """ test for self consistency of random data read/write """
        obj = brukerimage(data=self.data)
        obj.write(self.filename)
        new = brukerimage()
        new.read(self.filename)
        error = abs(new.data - self.data).max()
        self.assertTrue(error < numpy.finfo(numpy.float32).eps, "Error is %s>1e-7" % error)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        if os.path.exists(self.filename):
            os.unlink(self.filename)

# statistics come from fit2d I think
# filename dim1 dim2 min max mean stddev
TESTIMAGES = """Cr8F8140k103.0026   512  512  0  145942 289.37  432.17
                Cr8F8140k103.0026.gz   512  512  0  145942 289.37  432.17
                Cr8F8140k103.0026.bz2   512  512  0 145942 289.37  432.17"""


class TestRealImg(unittest.TestCase):
    """ check some read data from bruker detector"""
    def setUp(self):
        """
        download images
        """
        self.im_dir = os.path.dirname(UtilsTest.getimage("Cr8F8140k103.0026.bz2"))

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.im_dir = None

    def test_read(self):
        """ check we can read bruker images"""
        for line in TESTIMAGES.split("\n"):
            vals = line.split()
            name = vals[0]
            dim1, dim2 = [int(x) for x in vals[1:3]]
            mini, maxi, mean, stddev = [float(x) for x in vals[3:]]
            obj = brukerimage()
            obj.read(os.path.join(self.im_dir, name))
            self.assertAlmostEqual(mini, obj.getmin(), 2, "getmin")
            self.assertAlmostEqual(maxi, obj.getmax(), 2, "getmax")
            self.assertAlmostEqual(mean, obj.getmean(), 2, "getmean")
            self.assertAlmostEqual(stddev, obj.getstddev(), 2, "getstddev")
            self.assertEqual(dim1, obj.dim1, "dim1")
            self.assertEqual(dim2, obj.dim2, "dim2")

    def test_write(self):
        "Test writing with self consistency at the fabio level"
        for line in TESTIMAGES.split("\n"):
            vals = line.split()
            name = vals[0]
            obj = brukerimage()
            ref = brukerimage()
            fname = os.path.join(self.im_dir, name)
            obj.read(fname)
            obj.write(os.path.join(UtilsTest.tempdir, name))
            other = brukerimage()
            other.read(os.path.join(UtilsTest.tempdir, name))
            ref.read(fname)
            self.assertEqual(abs(obj.data - other.data).max(), 0, "data are the same")
            for key in ref.header:
                if key in ("filename",):
                    continue
                if key not in other.header:
                    logger.warning("Key %s is missing in new header, was %s" % (key, ref.header[key]))
                else:
                    self.assertEqual(ref.header[key], other.header[key], "value are the same for key %s: was %s now %s" % (key, ref.header[key], other.header[key]))


def suite():
    loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
    testsuite = unittest.TestSuite()
    testsuite.addTest(loadTests(TestBruker))
    testsuite.addTest(loadTests(TestBzipBruker))
    testsuite.addTest(loadTests(TestGzipBruker))
    testsuite.addTest(loadTests(TestRealImg))
    testsuite.addTest(loadTests(TestBrukerLinear))
    return testsuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
