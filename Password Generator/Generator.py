import random

class Generator(object):
    """
    This class defines a Password Generator.
    """

    def __init__(self):
        """
        Constructor for the Generator class.
        Initializes the valid characters that can be used in the generated password.
        """

        # String containing all valid characters for the password
        self.string = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

    def GeneratePassword(self, passlen):
        """
        Generate a random password of specified length.

        Args:
            passlen (int): Length of the password to generate.

        Returns:
            str: A randomly generated password of the specified length.
        """

        # Use random.sample to create a password of length passlen
        # The password will be a random selection of characters from self.string
        return "".join(random.sample(self.string, passlen))
