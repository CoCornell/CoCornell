class Error(object):
    # sign in / sign up
    EMPTY_NETID = 1
    EMPTY_PASSWORD = 2
    EMPTY_NAME = 3
    NETID_NOT_EXIST = 4
    NETID_EXISTED = 5
    INVALID_PASSWORD = 6

    @classmethod
    def error_message(cls, error_code):
        if error_code == cls.EMPTY_NETID:
            return 'NetID is empty'
        elif error_code == cls.EMPTY_PASSWORD:
            return 'Password is empty'
        elif error_code == cls.NETID_NOT_EXIST:
            return 'NetID not exists'
        elif error_code == cls.INVALID_PASSWORD:
            return 'Invalid password'
