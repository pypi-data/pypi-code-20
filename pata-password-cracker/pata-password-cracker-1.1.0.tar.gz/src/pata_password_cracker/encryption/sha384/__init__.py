import hashlib


class SHA384Encryption():
    def hash(self, pwd):
        """
        Return a sha384 hash value
        """
        hash_val = hashlib.sha384()
        hash_val.update(pwd.encode('utf-8'))
        return hash_val.hexdigest()
