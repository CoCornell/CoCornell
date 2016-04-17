from mysite import app
from mysite.views import index, signin, signup, signout, board, list, card, upload


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
