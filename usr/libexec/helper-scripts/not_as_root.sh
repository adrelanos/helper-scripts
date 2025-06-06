#!/bin/bash

## Copyright (C) 2025 - 2025 ENCRYPTED SUPPORT LLC <adrelanos@whonix.org>
## See the file COPYING for copying conditions.

source /usr/libexec/helper-scripts/get_colors.sh
source /usr/libexec/helper-scripts/log_run_die.sh

## Block running as root.
not_as_root(){
  test "$(id -u)" = "0" && die 1 "\
${underline}Non-Root Check:${nounderline} Running as root.
  - You are currently running this script with root privileges.
  - This script should not be run as root.
  - Please run as normal user."
  return 0
}
