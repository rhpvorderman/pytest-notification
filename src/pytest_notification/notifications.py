# Copyright (c) 2019 Leiden University Medical Center
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import sys
from typing import Optional

DEFAULT_SUCCESS_ICON = "weather-clear" if sys.platform == "linux" else None
DEFAULT_FAIL_ICON = "weather-storm" if sys.platform == "linux" else None


def notify(header: str,
           message: Optional[str] = None,
           urgency: Optional[str] = None,
           icon: Optional[str] = None):

    if sys.platform == "linux":
        # Icon names specified by freedesktop standard.
        _notify_linux(header, message, urgency, icon)

    else:  # Other platforms
        raise NotImplementedError("Systems other than Linux are not "
                                  "implemented for notifications")


def _notify_linux(summary: str,
                  message: Optional[str] = None,
                  urgency: Optional[str] = None,
                  icon: Optional[str] = None):
    args = ["notify-send"]
    if urgency is not None:
        args.extend(["--urgency", urgency])
    if icon is not None:
        args.extend(["--icon", icon])
    args.append(summary)
    if message is not None:
        args.append(message)
    try:
        subprocess.run(args)
    except FileNotFoundError as error:
        raise FileNotFoundError("The program 'notify-send' must be installed "
                                "on the system for notifications to work. "
                                + str(error))
