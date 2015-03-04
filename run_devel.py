# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app import create_app


if __name__ == '__main__':
    new_app = create_app(devel=True, testing=False)
    new_app.run(host='0.0.0.0', debug=True, use_debugger=True, use_reloader=True, port=18003)
