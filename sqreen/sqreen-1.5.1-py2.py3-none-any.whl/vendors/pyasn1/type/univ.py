#
# This file is part of pyasn1 software.
#
# Copyright (c) 2005-2017, Ilya Etingof <etingof@gmail.com>
# License: http://pyasn1.sf.net/license.html
#
import sys
import math
from pyasn1.type import base, tag, constraint, namedtype, namedval, tagmap
from pyasn1.codec.ber import eoo
from pyasn1.compat import octets, integer, binary
from pyasn1 import error

NoValue = base.NoValue
noValue = NoValue()

__all__ = ['Integer', 'Boolean', 'BitString', 'OctetString', 'Null',
           'ObjectIdentifier', 'Real', 'Enumerated', 'SequenceOfAndSetOfBase', 'SequenceOf',
           'SetOf', 'SequenceAndSetBase', 'Sequence', 'Set', 'Choice', 'Any',
           'NoValue', 'noValue']

# "Simple" ASN.1 types (yet incomplete)


class Integer(base.AbstractSimpleAsn1Item):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type Python :class:`int` objects.

    Parameters
    ----------
    value : :class:`int`, :class:`str` or |ASN.1| object
        Python integer or string literal or |ASN.1| class instance.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
        Object representing non-default symbolic aliases for numbers

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.
    """
    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x02)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.namedval.NamedValues` object
    #: representing symbolic aliases for numbers
    namedValues = namedval.NamedValues()

    # Optimization for faster codec lookup
    typeId = base.AbstractSimpleAsn1Item.getTypeId()

    def __init__(self, value=noValue, **kwargs):
        if 'namedValues' not in kwargs:
            kwargs['namedValues'] = self.namedValues

        base.AbstractSimpleAsn1Item.__init__(self, value, **kwargs)

    def __repr__(self):
        if self.namedValues is not self.__class__.namedValues:
            return '%s, %r)' % (base.AbstractSimpleAsn1Item.__repr__(self)[:-1], self.namedValues)
        else:
            return base.AbstractSimpleAsn1Item.__repr__(self)

    def __and__(self, value):
        return self.clone(self._value & value)

    def __rand__(self, value):
        return self.clone(value & self._value)

    def __or__(self, value):
        return self.clone(self._value | value)

    def __ror__(self, value):
        return self.clone(value | self._value)

    def __xor__(self, value):
        return self.clone(self._value ^ value)

    def __rxor__(self, value):
        return self.clone(value ^ self._value)

    def __lshift__(self, value):
        return self.clone(self._value << value)

    def __rshift__(self, value):
        return self.clone(self._value >> value)

    def __add__(self, value):
        return self.clone(self._value + value)

    def __radd__(self, value):
        return self.clone(value + self._value)

    def __sub__(self, value):
        return self.clone(self._value - value)

    def __rsub__(self, value):
        return self.clone(value - self._value)

    def __mul__(self, value):
        return self.clone(self._value * value)

    def __rmul__(self, value):
        return self.clone(value * self._value)

    def __mod__(self, value):
        return self.clone(self._value % value)

    def __rmod__(self, value):
        return self.clone(value % self._value)

    def __pow__(self, value, modulo=None):
        return self.clone(pow(self._value, value, modulo))

    def __rpow__(self, value):
        return self.clone(pow(value, self._value))

    def __floordiv__(self, value):
        return self.clone(self._value // value)

    def __rfloordiv__(self, value):
        return self.clone(value // self._value)

    if sys.version_info[0] <= 2:
        def __div__(self, value):
            if isinstance(value, float):
                return Real(self._value / value)
            else:
                return self.clone(self._value / value)

        def __rdiv__(self, value):
            if isinstance(value, float):
                return Real(value / self._value)
            else:
                return self.clone(value / self._value)
    else:
        def __truediv__(self, value):
            return Real(self._value / value)

        def __rtruediv__(self, value):
            return Real(value / self._value)

        def __divmod__(self, value):
            return self.clone(divmod(self._value, value))

        def __rdivmod__(self, value):
            return self.clone(divmod(value, self._value))

        __hash__ = base.AbstractSimpleAsn1Item.__hash__

    def __int__(self):
        return int(self._value)

    if sys.version_info[0] <= 2:
        def __long__(self):
            return long(self._value)

    def __float__(self):
        return float(self._value)

    def __abs__(self):
        return self.clone(abs(self._value))

    def __index__(self):
        return int(self._value)

    def __pos__(self):
        return self.clone(+self._value)

    def __neg__(self):
        return self.clone(-self._value)

    def __invert__(self):
        return self.clone(~self._value)

    def __round__(self, n=0):
        r = round(self._value, n)
        if n:
            return self.clone(r)
        else:
            return r

    def __floor__(self):
        return math.floor(self._value)

    def __ceil__(self):
        return math.ceil(self._value)

    if sys.version_info[0:2] > (2, 5):
        def __trunc__(self):
            return self.clone(math.trunc(self._value))

    def __lt__(self, value):
        return self._value < value

    def __le__(self, value):
        return self._value <= value

    def __eq__(self, value):
        return self._value == value

    def __ne__(self, value):
        return self._value != value

    def __gt__(self, value):
        return self._value > value

    def __ge__(self, value):
        return self._value >= value

    def prettyIn(self, value):
        try:
            return int(value)

        except ValueError:
            try:
                return self.namedValues[value]

            except KeyError:
                raise error.PyAsn1Error(
                    'Can\'t coerce %r into integer: %s' % (value, sys.exc_info()[1])
                )

    def prettyOut(self, value):
        try:
            return repr(self.namedValues[value])

        except KeyError:
            return str(value)

    def clone(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *clone()* method will replace corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`int`, :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        tagSet: :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tag(s) to use in new object instead of inheriting from the caller

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Object representing ASN.1 subtype constraint(s) to use in new object instead of inheriting from the caller

        namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
            Object representing symbolic aliases for numbers to use instead of inheriting from caller

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.clone(self, value, **kwargs)

    def subtype(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *subtype()* method will be added to the corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`int`, :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of 
            inheriting one from the caller.

        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Add ASN.1 constraints object to one of the caller, then
            use the result as new object's ASN.1 constraints.

        namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
            Add given object representing symbolic aliases for numbers
            to one of the caller, then use the result as new object's
            named numbers.

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.subtype(self, value, **kwargs)

    # backward compatibility

    def getNamedValues(self):
        return self.namedValues


class Boolean(Integer):
    __doc__ = Integer.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x01),
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = Integer.subtypeSpec + constraint.SingleValueConstraint(0, 1)

    #: Default :py:class:`~pyasn1.type.namedval.NamedValues` object
    #: representing symbolic aliases for numbers
    namedValues = namedval.NamedValues(('False', 0), ('True', 1))

    # Optimization for faster codec lookup
    typeId = Integer.getTypeId()


class BitString(base.AbstractSimpleAsn1Item):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type both Python :class:`tuple` (as a tuple
    of bits) and :class:`int` objects.

    Parameters
    ----------
    value : :class:`int`, :class:`str` or |ASN.1| object
        Python integer or string literal representing binary or hexadecimal
        number or sequence of integer bits or |ASN.1| object.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
        Object representing non-default symbolic aliases for numbers

    binValue: :py:class:`str`
        Binary string initializer to use instead of the *value*.
        Example: '10110011'.

    hexValue: :py:class:`str`
        Hexadecimal string initializer to use instead of the *value*.
        Example: 'DEADBEEF'.

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.
    """
    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x03)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.namedval.NamedValues` object
    #: representing symbolic aliases for numbers
    namedValues = namedval.NamedValues()

    # Optimization for faster codec lookup
    typeId = base.AbstractSimpleAsn1Item.getTypeId()

    defaultBinValue = defaultHexValue = noValue

    if sys.version_info[0] < 3:
        SizedIntegerBase = long
    else:
        SizedIntegerBase = int

    class SizedInteger(SizedIntegerBase):
        bitLength = leadingZeroBits = None

        def setBitLength(self, bitLength):
            self.bitLength = bitLength
            self.leadingZeroBits = max(bitLength - integer.bitLength(self), 0)
            return self

        def __len__(self):
            if self.bitLength is None:
                self.setBitLength(integer.bitLength(self))

            return self.bitLength

    def __init__(self, value=noValue, **kwargs):
        if value is noValue or value is None:
            if kwargs:
                try:
                    value = self.fromBinaryString(kwargs.pop('binValue'))

                except KeyError:
                    pass

                try:
                    value = self.fromHexString(kwargs.pop('hexValue'))

                except KeyError:
                    pass

        if value is noValue or value is None:
            if self.defaultBinValue is not noValue:
                value = self.fromBinaryString(self.defaultBinValue)

            elif self.defaultHexValue is not noValue:
                value = self.fromHexString(self.defaultHexValue)

        if 'namedValues' not in kwargs:
            kwargs['namedValues'] = self.namedValues

        base.AbstractSimpleAsn1Item.__init__(self, value, **kwargs)

    def clone(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *clone()* method will replace corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value : :class:`int`, :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        tagSet: :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tag(s) to use in new object instead of inheriting from the caller

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Object representing ASN.1 subtype constraint(s) to use in new object instead of inheriting from the caller

        namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
            Class instance representing BitString type enumerations

        binValue: :py:class:`str`
            Binary string initializer to use instead of the *value*.
            Example: '10110011'.

        hexValue: :py:class:`str`
            Hexadecimal string initializer to use instead of the *value*.
            Example: 'DEADBEEF'.

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.clone(self, value, **kwargs)

    def subtype(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *subtype()* method will be added to the corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`int`, :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Add ASN.1 constraints object to one of the caller, then
            use the result as new object's ASN.1 constraints.

        namedValues: :py:class:`~pyasn1.type.namedval.NamedValues`
            Add given object representing symbolic aliases for numbers
            to one of the caller, then use the result as new object's
            named numbers.

        binValue: :py:class:`str`
            Binary string initializer to use instead of the *value*.
            Example: '10110011'.

        hexValue: :py:class:`str`
            Hexadecimal string initializer to use instead of the *value*.
            Example: 'DEADBEEF'.

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.subtype(self, value, **kwargs)

    def __str__(self):
        return self.asBinary()

    def __eq__(self, other):
        other = self.prettyIn(other)
        return self is other or self._value == other and len(self._value) == len(other)

    def __ne__(self, other):
        other = self.prettyIn(other)
        return self._value != other or len(self._value) != len(other)

    def __lt__(self, other):
        other = self.prettyIn(other)
        return len(self._value) < len(other) or len(self._value) == len(other) and self._value < other

    def __le__(self, other):
        other = self.prettyIn(other)
        return len(self._value) <= len(other) or len(self._value) == len(other) and self._value <= other

    def __gt__(self, other):
        other = self.prettyIn(other)
        return len(self._value) > len(other) or len(self._value) == len(other) and self._value > other

    def __ge__(self, other):
        other = self.prettyIn(other)
        return len(self._value) >= len(other) or len(self._value) == len(other) and self._value >= other

    # Immutable sequence object protocol

    def __len__(self):
        return len(self._value)

    def __getitem__(self, i):
        if i.__class__ is slice:
            return self.clone([self[x] for x in range(*i.indices(len(self)))])
        else:
            length = len(self._value) - 1
            if i > length or i < 0:
                raise IndexError('bit index out of range')
            return (self._value >> (length - i)) & 1

    def __iter__(self):
        length = len(self._value)
        while length:
            length -= 1
            yield (self._value >> length) & 1

    def __reversed__(self):
        return reversed(tuple(self))

    # arithmetic operators

    def __add__(self, value):
        value = self.prettyIn(value)
        return self.clone(self.SizedInteger(self._value << len(value) | value).setBitLength(len(self._value) + len(value)))

    def __radd__(self, value):
        value = self.prettyIn(value)
        return self.clone(self.SizedInteger(value << len(self._value) | self._value).setBitLength(len(self._value) + len(value)))

    def __mul__(self, value):
        bitString = self._value
        while value > 1:
            bitString <<= len(self._value)
            bitString |= self._value
            value -= 1
        return self.clone(bitString)

    def __rmul__(self, value):
        return self * value

    def __lshift__(self, count):
        return self.clone(self.SizedInteger(self._value << count).setBitLength(len(self._value) + count))

    def __rshift__(self, count):
        return self.clone(self.SizedInteger(self._value >> count).setBitLength(max(0, len(self._value) - count)))

    def __int__(self):
        return self._value

    def __float__(self):
        return float(self._value)

    if sys.version_info[0] < 3:
        def __long__(self):
            return self._value

    def asNumbers(self):
        """Get |ASN.1| value as a sequence of 8-bit integers.

        If |ASN.1| object length is not a multiple of 8, result
        will be left-padded with zeros.
        """
        return tuple(octets.octs2ints(self.asOctets()))

    def asOctets(self):
        """Get |ASN.1| value as a sequence of octets.

        If |ASN.1| object length is not a multiple of 8, result
        will be left-padded with zeros.
        """
        return integer.to_bytes(self._value, length=len(self))

    def asInteger(self):
        """Get |ASN.1| value as a single integer value.
        """
        return self._value

    def asBinary(self):
        """Get |ASN.1| value as a text string of bits.
        """
        binString = binary.bin(self._value)[2:]
        return '0' * (len(self._value) - len(binString)) + binString

    @classmethod
    def fromHexString(cls, value):
        """Create a |ASN.1| object initialized from the hex string.
        
        Parameters
        ----------
        value: :class:`str`
            Text string like 'DEADBEEF'
        """
        try:
            return cls.SizedInteger(value, 16).setBitLength(len(value) * 4)

        except ValueError:
            raise error.PyAsn1Error('%s.fromHexString() error: %s' % (cls.__name__, sys.exc_info()[1]))

    @classmethod
    def fromBinaryString(cls, value):
        """Create a |ASN.1| object initialized from a string of '0' and '1'.

        Parameters
        ----------
        value: :class:`str`
            Text string like '1010111'
        """
        try:
            return cls.SizedInteger(value or '0', 2).setBitLength(len(value))

        except ValueError:
            raise error.PyAsn1Error('%s.fromBinaryString() error: %s' % (cls.__name__, sys.exc_info()[1]))

    @classmethod
    def fromOctetString(cls, value, padding=0):
        """Create a |ASN.1| object initialized from a string.

        Parameters
        ----------
        value: :class:`str` (Py2) or :class:`bytes` (Py3)
            Text string like '\\\\x01\\\\xff' (Py2) or b'\\\\x01\\\\xff' (Py3)
        """
        return cls(cls.SizedInteger(integer.from_bytes(value) >> padding).setBitLength(len(value) * 8 - padding))

    def prettyIn(self, value):
        if octets.isStringType(value):
            if not value:
                return self.SizedInteger(0).setBitLength(0)

            elif value[0] == '\'':  # "'1011'B" -- ASN.1 schema representation (deprecated)
                if value[-2:] == '\'B':
                    return self.fromBinaryString(value[1:-2])
                elif value[-2:] == '\'H':
                    return self.fromHexString(value[1:-2])
                else:
                    raise error.PyAsn1Error(
                        'Bad BIT STRING value notation %s' % (value,)
                    )

            elif self.namedValues and not value.isdigit():  # named bits like 'Urgent, Active'
                names = [x.strip() for x in value.split(',')]

                try:

                    bitPositions = [self.namedValues[name] for name in names]

                except KeyError:
                    raise error.PyAsn1Error('unknown bit name(s) in %r' % (names,))

                rightmostPosition = max(bitPositions)

                number = 0
                for bitPosition in bitPositions:
                    number |= 1 << (rightmostPosition - bitPosition)

                return self.SizedInteger(number).setBitLength(rightmostPosition + 1)

            elif value.startswith('0x'):
                return self.fromHexString(value[2:])

            elif value.startswith('0b'):
                return self.fromBinaryString(value[2:])

            else:  # assume plain binary string like '1011'
                return self.fromBinaryString(value)

        elif isinstance(value, (tuple, list)):
            return self.fromBinaryString(''.join([b and '1' or '0' for b in value]))

        elif isinstance(value, (self.SizedInteger, BitString)):
            return self.SizedInteger(value).setBitLength(len(value))

        elif isinstance(value, intTypes):
            return self.SizedInteger(value)

        else:
            raise error.PyAsn1Error(
                'Bad BitString initializer type \'%s\'' % (value,)
            )

    def prettyOut(self, value):
        return '\'%s\'' % str(self)


try:
    # noinspection PyStatementEffect
    all

except NameError:  # Python 2.4
    # noinspection PyShadowingBuiltins
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True


class OctetString(base.AbstractSimpleAsn1Item):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type Python 2 :class:`str` or Python 3 :class:`bytes`.
    When used in Unicode context, |ASN.1| type assumes "|encoding|" serialization.

    Parameters
    ----------
    value : :class:`str`, :class:`bytes` or |ASN.1| object
        string (Python 2) or bytes (Python 3), alternatively unicode object
        (Python 2) or string (Python 3) representing character string to be
        serialized into octets (note `encoding` parameter) or |ASN.1| object.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    encoding: :py:class:`str`
        Unicode codec ID to encode/decode :class:`unicode` (Python 2) or
        :class:`str` (Python 3) the payload when |ASN.1| object is used
        in text string context.

    binValue: :py:class:`str`
        Binary string initializer to use instead of the *value*.
        Example: '10110011'.
        
    hexValue: :py:class:`str`
        Hexadecimal string initializer to use instead of the *value*.
        Example: 'DEADBEEF'.

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.
    """
    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x04)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    # Optimization for faster codec lookup
    typeId = base.AbstractSimpleAsn1Item.getTypeId()

    defaultBinValue = defaultHexValue = noValue
    encoding = 'iso-8859-1'

    def __init__(self, value=noValue, **kwargs):
        if kwargs:
            if value is noValue or value is None:
                try:
                    value = self.fromBinaryString(kwargs.pop('binValue'))

                except KeyError:
                    pass

                try:
                    value = self.fromHexString(kwargs.pop('hexValue'))

                except KeyError:
                    pass

        if value is noValue or value is None:
            if self.defaultBinValue is not noValue:
                value = self.fromBinaryString(self.defaultBinValue)

            elif self.defaultHexValue is not noValue:
                value = self.fromHexString(self.defaultHexValue)

        if 'encoding' not in kwargs:
            kwargs['encoding'] = self.encoding

        base.AbstractSimpleAsn1Item.__init__(self, value, **kwargs)

    def clone(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *clone()* method will replace corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value : :class:`str`, :class:`bytes` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        tagSet: :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tag(s) to use in new object instead of inheriting from the caller

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Object representing ASN.1 subtype constraint(s) to use in new object instead of inheriting from the caller

        encoding: :py:class:`str`
            Unicode codec ID to encode/decode :class:`unicode` (Python 2)
            or :class:`str` (Python 3) the payload when |ASN.1|
            object is used in string context.

        binValue: :py:class:`str`
            Binary string initializer. Example: '10110011'.
        
        hexValue: :py:class:`str`
            Hexadecimal string initializer. Example: 'DEADBEEF'.

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.clone(self, value, **kwargs)

    def subtype(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *subtype()* method will be added to the corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value : :class:`str`, :class:`bytes` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to |ASN.1| object tag set
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to |ASN.1| object tag set
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Add ASN.1 constraints object to one of the caller, then
            use the result as new object's ASN.1 constraints.

        encoding: :py:class:`str`
            Unicode codec ID to encode/decode :class:`unicode` (Python 2)
            or :class:`str` (Python 3) the payload when *OctetString*
            object is used in string context.

        binValue: :py:class:`str`
            Binary string initializer. Example: '10110011'.
        
        hexValue: :py:class:`str`
            Hexadecimal string initializer. Example: 'DEADBEEF'.

        Returns
        -------
        :
             new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.subtype(self, value, **kwargs)

    if sys.version_info[0] <= 2:
        def prettyIn(self, value):
            if isinstance(value, str):
                return value
            elif isinstance(value, unicode):
                try:
                    return value.encode(self.encoding)
                except (LookupError, UnicodeEncodeError):
                    raise error.PyAsn1Error(
                        'Can\'t encode string \'%s\' with \'%s\' codec' % (value, self.encoding)
                    )
            elif isinstance(value, (tuple, list)):
                try:
                    return ''.join([chr(x) for x in value])
                except ValueError:
                    raise error.PyAsn1Error(
                        'Bad %s initializer \'%s\'' % (self.__class__.__name__, value)
                    )
            else:
                return str(value)

        def __str__(self):
            return str(self._value)

        def __unicode__(self):
            try:
                return self._value.decode(self.encoding)

            except UnicodeDecodeError:
                raise error.PyAsn1Error(
                    'Can\'t decode string \'%s\' with \'%s\' codec' % (self._value, self.encoding)
                )

        def asOctets(self):
            return str(self._value)

        def asNumbers(self):
            return tuple([ord(x) for x in self._value])

    else:
        def prettyIn(self, value):
            if isinstance(value, bytes):
                return value
            elif isinstance(value, str):
                try:
                    return value.encode(self.encoding)
                except UnicodeEncodeError:
                    raise error.PyAsn1Error(
                        'Can\'t encode string \'%s\' with \'%s\' codec' % (value, self.encoding)
                    )
            elif isinstance(value, OctetString):  # a shortcut, bytes() would work the same way
                return value.asOctets()
            elif isinstance(value, base.AbstractSimpleAsn1Item):  # this mostly targets Integer objects
                return self.prettyIn(str(value))
            elif isinstance(value, (tuple, list)):
                return self.prettyIn(bytes(value))
            else:
                return bytes(value)

        def __str__(self):
            try:
                return self._value.decode(self.encoding)

            except UnicodeDecodeError:
                raise error.PyAsn1Error(
                    'Can\'t decode string \'%s\' with \'%s\' codec at \'%s\'' % (self._value, self.encoding, self.__class__.__name__)
                )

        def __bytes__(self):
            return bytes(self._value)

        def asOctets(self):
            return bytes(self._value)

        def asNumbers(self):
            return tuple(self._value)

    def prettyOut(self, value):
        if sys.version_info[0] <= 2:
            numbers = tuple((ord(x) for x in value))
        else:
            numbers = tuple(value)
        for x in numbers:
            if x < 32 or x > 126:
                return '0x' + ''.join(('%.2x' % x for x in numbers))
        else:
            try:
                return value.decode(self.encoding)

            except UnicodeDecodeError:
                raise error.PyAsn1Error(
                    "Can't decode string '%s' with '%s' codec at '%s'" % (value, self.encoding, self.__class__.__name__)
                )

    @staticmethod
    def fromBinaryString(value):
        """Create a |ASN.1| object initialized from a string of '0' and '1'.

        Parameters
        ----------
        value: :class:`str`
            Text string like '1010111'
        """
        bitNo = 8
        byte = 0
        r = []
        for v in value:
            if bitNo:
                bitNo -= 1
            else:
                bitNo = 7
                r.append(byte)
                byte = 0
            if v in ('0', '1'):
                v = int(v)
            else:
                raise error.PyAsn1Error(
                    'Non-binary OCTET STRING initializer %s' % (v,)
                )
            byte |= v << bitNo

        r.append(byte)

        return octets.ints2octs(r)

    @staticmethod
    def fromHexString(value):
        """Create a |ASN.1| object initialized from the hex string.

        Parameters
        ----------
        value: :class:`str`
            Text string like 'DEADBEEF'
        """
        r = []
        p = []
        for v in value:
            if p:
                r.append(int(p + v, 16))
                p = None
            else:
                p = v
        if p:
            r.append(int(p + '0', 16))

        return octets.ints2octs(r)

    def __repr__(self):
        r = []
        doHex = False
        if self._value is not self.defaultValue:
            for x in self.asNumbers():
                if x < 32 or x > 126:
                    doHex = True
                    break
            if not doHex:
                r.append('%r' % (self._value,))
        if self.tagSet is not self.__class__.tagSet:
            r.append('tagSet=%r' % (self.tagSet,))
        if self.subtypeSpec is not self.__class__.subtypeSpec:
            r.append('subtypeSpec=%r' % (self.subtypeSpec,))
        if self.encoding is not self.__class__.encoding:
            r.append('encoding=%r' % (self.encoding,))
        if doHex:
            r.append('hexValue=%r' % ''.join(['%.2x' % x for x in self.asNumbers()]))
        return '%s(%s)' % (self.__class__.__name__, ', '.join(r))

    # Immutable sequence object protocol

    def __len__(self):
        return len(self._value)

    def __getitem__(self, i):
        if i.__class__ is slice:
            return self.clone(self._value[i])
        else:
            return self._value[i]

    def __iter__(self):
        return iter(self._value)

    def __contains__(self, value):
        return value in self._value

    def __add__(self, value):
        return self.clone(self._value + self.prettyIn(value))

    def __radd__(self, value):
        return self.clone(self.prettyIn(value) + self._value)

    def __mul__(self, value):
        return self.clone(self._value * value)

    def __rmul__(self, value):
        return self * value

    def __int__(self):
        return int(self._value)

    def __float__(self):
        return float(self._value)

    def __reversed__(self):
        return reversed(self._value)


class Null(OctetString):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type Python :class:`str` objects (always empty).

    Parameters
    ----------
    value : :class:`str` or :py:class:`~pyasn1.type.univ.Null` object
        Python empty string literal or *Null* class instance.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.
    """
    defaultValue = ''.encode()  # This is tightly constrained

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x05)
    )
    subtypeSpec = OctetString.subtypeSpec + constraint.SingleValueConstraint(octets.str2octs(''))

    # Optimization for faster codec lookup
    typeId = OctetString.getTypeId()

    def clone(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *clone()* method will replace corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of 
            inheriting one from the caller.

        tagSet: :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tag(s) to use in new object instead of inheriting from the caller

        Returns
        -------
        : :py:class:`~pyasn1.type.univ.Null`
            new instance of NULL type/value
        """
        return OctetString.clone(self, value, **kwargs)

    def subtype(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *subtype()* method will be added to the corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`int`, :class:`str` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        Returns
        -------
        : :py:class:`~pyasn1.type.univ.Null`
            new instance of NULL type/value
        """
        return OctetString.subtype(self, value, **kwargs)


if sys.version_info[0] <= 2:
    intTypes = (int, long)
else:
    intTypes = (int,)

numericTypes = intTypes + (float,)


class ObjectIdentifier(base.AbstractSimpleAsn1Item):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type Python :class:`tuple` objects (tuple of non-negative integers).

    Parameters
    ----------
    value: :class:`tuple`, :class:`str` or |ASN.1| object
        Python sequence of :class:`int` or string literal or |ASN.1| object.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.
    """
    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x06)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    # Optimization for faster codec lookup
    typeId = base.AbstractSimpleAsn1Item.getTypeId()

    def __add__(self, other):
        return self.clone(self._value + other)

    def __radd__(self, other):
        return self.clone(other + self._value)

    def asTuple(self):
        return self._value

    # Sequence object protocol

    def __len__(self):
        return len(self._value)

    def __getitem__(self, i):
        if i.__class__ is slice:
            return self.clone(self._value[i])
        else:
            return self._value[i]

    def __iter__(self):
        return iter(self._value)

    def __contains__(self, value):
        return value in self._value

    def __str__(self):
        return self.prettyPrint()

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.prettyPrint())

    def index(self, suboid):
        return self._value.index(suboid)

    def isPrefixOf(self, other):
        """Indicate if this |ASN.1| object is a prefix of other |ASN.1| object.

        Parameters
        ----------
        other: |ASN.1| object
            |ASN.1| object

        Returns
        -------
        : :class:`bool`
            :class:`True` if this |ASN.1| object is a parent (e.g. prefix) of the other |ASN.1| object
            or :class:`False` otherwise.
        """
        l = len(self)
        if l <= len(other):
            if self._value[:l] == other[:l]:
                return True
        return False

    def prettyIn(self, value):
        if isinstance(value, ObjectIdentifier):
            return tuple(value)
        elif octets.isStringType(value):
            if '-' in value:
                raise error.PyAsn1Error(
                    'Malformed Object ID %s at %s: %s' % (value, self.__class__.__name__, sys.exc_info()[1])
                )
            try:
                return tuple([int(subOid) for subOid in value.split('.') if subOid])
            except ValueError:
                raise error.PyAsn1Error(
                    'Malformed Object ID %s at %s: %s' % (value, self.__class__.__name__, sys.exc_info()[1])
                )

        try:
            tupleOfInts = tuple([int(subOid) for subOid in value if subOid >= 0])

        except (ValueError, TypeError):
            raise error.PyAsn1Error(
                'Malformed Object ID %s at %s: %s' % (value, self.__class__.__name__, sys.exc_info()[1])
            )

        if len(tupleOfInts) == len(value):
            return tupleOfInts

        raise error.PyAsn1Error('Malformed Object ID %s at %s' % (value, self.__class__.__name__))

    def prettyOut(self, value):
        return '.'.join([str(x) for x in value])


class Real(base.AbstractSimpleAsn1Item):
    """Create |ASN.1| type or object.

    |ASN.1| objects are immutable and duck-type Python :class:`float` objects.
    Additionally, |ASN.1| objects behave like a :class:`tuple` in which case its
    elements are mantissa, base and exponent.

    Parameters
    ----------
    value: :class:`tuple`, :class:`float` or |ASN.1| object
        Python sequence of :class:`int` (representing mantissa, base and
        exponent) or float instance or *Real* class instance.

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    Raises
    ------
    : :py:class:`pyasn1.error.PyAsn1Error`
        On constraint violation or bad initializer.

    """
    binEncBase = None  # binEncBase = 16 is recommended for large numbers

    try:
        _plusInf = float('inf')
        _minusInf = float('-inf')
        _inf = (_plusInf, _minusInf)
    except ValueError:
        # Infinity support is platform and Python dependent
        _plusInf = _minusInf = None
        _inf = ()

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x09)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    # Optimization for faster codec lookup
    typeId = base.AbstractSimpleAsn1Item.getTypeId()

    def clone(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *clone()* method will replace corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`tuple`, :class:`float` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        tagSet: :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tag(s) to use in new object instead of inheriting from the caller

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
            Object representing ASN.1 subtype constraint(s) to use in new object instead of inheriting from the caller

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.clone(self, value, **kwargs)

    def subtype(self, value=noValue, **kwargs):
        """Create a copy of a |ASN.1| type or object.

        Any parameters to the *subtype()* method will be added to the corresponding
        properties of the |ASN.1| object.

        Parameters
        ----------
        value: :class:`tuple`, :class:`float` or |ASN.1| object
            Initialization value to pass to new ASN.1 object instead of
            inheriting one from the caller.

        implicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Implicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        explicitTag: :py:class:`~pyasn1.type.tag.Tag`
            Explicitly apply given ASN.1 tag object to caller's 
            :py:class:`~pyasn1.type.tag.TagSet`, then use the result as
            new object's ASN.1 tag(s).

        subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
             Object representing ASN.1 subtype constraint(s) to use in new object instead of inheriting from the caller

        Returns
        -------
        :
            new instance of |ASN.1| type/value
        """
        return base.AbstractSimpleAsn1Item.subtype(self, value, **kwargs)

    @staticmethod
    def __normalizeBase10(value):
        m, b, e = value
        while m and m % 10 == 0:
            m /= 10
            e += 1
        return m, b, e

    def prettyIn(self, value):
        if isinstance(value, tuple) and len(value) == 3:
            if not isinstance(value[0], numericTypes) or \
                    not isinstance(value[1], intTypes) or \
                    not isinstance(value[2], intTypes):
                raise error.PyAsn1Error('Lame Real value syntax: %s' % (value,))
            if isinstance(value[0], float) and \
                    self._inf and value[0] in self._inf:
                return value[0]
            if value[1] not in (2, 10):
                raise error.PyAsn1Error(
                    'Prohibited base for Real value: %s' % (value[1],)
                )
            if value[1] == 10:
                value = self.__normalizeBase10(value)
            return value
        elif isinstance(value, intTypes):
            return self.__normalizeBase10((value, 10, 0))
        elif isinstance(value, float) or octets.isStringType(value):
            if octets.isStringType(value):
                try:
                    value = float(value)
                except ValueError:
                    raise error.PyAsn1Error(
                        'Bad real value syntax: %s' % (value,)
                    )
            if self._inf and value in self._inf:
                return value
            else:
                e = 0
                while int(value) != value:
                    value *= 10
                    e -= 1
                return self.__normalizeBase10((int(value), 10, e))
        elif isinstance(value, Real):
            return tuple(value)
        raise error.PyAsn1Error(
            'Bad real value syntax: %s' % (value,)
        )

    def prettyOut(self, value):
        if value in self._inf:
            return '\'%s\'' % value
        else:
            return str(value)

    def prettyPrint(self, scope=0):
        if self.isInf:
            return self.prettyOut(self._value)
        else:
            return str(float(self))

    @property
    def isPlusInf(self):
        """Indicate PLUS-INFINITY object value

        Returns
        -------
        : :class:`bool`
            :class:`True` if calling object represents plus infinity
            or :class:`False` otherwise.

        """
        return self._value == self._plusInf

    @property
    def isMinusInf(self):
        """Indicate MINUS-INFINITY object value

        Returns
        -------
        : :class:`bool`
            :class:`True` if calling object represents minus infinity
            or :class:`False` otherwise.
        """
        return self._value == self._minusInf

    @property
    def isInf(self):
        return self._value in self._inf

    def __str__(self):
        return str(float(self))

    def __add__(self, value):
        return self.clone(float(self) + value)

    def __radd__(self, value):
        return self + value

    def __mul__(self, value):
        return self.clone(float(self) * value)

    def __rmul__(self, value):
        return self * value

    def __sub__(self, value):
        return self.clone(float(self) - value)

    def __rsub__(self, value):
        return self.clone(value - float(self))

    def __mod__(self, value):
        return self.clone(float(self) % value)

    def __rmod__(self, value):
        return self.clone(value % float(self))

    def __pow__(self, value, modulo=None):
        return self.clone(pow(float(self), value, modulo))

    def __rpow__(self, value):
        return self.clone(pow(value, float(self)))

    if sys.version_info[0] <= 2:
        def __div__(self, value):
            return self.clone(float(self) / value)

        def __rdiv__(self, value):
            return self.clone(value / float(self))
    else:
        def __truediv__(self, value):
            return self.clone(float(self) / value)

        def __rtruediv__(self, value):
            return self.clone(value / float(self))

        def __divmod__(self, value):
            return self.clone(float(self) // value)

        def __rdivmod__(self, value):
            return self.clone(value // float(self))

    def __int__(self):
        return int(float(self))

    if sys.version_info[0] <= 2:
        def __long__(self):
            return long(float(self))

    def __float__(self):
        if self._value in self._inf:
            return self._value
        else:
            return float(
                self._value[0] * pow(self._value[1], self._value[2])
            )

    def __abs__(self):
        return self.clone(abs(float(self)))

    def __pos__(self):
        return self.clone(+float(self))

    def __neg__(self):
        return self.clone(-float(self))

    def __round__(self, n=0):
        r = round(float(self), n)
        if n:
            return self.clone(r)
        else:
            return r

    def __floor__(self):
        return self.clone(math.floor(float(self)))

    def __ceil__(self):
        return self.clone(math.ceil(float(self)))

    if sys.version_info[0:2] > (2, 5):
        def __trunc__(self):
            return self.clone(math.trunc(float(self)))

    def __lt__(self, value):
        return float(self) < value

    def __le__(self, value):
        return float(self) <= value

    def __eq__(self, value):
        return float(self) == value

    def __ne__(self, value):
        return float(self) != value

    def __gt__(self, value):
        return float(self) > value

    def __ge__(self, value):
        return float(self) >= value

    if sys.version_info[0] <= 2:
        def __nonzero__(self):
            return bool(float(self))
    else:
        def __bool__(self):
            return bool(float(self))

        __hash__ = base.AbstractSimpleAsn1Item.__hash__

    def __getitem__(self, idx):
        if self._value in self._inf:
            raise error.PyAsn1Error('Invalid infinite value operation')
        else:
            return self._value[idx]

    # compatibility stubs

    def isPlusInfinity(self):
        return self.isPlusInf

    def isMinusInfinity(self):
        return self.isMinusInf

    def isInfinity(self):
        return self.isInf


class Enumerated(Integer):
    __doc__ = Integer.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatSimple, 0x0A)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    # Optimization for faster codec lookup
    typeId = Integer.getTypeId()

    #: Default :py:class:`~pyasn1.type.namedval.NamedValues` object
    #: representing symbolic aliases for numbers
    namedValues = namedval.NamedValues()


# "Structured" ASN.1 types

class SequenceOfAndSetOfBase(base.AbstractConstructedAsn1Item):
    """Create |ASN.1| type.

    |ASN.1| objects are mutable and duck-type Python :class:`list` objects.

    Parameters
    ----------
    componentType : :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
        A pyasn1 object representing ASN.1 type allowed within |ASN.1| type

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    sizeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing collection size constraint
     """

    def __init__(self, *args, **kwargs):
        # support positional params for backward compatibility
        if args:
            for key, value in zip(('componentType', 'tagSet',
                                   'subtypeSpec', 'sizeSpec'), args):
                if key in kwargs:
                    raise error.PyAsn1Error('Conflicting positional and keyword params!')
                kwargs['componentType'] = value

        base.AbstractConstructedAsn1Item.__init__(self, **kwargs)

    # Python list protocol

    def clear(self):
        self._componentValues = []

    def append(self, value):
        self[len(self)] = value

    def count(self, value):
        return self._componentValues.count(value)

    def extend(self, values):
        for value in values:
            self.append(value)

    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = len(self)
        return self._componentValues.index(value, start, stop)

    def reverse(self):
        self._componentValues.reverse()

    def sort(self, key=None, reverse=False):
        self._componentValues.sort(key=key, reverse=reverse)

    def __iter__(self):
        return iter(self._componentValues)

    def _cloneComponentValues(self, myClone, cloneValueFlag):
        for idx, componentValue in enumerate(self._componentValues):
            if componentValue is not noValue:
                if isinstance(componentValue, base.AbstractConstructedAsn1Item):
                    myClone.setComponentByPosition(
                        idx, componentValue.clone(cloneValueFlag=cloneValueFlag)
                    )
                else:
                    myClone.setComponentByPosition(idx, componentValue.clone())

    def getComponentByPosition(self, idx):
        """Return |ASN.1| type component value by position.

        Equivalent to Python sequence subscription operation (e.g. `[]`).

        Parameters
        ----------
        idx : :class:`int`
            Component index (zero-based). Must either refer to an existing
            component or to N+1 component (if *componentType* is set). In the latter
            case a new component type gets instantiated and appended to the |ASN.1|
            sequence.

        Returns
        -------
        : :py:class:`~pyasn1.type.base.PyAsn1Item`
            a pyasn1 object
        """
        try:
            return self._componentValues[idx]
        except IndexError:
            self.setComponentByPosition(idx)
            return self._componentValues[idx]

    def setComponentByPosition(self, idx, value=noValue,
                               verifyConstraints=True,
                               matchTags=True,
                               matchConstraints=True):
        """Assign |ASN.1| type component by position.

        Equivalent to Python sequence item assignment operation (e.g. `[]`)
        or list.append() (when idx == len(self)).

        Parameters
        ----------
        idx: :class:`int`
            Component index (zero-based). Must either refer to existing
            component or to N+1 component. In the latter case a new component
            type gets instantiated (if *componentType* is set, or given ASN.1
            object is taken otherwise) and appended to the |ASN.1| sequence.

        value: :class:`object` or :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
            A Python value to initialize |ASN.1| component with (if *componentType* is set)
            or ASN.1 value object to assign to |ASN.1| component.

        verifyConstraints: :class:`bool`
             If `False`, skip constraints validation

        matchTags: :class:`bool`
             If `False`, skip component tags matching

        matchConstraints: :class:`bool`
             If `False`, skip component constraints matching

        Returns
        -------
        self

        Raises
        ------
        IndexError:
            When idx > len(self)
        """
        if value is None:  # backward compatibility
            value = noValue

        componentType = self.componentType

        try:
            currentValue = self._componentValues[idx]
        except IndexError:
            currentValue = noValue

            if len(self._componentValues) < idx:
                raise error.PyAsn1Error('Component index out of range')

        if value is noValue:
            if componentType is not None:
                value = componentType.clone()
            elif currentValue is noValue:
                raise error.PyAsn1Error('Component type not defined')
        elif not isinstance(value, base.Asn1Item):
            if componentType is not None and isinstance(componentType, base.AbstractSimpleAsn1Item):
                value = componentType.clone(value=value)
            elif currentValue is not noValue and isinstance(currentValue, base.AbstractSimpleAsn1Item):
                value = currentValue.clone(value=value)
            else:
                raise error.PyAsn1Error('%s undefined component type' % componentType.__class__.__name__)
        elif componentType is not None:
            if self.strictConstraints:
                if not componentType.isSameTypeWith(value, matchTags, matchConstraints):
                    raise error.PyAsn1Error('Component value is tag-incompatible: %r vs %r' % (value, componentType))
            else:
                if not componentType.isSuperTypeOf(value, matchTags, matchConstraints):
                    raise error.PyAsn1Error('Component value is tag-incompatible: %r vs %r' % (value, componentType))

        if verifyConstraints and value.isValue:
            try:
                self.subtypeSpec(value, idx)

            except error.PyAsn1Error:
                exType, exValue, exTb = sys.exc_info()
                raise exType('%s at %s' % (exValue, self.__class__.__name__))

        if currentValue is noValue:
            self._componentValues.append(value)
        else:
            self._componentValues[idx] = value

        return self

    @property
    def componentTagMap(self):
        if self.componentType is not None:
            return self.componentType.tagMap

    def prettyPrint(self, scope=0):
        scope += 1
        representation = self.__class__.__name__ + ':\n'
        for idx, componentValue in enumerate(self._componentValues):
            representation += ' ' * scope
            if (componentValue is noValue and
                    self.componentType is not None):
                representation += '<empty>'
            else:
                representation += componentValue.prettyPrint(scope)
        return representation

    def prettyPrintType(self, scope=0):
        scope += 1
        representation = '%s -> %s {\n' % (self.tagSet, self.__class__.__name__)
        if self.componentType is not None:
            representation += ' ' * scope
            representation += self.componentType.prettyPrintType(scope)
        return representation + '\n' + ' ' * (scope - 1) + '}'


    @property
    def isValue(self):
        """Indicate if |ASN.1| object represents ASN.1 type or ASN.1 value.

        In other words, if *isValue* is `True`, then the ASN.1 object is
        initialized.

        For the purpose of this check, empty |ASN.1| object is considered
        as initialized.

        Returns
        -------
        : :class:`bool`
            :class:`True` if object represents ASN.1 value and type,
            :class:`False` if object represents just ASN.1 type.

        Note
        ----
        There is an important distinction between PyASN1 type and value objects.
        The PyASN1 type objects can only participate in ASN.1 type
        operations (subtyping, comparison etc) and serve as a
        blueprint for serialization codecs to resolve ambiguous types.

        The PyASN1 value objects can additionally participate in most
        of built-in Python operations.
        """
        for componentValue in self._componentValues:
            if not componentValue.isValue:
                return False

        return True


class SequenceOf(SequenceOfAndSetOfBase):
    __doc__ = SequenceOfAndSetOfBase.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatConstructed, 0x10)
    )

    #: Default :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
    #: object representing ASN.1 type allowed within |ASN.1| type
    componentType = None

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
    #: object imposing size constraint on |ASN.1| objects
    sizeSpec = constraint.ConstraintsIntersection()

    # Disambiguation ASN.1 types identification
    typeId = SequenceOfAndSetOfBase.getTypeId()


class SetOf(SequenceOfAndSetOfBase):
    __doc__ = SequenceOfAndSetOfBase.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatConstructed, 0x11)
    )

    #: Default :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
    #: object representing ASN.1 type allowed within |ASN.1| type
    componentType = None

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
    #: object imposing size constraint on |ASN.1| objects
    sizeSpec = constraint.ConstraintsIntersection()

    # Disambiguation ASN.1 types identification
    typeId = SequenceOfAndSetOfBase.getTypeId()


class SequenceAndSetBase(base.AbstractConstructedAsn1Item):
    """Create |ASN.1| type.

    |ASN.1| objects are mutable and duck-type Python :class:`dict` objects.

    Parameters
    ----------
    componentType: :py:class:`~pyasn1.type.namedtype.NamedType`
        Object holding named ASN.1 types allowed within this collection

    tagSet: :py:class:`~pyasn1.type.tag.TagSet`
        Object representing non-default ASN.1 tag(s)

    subtypeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing non-default ASN.1 subtype constraint(s)

    sizeSpec: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
        Object representing collection size constraint
    """
    #: Default :py:class:`~pyasn1.type.namedtype.NamedTypes`
    #: object representing named ASN.1 types allowed within |ASN.1| type
    componentType = namedtype.NamedTypes()

    def __init__(self, **kwargs):
        base.AbstractConstructedAsn1Item.__init__(self, **kwargs)
        self._componentTypeLen = len(self.componentType)

    def __getitem__(self, idx):
        if octets.isStringType(idx):
            return self.getComponentByName(idx)
        else:
            return base.AbstractConstructedAsn1Item.__getitem__(self, idx)

    def __setitem__(self, idx, value):
        if octets.isStringType(idx):
            self.setComponentByName(idx, value)
        else:
            base.AbstractConstructedAsn1Item.__setitem__(self, idx, value)

    def __contains__(self, key):
        return key in self.componentType

    def __iter__(self):
        return iter(self.componentType)

    # Python dict protocol

    def values(self):
        for idx in range(self._componentTypeLen):
            yield self[idx]

    def keys(self):
        return iter(self.componentType)

    def items(self):
        for idx in range(self._componentTypeLen):
            yield self.componentType[idx].getName(), self[idx]

    def update(self, *iterValue, **mappingValue):
        for k, v in iterValue:
            self[k] = v
        for k in mappingValue:
            self[k] = mappingValue[k]

    def clear(self):
        self._componentValues = []

    def _cloneComponentValues(self, myClone, cloneValueFlag):
        for idx, componentValue in enumerate(self._componentValues):
            if componentValue is not noValue:
                if isinstance(componentValue, base.AbstractConstructedAsn1Item):
                    myClone.setComponentByPosition(
                        idx, componentValue.clone(cloneValueFlag=cloneValueFlag)
                    )
                else:
                    myClone.setComponentByPosition(idx, componentValue.clone())

    def getComponentByName(self, name):
        """Returns |ASN.1| type component by name.

        Equivalent to Python :class:`dict` subscription operation (e.g. `[]`).

        Parameters
        ----------
        name : :class:`str`
            |ASN.1| type component name

        Returns
        -------
        : :py:class:`~pyasn1.type.base.PyAsn1Item`
            Instantiate |ASN.1| component type or return existing component value
        """
        return self.getComponentByPosition(
            self.componentType.getPositionByName(name)
        )

    def setComponentByName(self, name, value=noValue,
                           verifyConstraints=True,
                           matchTags=True,
                           matchConstraints=True):
        """Assign |ASN.1| type component by name.

        Equivalent to Python :class:`dict` item assignment operation (e.g. `[]`).

        Parameters
        ----------
        name: :class:`str`
            |ASN.1| type component name

        value : :class:`object` or :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
            A Python value to initialize |ASN.1| component with (if *componentType* is set)
            or ASN.1 value object to assign to |ASN.1| component.

        verifyConstraints: :class:`bool`
             If `False`, skip constraints validation

        matchTags: :class:`bool`
             If `False`, skip component tags matching

        matchConstraints: :class:`bool`
             If `False`, skip component constraints matching

        Returns
        -------
        self
        """
        return self.setComponentByPosition(
            self.componentType.getPositionByName(name), value, verifyConstraints, matchTags, matchConstraints
        )

    def getComponentByPosition(self, idx):
        """Returns |ASN.1| type component by index.

        Equivalent to Python sequence subscription operation (e.g. `[]`).

        Parameters
        ----------
        idx : :class:`int`
            Component index (zero-based). Must either refer to an existing
            component or (if *componentType* is set) new ASN.1 type object gets
            instantiated.

        Returns
        -------
        : :py:class:`~pyasn1.type.base.PyAsn1Item`
            a PyASN1 object
        """
        try:
            componentValue = self._componentValues[idx]
        except IndexError:
            componentValue = noValue

        if componentValue is noValue:
            self.setComponentByPosition(idx)

        return self._componentValues[idx]

    def setComponentByPosition(self, idx, value=noValue,
                               verifyConstraints=True,
                               matchTags=True,
                               matchConstraints=True):
        """Assign |ASN.1| type component by position.

        Equivalent to Python sequence item assignment operation (e.g. `[]`).

        Parameters
        ----------
        idx : :class:`int`
            Component index (zero-based). Must either refer to existing
            component (if *componentType* is set) or to N+1 component
            otherwise. In the latter case a new component of given ASN.1
            type gets instantiated and appended to |ASN.1| sequence.

        value : :class:`object` or :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
            A Python value to initialize |ASN.1| component with (if *componentType* is set)
            or ASN.1 value object to assign to |ASN.1| component.

        verifyConstraints : :class:`bool`
             If `False`, skip constraints validation

        matchTags: :class:`bool`
             If `False`, skip component tags matching

        matchConstraints: :class:`bool`
             If `False`, skip component constraints matching

        Returns
        -------
        self
        """
        if value is None:  # backward compatibility
            value = noValue

        componentType = self.componentType
        componentTypeLen = self._componentTypeLen

        try:
            currentValue = self._componentValues[idx]
        except IndexError:
            currentValue = noValue
            if componentTypeLen:
                if componentTypeLen < idx:
                    raise IndexError('component index out of range')
                self._componentValues = [noValue] * componentTypeLen

        if value is noValue:
            if componentTypeLen:
                value = componentType.getTypeByPosition(idx).clone()
            elif currentValue is noValue:
                raise error.PyAsn1Error('Component type not defined')
        elif not isinstance(value, base.Asn1Item):
            if componentTypeLen:
                subComponentType = componentType.getTypeByPosition(idx)
                if isinstance(subComponentType, base.AbstractSimpleAsn1Item):
                    value = subComponentType.clone(value=value)
                else:
                    raise error.PyAsn1Error('%s can cast only scalar values' % componentType.__class__.__name__)
            elif currentValue is not noValue and isinstance(currentValue, base.AbstractSimpleAsn1Item):
                value = currentValue.clone(value=value)
            else:
                raise error.PyAsn1Error('%s undefined component type' % componentType.__class__.__name__)
        elif (matchTags or matchConstraints) and componentTypeLen:
            subComponentType = componentType.getTypeByPosition(idx)
            if subComponentType is not noValue:
                if self.strictConstraints:
                    if not subComponentType.isSameTypeWith(value, matchTags, matchConstraints):
                        raise error.PyAsn1Error('Component value is tag-incompatible: %r vs %r' % (value, componentType))
                else:
                    if not subComponentType.isSuperTypeOf(value, matchTags, matchConstraints):
                        raise error.PyAsn1Error('Component value is tag-incompatible: %r vs %r' % (value, componentType))

        if verifyConstraints and value.isValue:
            try:
                self.subtypeSpec(value, idx)

            except error.PyAsn1Error:
                exType, exValue, exTb = sys.exc_info()
                raise exType('%s at %s' % (exValue, self.__class__.__name__))

        if componentTypeLen:
            self._componentValues[idx] = value
        elif len(self._componentValues) == idx:
            self._componentValues.append(value)
        else:
            raise error.PyAsn1Error('Component index out of range')

        return self

    @property
    def isValue(self):
        """Indicate if |ASN.1| object represents ASN.1 type or ASN.1 value.

        In other words, if *isValue* is `True`, then the ASN.1 object is
        initialized.

        For the purpose of check, the *OPTIONAL* and *DEFAULT* fields are
        unconditionally considered as initialized.

        Returns
        -------
        : :class:`bool`
            :class:`True` if object represents ASN.1 value and type,
            :class:`False` if object represents just ASN.1 type.

        Note
        ----
        There is an important distinction between PyASN1 type and value objects.
        The PyASN1 type objects can only participate in ASN.1 type
        operations (subtyping, comparison etc) and serve as a
        blueprint for serialization codecs to resolve ambiguous types.

        The PyASN1 value objects can additionally participate in most
        of built-in Python operations.
        """
        componentType = self.componentType

        if componentType:
            for idx, subComponentType in enumerate(componentType.namedTypes):
                if subComponentType.isDefaulted or subComponentType.isOptional:
                    continue
                if (not self._componentValues or
                        not self._componentValues[idx].isValue):
                    return False

        else:
            for componentValue in self._componentValues:
                if not componentValue.isValue:
                    return False

        return True

    def prettyPrint(self, scope=0):
        """Return an object representation string.

        Returns
        -------
        : :class:`str`
            Human-friendly object representation.
        """
        scope += 1
        representation = self.__class__.__name__ + ':\n'
        for idx, componentValue in enumerate(self._componentValues):
            if componentValue is not noValue:
                representation += ' ' * scope
                if self.componentType:
                    representation += self.componentType.getNameByPosition(idx)
                else:
                    representation += 'field-%d' % idx
                representation = '%s=%s\n' % (
                    representation, componentValue.prettyPrint(scope)
                )
        return representation

    def prettyPrintType(self, scope=0):
        scope += 1
        representation = '%s -> %s {\n' % (self.tagSet, self.__class__.__name__)
        for idx, componentType in enumerate(self.componentType):
            representation += ' ' * scope
            representation += '"%s"' % self.componentType.getNameByPosition(idx)
            representation = '%s = %s\n' % (
                representation, componentType.prettyPrintType(scope)
            )
        return representation + '\n' + ' ' * (scope - 1) + '}'

    # backward compatibility

    def setDefaultComponents(self):
        return self

    def getComponentType(self):
        if self._componentTypeLen:
            return self.componentType

    def getNameByPosition(self, idx):
        if self._componentTypeLen:
            return self.componentType[idx].name


class Sequence(SequenceAndSetBase):
    __doc__ = SequenceAndSetBase.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatConstructed, 0x10)
    )

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
    #: object imposing constraints on |ASN.1| objects
    sizeSpec = constraint.ConstraintsIntersection()

    #: Default collection of ASN.1 types of component (e.g. :py:class:`~pyasn1.type.namedtype.NamedType`)
    #: object imposing size constraint on |ASN.1| objects
    componentType = namedtype.NamedTypes()

    # Disambiguation ASN.1 types identification
    typeId = SequenceAndSetBase.getTypeId()

    # backward compatibility

    def getComponentTagMapNearPosition(self, idx):
        if self.componentType:
            return self.componentType.getTagMapNearPosition(idx)

    def getComponentPositionNearType(self, tagSet, idx):
        if self.componentType:
            return self.componentType.getPositionNearType(tagSet, idx)
        else:
            return idx


class Set(SequenceAndSetBase):
    __doc__ = SequenceAndSetBase.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.initTagSet(
        tag.Tag(tag.tagClassUniversal, tag.tagFormatConstructed, 0x11)
    )

    #: Default collection of ASN.1 types of component (e.g. :py:class:`~pyasn1.type.namedtype.NamedType`)
    #: object representing ASN.1 type allowed within |ASN.1| type
    componentType = namedtype.NamedTypes()

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
    #: object imposing constraints on |ASN.1| objects
    sizeSpec = constraint.ConstraintsIntersection()

    # Disambiguation ASN.1 types identification
    typeId = SequenceAndSetBase.getTypeId()

    def getComponent(self, innerFlag=False):
        return self

    def getComponentByType(self, tagSet, innerFlag=False):
        """Returns |ASN.1| type component by ASN.1 tag.

        Parameters
        ----------
        tagSet : :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tags to identify one of
            |ASN.1| object component

        Returns
        -------
        : :py:class:`~pyasn1.type.base.PyAsn1Item`
            a pyasn1 object
        """
        component = self.getComponentByPosition(
            self.componentType.getPositionByType(tagSet)
        )
        if innerFlag and isinstance(component, Set):
            # get inner component by inner tagSet
            return component.getComponent(innerFlag=True)
        else:
            # get outer component by inner tagSet
            return component

    def setComponentByType(self, tagSet, value=noValue,
                           verifyConstraints=True,
                           matchTags=True,
                           matchConstraints=True,
                           innerFlag=False):
        """Assign |ASN.1| type component by ASN.1 tag.

        Parameters
        ----------
        tagSet : :py:class:`~pyasn1.type.tag.TagSet`
            Object representing ASN.1 tags to identify one of
            |ASN.1| object component

        value : :class:`object` or :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
            A Python value to initialize |ASN.1| component with (if *componentType* is set)
            or ASN.1 value object to assign to |ASN.1| component.

        verifyConstraints : :class:`bool`
            If `False`, skip constraints validation

        matchTags: :class:`bool`
            If `False`, skip component tags matching

        matchConstraints: :class:`bool`
            If `False`, skip component constraints matching

        innerFlag: :class:`bool`
            If `True`, search for matching *tagSet* recursively.

        Returns
        -------
        self
        """
        idx = self.componentType.getPositionByType(tagSet)

        if innerFlag:  # set inner component by inner tagSet
            componentType = self.componentType.getTypeByPosition(idx)

            if componentType.tagSet:
                return self.setComponentByPosition(
                    idx, value, verifyConstraints, matchTags, matchConstraints
                )
            else:
                componentType = self.getComponentByPosition(idx)
                return componentType.setComponentByType(
                    tagSet, value, verifyConstraints, matchTags, matchConstraints, innerFlag=innerFlag
                )
        else:  # set outer component by inner tagSet
            return self.setComponentByPosition(
                idx, value, verifyConstraints, matchTags, matchConstraints
            )

    @property
    def componentTagMap(self):
        if self.componentType:
            return self.componentType.tagMapUnique


class Choice(Set):
    __doc__ = Set.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.TagSet()  # untagged

    #: Default collection of ASN.1 types of component (e.g. :py:class:`~pyasn1.type.namedtype.NamedType`)
    #: object representing ASN.1 type allowed within |ASN.1| type
    componentType = namedtype.NamedTypes()

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    #: Default :py:class:`~pyasn1.type.constraint.ConstraintsIntersection`
    #: object imposing size constraint on |ASN.1| objects
    sizeSpec = constraint.ConstraintsIntersection(
        constraint.ValueSizeConstraint(1, 1)
    )

    # Disambiguation ASN.1 types identification
    typeId = Set.getTypeId()

    _currentIdx = None

    def __eq__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] == other
        return NotImplemented

    def __ne__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] != other
        return NotImplemented

    def __lt__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] < other
        return NotImplemented

    def __le__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] <= other
        return NotImplemented

    def __gt__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] > other
        return NotImplemented

    def __ge__(self, other):
        if self._componentValues:
            return self._componentValues[self._currentIdx] >= other
        return NotImplemented

    if sys.version_info[0] <= 2:
        def __nonzero__(self):
            return self._componentValues and True or False
    else:
        def __bool__(self):
            return self._componentValues and True or False

    def __len__(self):
        return self._currentIdx is not None and 1 or 0

    def __contains__(self, key):
        if self._currentIdx is None:
            return False
        return key == self.componentType[self._currentIdx].getName()

    def __iter__(self):
        if self._currentIdx is None:
            raise StopIteration
        yield self.componentType[self._currentIdx].getName()

    # Python dict protocol

    def values(self):
        if self._currentIdx is not None:
            yield self._componentValues[self._currentIdx]

    def keys(self):
        if self._currentIdx is not None:
            yield self.componentType[self._currentIdx].getName()

    def items(self):
        if self._currentIdx is not None:
            yield self.componentType[self._currentIdx].getName(), self[self._currentIdx]

    def verifySizeSpec(self):
        if self._currentIdx is None:
            raise error.PyAsn1Error('Component not chosen')

    def _cloneComponentValues(self, myClone, cloneValueFlag):
        try:
            component = self.getComponent()
        except error.PyAsn1Error:
            pass
        else:
            if isinstance(component, Choice):
                tagSet = component.effectiveTagSet
            else:
                tagSet = component.tagSet
            if isinstance(component, base.AbstractConstructedAsn1Item):
                myClone.setComponentByType(
                    tagSet, component.clone(cloneValueFlag=cloneValueFlag)
                )
            else:
                myClone.setComponentByType(tagSet, component.clone())

    def getComponentByPosition(self, idx):
        __doc__ = Set.__doc__

        if self._currentIdx is None or self._currentIdx != idx:
            return Set.getComponentByPosition(self, idx)

        return self._componentValues[idx]

    def setComponentByPosition(self, idx, value=noValue,
                               verifyConstraints=True,
                               matchTags=True,
                               matchConstraints=True):
        """Assign |ASN.1| type component by position.

        Equivalent to Python sequence item assignment operation (e.g. `[]`).

        Parameters
        ----------
        idx: :class:`int`
            Component index (zero-based). Must either refer to existing
            component or to N+1 component. In the latter case a new component
            type gets instantiated (if *componentType* is set, or given ASN.1
            object is taken otherwise) and appended to the |ASN.1| sequence.

        value: :class:`object` or :py:class:`~pyasn1.type.base.PyAsn1Item` derivative
            A Python value to initialize |ASN.1| component with (if *componentType* is set)
            or ASN.1 value object to assign to |ASN.1| component. Once a new value is
            set to *idx* component, previous value is dropped.

        verifyConstraints : :class:`bool`
            If `False`, skip constraints validation

        matchTags: :class:`bool`
            If `False`, skip component tags matching

        matchConstraints: :class:`bool`
            If `False`, skip component constraints matching

        Returns
        -------
        self
        """
        oldIdx = self._currentIdx
        Set.setComponentByPosition(self, idx, value, verifyConstraints, matchTags, matchConstraints)
        self._currentIdx = idx
        if oldIdx is not None and oldIdx != idx:
            self._componentValues[oldIdx] = None
        return self

    @property
    def minTagSet(self):
        if self.tagSet:
            return self.tagSet
        else:
            return self.componentType.minTagSet

    @property
    def effectiveTagSet(self):
        """Return a :class:`~pyasn1.type.tag.TagSet` object of the currently initialized component or self (if |ASN.1| is tagged)."""
        if self.tagSet:
            return self.tagSet
        else:
            component = self.getComponent()
            return component.effectiveTagSet

    @property
    def tagMap(self):
        """"Return a :class:`~pyasn1.type.tagmap.TagMap` object mapping
            ASN.1 tags to ASN.1 objects contained within callee.
        """
        if self.tagSet:
            return Set.tagMap.fget(self)
        else:
            return self.componentType.tagMapUnique

    def getComponent(self, innerFlag=0):
        """Return currently assigned component of the |ASN.1| object.

        Returns
        -------
        : :py:class:`~pyasn1.type.base.PyAsn1Item`
            a PyASN1 object
        """
        if self._currentIdx is None:
            raise error.PyAsn1Error('Component not chosen')
        else:
            c = self._componentValues[self._currentIdx]
            if innerFlag and isinstance(c, Choice):
                return c.getComponent(innerFlag)
            else:
                return c

    def getName(self, innerFlag=False):
        """Return the name of currently assigned component of the |ASN.1| object.

        Returns
        -------
        : :py:class:`str`
            |ASN.1| component name
        """
        if self._currentIdx is None:
            raise error.PyAsn1Error('Component not chosen')
        else:
            if innerFlag:
                c = self._componentValues[self._currentIdx]
                if isinstance(c, Choice):
                    return c.getName(innerFlag)
            return self.componentType.getNameByPosition(self._currentIdx)

    @property
    def isValue(self):
        """Indicate if |ASN.1| component is set and represents ASN.1 type or ASN.1 value.

        The PyASN1 type objects can only participate in types comparison
        and serve as a blueprint for serialization codecs to resolve
        ambiguous types.

        The PyASN1 value objects can additionally participate in most
        of built-in Python operations.

        Returns
        -------
        : :class:`bool`
            :class:`True` if |ASN.1| component is set and represent value and type,
            :class:`False` if |ASN.1| component is not set or it represents just ASN.1 type.
        """
        if self._currentIdx is None:
            return False

        return self._componentValues[self._currentIdx].isValue

    # compatibility stubs

    def getMinTagSet(self):
        return self.minTagSet


class Any(OctetString):
    __doc__ = OctetString.__doc__

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.tag.TagSet` object representing ASN.1 tag(s)
    #: associated with |ASN.1| type.
    tagSet = tag.TagSet()  # untagged

    #: Set (on class, not on instance) or return a
    #: :py:class:`~pyasn1.type.constraint.ConstraintsIntersection` object
    #: imposing constraints on |ASN.1| type initialization values.
    subtypeSpec = constraint.ConstraintsIntersection()

    # Disambiguation ASN.1 types identification
    typeId = OctetString.getTypeId()

    @property
    def tagMap(self):
        """"Return a :class:`~pyasn1.type.tagmap.TagMap` object mapping
            ASN.1 tags to ASN.1 objects contained within callee.
        """
        try:
            return self._tagMap

        except AttributeError:
            self._tagMap = tagmap.TagMap(
                {self.tagSet: self},
                {eoo.endOfOctets.tagSet: eoo.endOfOctets},
                self
            )

            return self._tagMap

# XXX
# coercion rules?
