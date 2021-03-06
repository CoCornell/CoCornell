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
    EMPTY_BOARD_ID = 11
    EMPTY_BOARD_NAME = 12

    # list
    NO_ACCESS_TO_LIST = 20
    EMPTY_LIST_NAME = 21
    EMPTY_LIST_ID = 22

    # card
    NO_ACCESS_TO_CARD = 26
    EMPTY_CARD_CONTENT = 27
    EMPTY_IMAGE = 28
    NO_OCR_TEXT = 29
    INVALID_UPLOAD_IMAGE = 30

    MISSING_PARAMETER = 31

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
        elif error_code == cls.NO_ACCESS_TO_BOARD:
            return 'Board id is empty'
        elif error_code == cls.NO_ACCESS_TO_LIST:
            return 'No access to list'
        elif error_code == cls.EMPTY_LIST_NAME:
            return 'List name is empty'
        elif error_code == cls.MISSING_PARAMETER:
            return 'Missing parameter: ' + args[0]
        elif error_code == cls.EMPTY_BOARD_NAME:
            return 'Board name is empty'
        elif error_code == cls.NO_ACCESS_TO_CARD:
            return 'No access to card'
        elif error_code == cls.EMPTY_CARD_CONTENT:
            return 'Card content is empty'
        elif error_code == cls.EMPTY_LIST_ID:
            return 'List id is empty'
        elif error_code == cls.NO_OCR_TEXT:
            return 'No OCR text for this card'
        elif error_code == cls.INVALID_UPLOAD_IMAGE:
            return 'The upload image is not valid'
