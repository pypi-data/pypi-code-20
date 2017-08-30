#-*- coding: utf-8 -*-

"""
Copyright (C) 2011-2017 Michal Goral.

This file is part of Subconvert

Subconvert is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Subconvert is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Subconvert. If not, see <http://www.gnu.org/licenses/>.
"""

import re
import functools

from subconvert.utils.SubException import SubAssert
from subconvert.utils.Locale import _

_timeexpr = re.compile(r"""(?P<sign>[+-]?)
                           (?P<h>\d+):
                           (?P<m>[0-5][0-9]):
                           (?P<s>[0-5][0-9])
                           (?:$|\.(?P<ms>\d{1,3}))""", re.VERBOSE)


def ms2f(ms, fps):
    """Converts milliseconds to frame."""
    return round(ms * fps / 1000)

def f2ms(frame, fps):
    """Converts frame to milliseconds."""
    return round(frame / fps * 1000)

class FrameTimeType:
    """Used to determine if frame or time should be changed on FPS change."""
    Undefined = 0
    Frame = 1
    Time = 2

@functools.total_ordering
class FrameTime():
    """Class defining a FrameTime object which consists of frame and time metrics (and fps as well)."""

    __slots__ = ('_fps', '_ms', '_frame', '_origin')

    def __init__(self, ms, fps):
        """Constructs FrameTime object with a given FPS value."""
        if fps <= 0:
            raise ValueError("Incorrect FPS value: %s." % fps)

        self._origin = FrameTimeType.Time
        self._fps = float(fps)
        self._ms = int(ms)
        self._frame = ms2f(self._ms, self._fps)

    @classmethod
    def InitFrames(cls, frame, fps):
        frame = int(frame)
        ft = FrameTime(0, fps)
        ft._frame = frame
        ft._ms = f2ms(frame, ft.fps)
        ft._origin = FrameTimeType.Frame
        return ft

    @classmethod
    def InitTimeStr(cls, timestr, fps):
        """Inits FrameTimejfrom a string representation.

        Example:
          FrameTime.InitTimeStr("1:01:01.100", 25)
        """
        time = _timeexpr.match(timestr)
        if time is None:
            raise ValueError("Incorrect time format.")

        sign = 1
        if time.group('sign') is not None:
            sign = int('%s1' % time.group('sign'))

        if time.group('ms') is not None:
            # ljust explanation:
            # 10.1 != 10.001
            # 10.1 == 10.100
            ms = int(time.group('ms').ljust(3, '0'))
        else:
            ms = 0

        seconds = int(time.group('s'))
        minutes = int(time.group('m'))
        hours = int(time.group('h'))

        total_ms = sign * (1000 * (3600 * hours + 60 * minutes + seconds) + ms)
        return FrameTime(total_ms, fps)

    def clone(self):
        return FrameTime(self.ms, self.fps)

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, newFps):
        if newFps > 0:
            self._fps = float(newFps)
        else:
            raise ValueError("Incorrect FPS value: %s." % newFps)

        if self._origin == FrameTimeType.Time:
            self._frame = ms2f(self.ms, self.fps)
        else:
            self._ms = f2ms(self.frame, self.fps)

    @property
    def frame(self):
        return self._frame

    @property
    def ms(self):
        return self._ms

    @property
    def time(self):
        hours = int(self.ms / 3600000)
        counted = hours * 3600000
        minutes = int((self.ms - counted) / 60000)
        counted += minutes * 60000
        seconds = int((self.ms - counted) / 1000)
        counted += seconds * 1000
        ms = int(self.ms - counted)

        return { \
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds,
            'milliseconds': ms
        }

    def toStr(self, strType="time"):
        """Convert FrameTime to string representation"""
        if strType == "time":
            t = self.time
            fmt = dict(sign='' if self.ms >= 0 else '-',
                       h=abs(t['hours']),
                       m=abs(t['minutes']),
                       s=abs(t['seconds']),
                       ms=abs(t['milliseconds']))
            return "%(sign)s%(h)d:%(m)02d:%(s)02d.%(ms)03d" % fmt
        elif strType == "frame":
            return "%s" % self.frame
        else:
            raise AttributeError("Incorrect string type: '%s'" % strType)

    def __eq__(self, other):
        SubAssert(self._fps == other._fps, _("FPS values are not equal"))
        return self.ms == other.ms

    def __lt__(self, other):
        SubAssert(self._fps == other._fps, _("FPS values are not equal"))
        return self.ms < other.ms

    def __add__(self, other):
        """Defines FrameTime + FrameTime"""
        SubAssert(self._fps == other._fps, _("FPS values are not equal"))
        return FrameTime(self.ms + other.ms, self.fps)

    def __sub__(self, other):
        """Defines FrameTime - FrameTime"""
        SubAssert(self._fps == other._fps, _("FPS values are not equal"))
        return FrameTime(self.ms - other.ms, self.fps)

    def __mul__(self, val):
        """Defines FrameTime * number"""
        return FrameTime(self.ms * val, self.fps)

    def __div__(self, val):
        """Defines FrameTime / number"""
        return FrameTime(round(self.ms / val), self.fps)

    def __str__(self):
        """Defines str(FrameTime)"""
        return "t: %s; f: %s" % (self.toStr(), self.toStr('frame'))

    def __repr__(self):
        return "FrameTime(id=%s, ms=%s, f=%s, fps=%s)" % \
               (id(self), self.ms, self.frame, self.fps)
