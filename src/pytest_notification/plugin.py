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

from _pytest.config.argparsing import Parser as PytestParser

import pytest

from .notifications import DEFAULT_FAIL_ICON, DEFAULT_SUCCESS_ICON, notify
from .sound import DEFAULT_FAIL_SOUND, DEFAULT_SUCCESS_SOUND, play_sound


def pytest_addoption(parser: PytestParser):
    """
    Add options to the pytest parser. Works like the built-in argparse module.
    This function is used by pytest. It is not meant to be called from outside.
    """
    parser.addoption("--notify", action="store_true",
                     help="Sends a desktop notification when pytest is "
                          "finished. (Only implemented on Linux. Requires the "
                          "'notify-send' program in PATH on Linux.")

    parser.addoption("--sound", "--play-sound", action="store_true",
                     help="Plays a sound when pytest is finished. (Only "
                          "implemented on Linux and Macintosh systems).")

    parser.addoption("--disturb", action="store_true",
                     help="Alias for --notify --sound")


def pytest_sessionfinish(session: pytest.Session, exitstatus: int):
    """
    Hook function used by pytest. This code will be run at the end of a
    pytest session.
    """
    notify_on = session.config.getoption("notify")
    sound_on = session.config.getoption("sound")
    disturb = session.config.getoption("disturb")

    if notify_on or disturb:
        if exitstatus == 0:
            notify("Pytest", "All tests are succesfull!",
                   icon=DEFAULT_SUCCESS_ICON)
        else:
            notify("Pytest", "Failing tests detected!",
                   icon=DEFAULT_FAIL_ICON)

    if sound_on or disturb:
        if exitstatus == 0:
            play_sound(DEFAULT_SUCCESS_SOUND)
        else:
            play_sound(DEFAULT_FAIL_SOUND)
