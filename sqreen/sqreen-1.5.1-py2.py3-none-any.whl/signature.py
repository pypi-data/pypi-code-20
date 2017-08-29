# -*- coding: utf-8 -*-
# Copyright (c) 2016 Sqreen. All Rights Reserved.
# Please refer to our terms for more information: https://www.sqreen.io/terms.html
""" RSA signature helpers, comes from BackEnd/signature
"""
import json

from abc import ABCMeta
from base64 import b64decode, b64encode
from logging import getLogger

import rsa

from .exceptions import SqreenException
from .utils import is_string


LOGGER = getLogger(__name__)
REQUIRED_KEYS = ('hookpoint', 'name', 'callbacks', 'conditions')
SIGNATURE_VERSION = 'rsa_0_1'
PUBLIC_KEY = rsa.PublicKey.load_pkcs1_openssl_pem("""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvk/Fwmuv1/l90AZe2kvO
+aJsAB0Lobg99urn5MKBLI0JmW6g8NaNW7G+NGgU+4Ro4qQP3zL9B8FXU0RbKX7h
YsAmBHtBwp6wCNeiLVLb8buH8fybJa4bruZmZ1wYN2HPMcSu95GwSIKm+Om3nq84
GjpILgJbN8sGfHzNl7y1cJSj4H6YjAPKmPocJm9wpMb9GVbV/QPgwFPxhFPFijkZ
/rnY4YVDb4lYsYmfUX8JGLSNMDmxtSWCwFsmtWp75p+76Xq0dGGZEKS/CGVwdNfA
tq4p9Kkd4wcZWVWXZNryt2o3kWwt6Oz4dB9EBjjvSBbwlwp2weuCNf8MgMRgoE/9
xwIDAQAB
-----END PUBLIC KEY-----""")


class InvalidSignature(SqreenException):
    """ Exception raised when encountering an invalid rule signature
    """


class Signature(object):
    """ Signature helpers """

    def __init__(self, digest):
        self.digest = digest

    @staticmethod
    def _normalize_val(val, level):
        """ Normalize a JSON value """

        if level == 0:
            raise Exception("recursion level too deep")

        if isinstance(val, dict):
            val = Signature.normalize(val, None, level - 1)
        elif isinstance(val, list):
            val = [Signature._normalize_val(e, level - 1) for e in val]
            val = '[' + ','.join(val) + ']'
        elif is_string(val) or isinstance(val, int):
            val = json.dumps(val)
        else:
            raise Exception("JSON hash parsing error (wrong type %r)" % val)
        return val

    @staticmethod
    def _normalize_key(key):
        """ Escapes a JSON key """

        if is_string(key) or isinstance(key, int):
            key = json.dumps(key)
        else:
            raise Exception("JSON hash parsing error (wrong key type %r)" % key)
        return key

    @staticmethod
    def normalize(h, keys=None, level=20):
        """ Normalize the `h`
        Normalization is necessary prior cryptographic signature so that 2 objects have the
        same string representation, independently of their keys order or formatting.
        :param h:     the JSON object to be normalized
        :param keys:  the JSON keys we need to keep
        :param level: the maximum level of recursion we may want to keep
        Return a string that will deterministically represent the JSON.
        """
        """
        Currently a dict { 1: <any>} is serialized as {1:<any>}.
        It is not JSON-valid and cannot be supported in Node.js agent
        The correct form would be {"1":<any>} indifferently for dicts { 1: <any> } or { "1": <any> }
        """

        if level == 0:
            raise Exception("recursion level too deep")
        if not isinstance(h, dict):
            raise Exception("%r is not a dict" % h)

        res = []
        for key in sorted(h):
            v = h[key]
            if keys is not None and key not in keys:
                continue

            v = Signature._normalize_val(v, level - 1)
            k = Signature._normalize_key(key)

            res.append("%s:%s" % (k, v))

        return '{' + ','.join(res) + '}'


class RuleSignature(Signature):
    """ Helpers for signing and verifying rules signatures """

    __metaclass__ = ABCMeta

    def verify_rule(self, hash_rule, keys, version):
        """ Return true if signature is correct, else raises an exception """

        # Encode it in ascii
        value = Signature.normalize(hash_rule, keys).encode("ascii")

        encoded_signature = hash_rule['signature'][version]['value']
        signature = b64decode(encoded_signature)

        return self.verify(value, signature)

    def sign_rule(self, hash_rule, keys, version):
        """ Add the signature inside of the hash_rule. """

        # Encode it in ascii
        value = Signature.normalize(hash_rule, keys).encode("ascii")

        signature = self.sign(value)

        sig_hash = hash_rule.setdefault('signature', {})
        sig_hash.update({
            version: {
                'value': b64encode(signature),
                'keys': keys,
            },
        })


class RSASigner(RuleSignature):
    """ Generates signatures given a private key using RSA. """

    def __init__(self,
                 private_key,
                 digest=None):
        super(RSASigner, self).__init__(digest)
        self.private_key = rsa.PrivateKey.load_pkcs1(private_key)

    def sign(self, value):
        """ Return the signed value parameter. """
        signature = rsa.sign(value, self.private_key, 'SHA-512')
        return signature


class RSAVerifier(RuleSignature):
    """ Allow to verify signature given a public key using RSA. """

    def __init__(self,
                 public_key=None,
                 digest=None):

        super(RSAVerifier, self).__init__(digest)

        if public_key is None:
            self.public_key = PUBLIC_KEY
        else:
            self.public_key = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)

    def verify(self, value, signature):
        """ Return true if value matches the signature, else raises an exception
        """
        try:
            result = rsa.verify(value, signature, self.public_key)
        except rsa.VerificationError as e:
            raise InvalidSignature(str(e))
        return result
