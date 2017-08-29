# Part of p5: A Python package based on Processing
# Copyright (C) 2017 Abhik Pal
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import builtins
import colorsys
import math

from ..pmath import lerp
from ..pmath import constrain

__all__ = ['color_mode', 'Color']

color_parse_mode = 'RGB'
color_range = (255, 255, 255, 255)

def color_mode(mode, max_1=255, max_2=None, max_3=None, max_4=255):
    """Set the color mode of the renderer.

    :param mode: One of {'RGB', 'HSB'} corresponding to Red/Green/Blue
        or Hue/Saturation/Brightness
    :type mode: str

    """
    global color_parse_mode
    global color_range

    if (max_2 is None) or (max_3 is None):
        max_2 = max_1
        max_3 = max_1

    color_range = (max_1, max_2, max_3, max_4)
    color_parse_mode = mode

def parse_color(*args, color_mode='RGB', **kwargs):
    """Parses a color from a range of different input formats.

    This assumes that the args and kwargs are in the following form:

    - gray
    - gray, alpha = ...
    - gray, alpha
    - r, g, b
    - h, s, v
    - r, g, b, a
    - h, s, v, a

    - gray = ...
    - gray = ..., alpha = ...
    - r = ..., g = ..., b = ...,
    - red = ..., green = ..., blue = ...,
    - h = ..., s = ..., b = ...,
    - hue = ..., saturation = ..., brightness = ...,
    - r = ..., g = ..., b = ..., a = ...
    - red = ..., green = ..., blue = ..., alpha = ...
    - h = ..., s = ..., b = ..., a = ...
    - hue = ..., saturation = ..., brightness = ..., alpha = ...

    :param args: The positional arguments that define the color.
    :type args: tuple

    :param kwargs: The keyword arguments that define the color.
    :type kwargs: dict

    :returns: The color parsed as red, green, blue, alpha values.
    :rtype: tuple

    """

    if 'alpha' in kwargs:
        alpha = kwargs['alpha']
    elif 'a' in kwargs:
        alpha = kwargs['a']
    else:
        alpha = 255

    hsb = None
    rgb = None

    if len(args) == 1:
        gray = args[0]
        rgb = gray, gray, gray
    elif len(args) == 2:
        gray, alpha = args
        rgb =  gray, gray, gray
    elif (len(args) == 3) and color_mode.startswith('RGB'):
        rgb = args
    elif (len(args) == 3) and color_mode.startswith('HSB'):
        hsb = args
    elif (len(args) == 4) and color_mode.startswith('RGB'):
        _r, _g, _b, alpha = args
        rgb = (_r, _g, _b)
    elif (len(args) == 4) and color_mode.startswith('HSB'):
        _h, _s, _b, alpha = args
        hsb = (_h, _s. _b)
    elif 'gray' in kwargs:
        gray = kwargs['gray']
        rgb = gray, gray, gray
    elif all(param in kwargs for param in ['red', 'green', 'blue']):
        _r = kwargs['red']
        _g = kwargs['green']
        _b = kwargs['blue']
        rgb = (_r, _g, _b)
    elif all(param in kwargs for param in ['r', 'g', 'b']):
        _r = kwargs['r']
        _g = kwargs['g']
        _b = kwargs['b']
        rgb = (_r, _g, _b)
    elif all(param in kwargs for param in ['hue', 'saturation', 'brightness']):
        _h = kwargs['hue']
        _s = kwargs['saturation']
        _b = kwargs['brightness']
        hsb = (_h, _s, _b)
    elif all(param in kwargs for param in ['h', 's', 'b']):
        _h = kwargs['h']
        _s = kwargs['s']
        _b = kwargs['b']
        hsb = (_h, _s, _b)
    else:
        raise ValueError("Failed to parse color.")

    if not (hsb is None):
        h, s, b = hsb
        h = constrain(h / color_range[0], 0, 1)
        s = constrain(s / color_range[1], 0, 1)
        b = constrain(b / color_range[2], 0, 1)
        red, green, blue = colorsys.hsv_to_rgb(h, s, b)

    if not (rgb is None):
        r, g, b = rgb
        red = constrain(r / color_range[0], 0, 1)
        green = constrain(g / color_range[1], 0, 1)
        blue = constrain(b / color_range[2], 0, 1)

    alpha = constrain(alpha / color_range[3], 0, 1)
    return red, green, blue, alpha

class Color:
    """Represents a color."""
    def __init__(self, *args, color_mode=None, **kwargs):
        if color_mode is None:
            color_mode = color_parse_mode

        if (len(args) == 1) and isinstance(args[0], Color):
           r = args[0]._red
           g = args[0]._green
           b = args[0]._blue
           a = args[0]._alpha
        else:
            r, g, b, a = parse_color(*args, color_mode=color_mode, **kwargs)

        self._red = r
        self._green = g
        self._blue = b
        self._alpha = a

        self._recompute_hsb()

    def _recompute_rgb(self):
        """Recompute the RGB values from HSB values."""
        r, g, b = colorsys.hsv_to_rgb(self._hue, self._saturation, self._brightness)
        self._red = r
        self._greeen = g
        self._blue = b

    def _recompute_hsb(self):
        """Recompute the HSB values from the RGB values."""
        h, s, b = colorsys.rgb_to_hsv(self._red, self._green, self._blue)
        self._hue = h
        self._saturation = s
        self._brightness = b

    def lerp(self, target, amount):
        """Linearly interpolate one color to another by the given amount.

        :param target: The target color to lerp to.
        :type target: Color

        :param amount: The amount by which the color should be lerped
            (should be a float between 0 and 1).
        :type amount: float

        :returns: A new color lerped between the current color and the
            other color.
        :rtype: Color

        """
        lerped = (lerp(s, t, amount) for s, t in zip(self.rgba, target.rgba))
        return Color(*lerped, color_mode='RGB')

    def __repr__(self):
        fvalues = self._red, self._green, self._blue
        return "Color( red={}, green={}, blue={} )".format(*fvalues)

    __str__ = __repr__

    def __eq__(self, other):
        return all(math.isclose(sc, oc)
                   for sc, oc in zip(self.normalized, other.normalized))

    def __neq__(self, other):
        return not all(math.isclose(sc, oc)
                       for sc, oc in zip(self.normalized, other.normalized))

    @property
    def normalized(self):
        """Normalized RGBA color values"""
        return (self._red, self._green, self._blue, self._alpha)

    @property
    def gray(self):
        """The gray-scale value of the color.

        Performs a luminance conversion of the current color to
        grayscale.

        """
        # The formula we use to convert to grayscale is approximate
        # and probably not as accurate as a proper coloremetric
        # conversion. However, the number of calculations required is
        # less and GIMP uses something similar so we should be fine.
        #
        # REFERENCES:
        #
        # - "Converting Color Images to B&W"
        #   <https://www.gimp.org/tutorials/Color2BW/>
        #
        # - "Luma Coding in Video Systems" from "Grayscale"
        #   <https://en.wikipedia.org/wiki/Grayscale#Luma_coding_in_video_systems>
        #
        # - Wikipedia : Grayscale
        #   <https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale>
        #
        # - Conversion to grayscale, sample implementation (StackOverflow)
        # <https://stackoverflow.com/a/15686412>
        norm_gray  = 0.299 * self._red + 0.587 * self._green + 0.144 * self._blue
        return norm_gray * 255

    @gray.setter
    def gray(self, value):
        value = constrain(value / 255, 0, 1)
        self._red = value
        self._green = value
        self._blue = value
        self._recompute_hsb()

    @property
    def alpha(self):
        """The alpha value for the color."""
        return self._alpha * color_range[3]

    @alpha.setter
    def alpha(self, value):
        self._alpha = constrain(value / color_range[3], 0, 1)

    @property
    def rgb(self):
        """
        :returns: Color components in RGB.
        :rtype: tuple
        """
        return (self.red, self.green, self.blue)

    @property
    def rgba(self):
        """
        :returns: Color components in RGBA.
        :rtype: tuple
        """
        return (self.red, self.green, self.blue, self.alpha)


    @property
    def red(self):
        """The red component of the color"""
        return self._red * color_range[0]

    @red.setter
    def red(self, value):
        self._red = constrain(value / color_range[0], 0, 1)
        self._recompute_hsb()

    @property
    def green(self):
        """The green component of the color"""
        return self._green * color_range[1]

    @green.setter
    def green(self, value):
        self._green = constrain(value / color_range[1], 0, 1)
        self._recompute_hsb()

    @property
    def blue(self):
        """The blue component of the color"""
        return self._blue * color_range[2]

    @blue.setter
    def blue(self, value):
        self._blue = constrain(value / color_range[2], 0, 1)
        self._recompute_hsb()

    @property
    def hsb(self):
        """
        :returns: Color components in HSB.
        :rtype: tuple
        """
        return (self._hue, self._saturation, self._brightness)

    @property
    def hsba(self):
        """
        :returns: Color components in HSBA.
        :rtype: tuple
        """
        return (self.hue, self.saturation, self.brightness, self.alpha)

    @property
    def hue(self):
        """The hue component of the color"""
        return self._hue * color_range[0]

    @hue.setter
    def hue(self, value):
        self._hue = constrain(value / color_range[0], 0, 1)
        self._recompute_rgb()

    @property
    def saturation(self):
        """The saturation component of the color"""
        return self._saturation * color_range[1]

    @saturation.setter
    def saturation(self, value):
        self._saturation = constrain(value / color_range[1], 0, 1)
        self._recompute_rgb()

    @property
    def brightness(self):
        """The brightness component of the color"""
        return self._brightness * color_range[2]

    @brightness.setter
    def brightness(self, value):
        self._brightness = constrain(value / color_range[2], 0, 1)
        self._recompute_rgb()

    # ...and some convenient aliases
    r = red
    g = green
    h = hue
    s = saturation
    value = brightness
    v = value

    # `b` is tricky. depending on the current color code, this could
    # either be the brightness value or the blue value.
    @property
    def b(self):
        """The blue or the brightness value (depending on the color mode)."""
        if color_parse_mode== 'RGB':
            return self.blue
        elif color_parse_mode== 'HSB':
            return self.brightness
        else:
            raise ValueError("Unknown color mode {}".format(color_parse_mode))

    @b.setter
    def b(self, value):
        if color_parse_mode== 'RGB':
            self.blue = value
        elif color_parse_mode== 'HSB':
            self.brightness = value
        else:
            raise ValueError("Unknown color mode {}".format(color_parse_mode))

    @property
    def hex(self):
        """
        :returns: Color as a hex value
        :rtype: str
        """
        raise NotImplementedError()
