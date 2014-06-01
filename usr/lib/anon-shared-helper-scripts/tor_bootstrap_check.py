#!/usr/bin/python

## This file is part of Whonix.
## Copyright (C) 2012 - 2014 Patrick Schleizer <adrelanos@riseup.net>
## See the file COPYING for copying conditions.

import sys
import os.path
import re
import stem

from stem.control import Controller

a=str(sys.argv[1])
p=int(sys.argv[2])

try:
  with Controller.from_port(address = a, port = p) as controller:

    if str(sys.argv[3]) == "1":
      controller.authenticate()

    bootstrap_status = controller.get_info("status/bootstrap-phase")

    ## Possible answer, if network cable has been removed:
    ## 250-status/bootstrap-phase=WARN BOOTSTRAP PROGRESS=80 TAG=conn_or SUMMARY="Connecting to the Tor network" WARNING="No route to host" REASON=NOROUTE COUNT=26 RECOMMENDATION=warn

    ## Possible answer:
    ## 250-status/bootstrap-phase=NOTICE BOOTSTRAP PROGRESS=85 TAG=handshake_or SUMMARY="Finishing handshake with first hop"

    ## Possible answer, when done:
    ## 250-status/bootstrap-phase=NOTICE BOOTSTRAP PROGRESS=100 TAG=done SUMMARY="Done"

    ## TODO: parse the messages above.

    print "%s" % (bootstrap_status)

    progress_percent = re.match('.* PROGRESS=([0-9]+).*', bootstrap_status)

    exit_code = int(progress_percent.group(1))

except:
  exit_code=255

sys.exit(exit_code)
