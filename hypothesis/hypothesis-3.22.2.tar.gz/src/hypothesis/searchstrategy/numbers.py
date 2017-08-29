# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2017 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

import math
from collections import namedtuple

import hypothesis.internal.conjecture.utils as d
from hypothesis.control import assume
from hypothesis.internal.compat import hbytes, struct_pack, \
    struct_unpack, int_from_bytes
from hypothesis.internal.floats import sign
from hypothesis.searchstrategy.strategies import SearchStrategy, \
    MappedSearchStrategy


class IntStrategy(SearchStrategy):

    """A generic strategy for integer types that provides the basic methods
    other than produce.

    Subclasses should provide the produce method.

    """


class IntegersFromStrategy(SearchStrategy):

    def __init__(self, lower_bound, average_size=100000.0):
        super(IntegersFromStrategy, self).__init__()
        self.lower_bound = lower_bound
        self.average_size = average_size

    def __repr__(self):
        return 'IntegersFromStrategy(%d)' % (self.lower_bound,)

    def do_draw(self, data):
        return int(
            self.lower_bound + d.geometric(data, 1.0 / self.average_size))


class WideRangeIntStrategy(IntStrategy):

    def __repr__(self):
        return 'WideRangeIntStrategy()'

    def do_draw(self, data):
        size = 16
        sign_mask = 2 ** (size * 8 - 1)

        byt = data.draw_bytes(size)
        r = int_from_bytes(byt)
        negative = r & sign_mask
        r &= (~sign_mask)
        if negative:
            r = -r
        return int(r)


class BoundedIntStrategy(SearchStrategy):

    """A strategy for providing integers in some interval with inclusive
    endpoints."""

    def __init__(self, start, end):
        SearchStrategy.__init__(self)
        self.start = start
        self.end = end

    def __repr__(self):
        return 'BoundedIntStrategy(%d, %d)' % (self.start, self.end)

    def do_draw(self, data):
        return d.integer_range(data, self.start, self.end)


NASTY_FLOATS = [
    0.0, 0.5, 1.0 / 3, 10e6, 10e-6, 1.175494351e-38, 2.2250738585072014e-308,
    1.7976931348623157e+308, 3.402823466e+38, 9007199254740992, 1 - 10e-6,
    2 + 10e-6, 1.192092896e-07, 2.2204460492503131e-016,

] + [float('inf'), float('nan')] * 5
NASTY_FLOATS.extend([-x for x in NASTY_FLOATS])
NASTY_FLOATS = list(map(float, NASTY_FLOATS))


class FloatStrategy(SearchStrategy):

    """Generic superclass for strategies which produce floats."""

    def __init__(self, allow_infinity, allow_nan):
        SearchStrategy.__init__(self)
        assert isinstance(allow_infinity, bool)
        assert isinstance(allow_nan, bool)
        self.allow_infinity = allow_infinity
        self.allow_nan = allow_nan

        self.nasty_floats = [f for f in NASTY_FLOATS if self.permitted(f)]
        weights = [
            0.6 * len(self.nasty_floats)
        ] + [0.4] * len(self.nasty_floats)
        self.sampler = d.Sampler(weights)

    def __repr__(self):
        return '%s()' % (self.__class__.__name__,)

    def permitted(self, f):
        assert isinstance(f, float)
        if not self.allow_infinity and math.isinf(f):
            return False
        if not self.allow_nan and math.isnan(f):
            return False
        return True

    def do_draw(self, data):
        while True:
            data.start_example()
            i = self.sampler.sample(data)
            if i == 0:
                result = struct_unpack(b'!d', hbytes(
                    data.draw_bytes(8)))[0]
            else:
                result = self.nasty_floats[i - 1]
                data.write(
                    struct_pack(b'!d', result)
                )
            data.stop_example()
            if self.permitted(result):
                return result


def float_order_key(k):
    return (sign(k), k)


class FixedBoundedFloatStrategy(SearchStrategy):

    """A strategy for floats distributed between two endpoints.

    The conditional distribution tries to produce values clustered
    closer to one of the ends.

    """
    Parameter = namedtuple(
        'Parameter',
        ('cut', 'leftwards')
    )

    def __init__(self, lower_bound, upper_bound):
        SearchStrategy.__init__(self)
        self.lower_bound = float(lower_bound)
        self.upper_bound = float(upper_bound)
        assert not math.isinf(self.upper_bound - self.lower_bound)
        lb = float_order_key(self.lower_bound)
        ub = float_order_key(self.upper_bound)

        self.critical = [
            z for z in (-0.0, 0.0)
            if lb <= float_order_key(z) <= ub
        ]
        self.critical.append(self.lower_bound)
        self.critical.append(self.upper_bound)

    def __repr__(self):
        return 'FixedBoundedFloatStrategy(%s, %s)' % (
            self.lower_bound, self.upper_bound,
        )

    def do_draw(self, data):
        f = self.lower_bound + (
            self.upper_bound - self.lower_bound) * d.fractional_float(data)
        assume(self.lower_bound <= f <= self.upper_bound)
        assume(sign(self.lower_bound) <= sign(f) <= sign(self.upper_bound))
        # Special handling for bounds of -0.0
        for g in [self.lower_bound, self.upper_bound]:
            if f == g:
                f = math.copysign(f, g)
        return f


class ComplexStrategy(MappedSearchStrategy):

    """A strategy over complex numbers, with real and imaginary values
    distributed according to some provided strategy for floating point
    numbers."""

    def __repr__(self):
        return 'ComplexStrategy()'

    def pack(self, value):
        return complex(*value)
