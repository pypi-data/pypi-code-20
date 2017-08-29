import base64
import string
import random
import six

try:
    maketrans = string.maketrans
except:
    maketrans = bytes.maketrans

class BaseCodec(object):
    @classmethod
    def generate_characters(cls, length):
        randomizer = random.SystemRandom()
        max_num = len(cls.chars) - 1
        return b''.join(cls.chars[randomizer.randint(0, max_num)]
            for i in range(length)).decode('UTF-8')

class Base64(BaseCodec):
    chars = (string.ascii_letters + string.digits + '+/').encode('UTF-8')
    padding = True

    @classmethod
    def encode(cls, string):
        return base64.b64encode(string)

    @classmethod
    def normalize(cls, string):
        return string

    @classmethod
    def decode(cls, string):
        return base64.b64decode(string)

_std_b32_to_crockford_b32 = maketrans(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567",
    b"0123456789ABCDEFGHJKMNPQRSTVWXYZ"
)

_crockford_b32_to_std_b32 = maketrans(
    b"0OI1L23456789ABCDEFGHJKMNPQRSTVWXYZ",
    b"AABBBCDEFGHIJKLMNOPQRSTUVWXYZ234567"
)

_normalize_crockford_b32 = maketrans(
    b"OIL" + string.ascii_lowercase.encode('UTF-8'),
    b"011" + string.ascii_uppercase.encode('UTF-8')
)

class CrockfordBase32(BaseCodec):
    chars = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
    padding = False

    @classmethod
    def encode(cls, string, normalize=True, validate=False):
        if isinstance(string, six.text_type):
            string = string.decode("utf-8")

        return base64.b32encode(string).translate(
                _std_b32_to_crockford_b32, b'=').decode('UTF-8')

    @classmethod
    def decode(cls, string, normalize=True, validate=False):
        if normalize:
            string = cls.normalize(string)

        if isinstance(string, six.text_type):
            string = string.encode("utf-8")

        # Ensure the manatory padding is correct:
        b32 = string.upper()
        b32 += b'=' * ((8 - len(b32) % 8) % 8)
        return base64.b32decode(b32.translate(_crockford_b32_to_std_b32))

        return base64.b

    @classmethod
    def normalize(cls, string):
        if isinstance(string, six.text_type):
            string = string.encode("utf-8")

        string = string.translate(_normalize_crockford_b32)
        return string.decode('UTF-8')
