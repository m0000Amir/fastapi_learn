from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes="bcrypt", deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        """
        The rule:
            1st plain_password (secret)
            2nd hashed_password (hash)

        :arg secret:
            the secret to verify
        
        :arg hash:
            hash string to compare to
        """
        return pwd_cxt.verify(plain_password, hashed_password)