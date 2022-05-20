#!/usr/bin/python3 -u

## Copyright (C) 2012 - 2022 ENCRYPTED SUPPORT LP <adrelanos@whonix.org>
## See the file COPYING for copying conditions.

import sys
from stem.connection import connect
from stem.control import Controller
from stem import Signal

controller = connect()

if not controller:
    sys.exit(255)

controller.signal(Signal.NEWNYM)

controller.close()

sys.exit(0)
