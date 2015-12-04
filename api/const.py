class Error(object):
    # sign in / sign up
    EMPTY_NETID = 1
    EMPTY_PASSWORD = 2
    EMPTY_NAME = 3
    NETID_NOT_EXIST = 4
    NETID_EXISTED = 5
    INVALID_PASSWORD = 6

    # board
    NO_ACCESS_TO_BOARD = 10

    # list
    NO_ACCESS_TO_LIST = 20

    MISSING_PARAMETER = 30

    @classmethod
    def error_message(cls, error_code, *args):
        if error_code == cls.EMPTY_NETID:
            return 'NetID is empty'
        elif error_code == cls.EMPTY_PASSWORD:
            return 'Password is empty'
        elif error_code == cls.NETID_NOT_EXIST:
            return 'NetID not exists'
        elif error_code == cls.INVALID_PASSWORD:
            return 'Invalid password'
        elif error_code == cls.NO_ACCESS_TO_BOARD:
            return 'No access to board'
        elif error_code == cls.NO_ACCESS_TO_LIST:
            return 'No access to list'
        elif error_code == cls.MISSING_PARAMETER:
            return 'Missing parameter: ' + args[0]
