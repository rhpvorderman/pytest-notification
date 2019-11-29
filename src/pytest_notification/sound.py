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
from pathlib import Path

SOUNDS_DIR = (Path(__file__).parent / Path("sounds")).absolute()
DEFAULT_SUCCESS_SOUND = str(SOUNDS_DIR / Path("applause.oga"))
DEFAULT_FAIL_SOUND = str(SOUNDS_DIR / Path("buzzer.oga"))


def play_sound(sound_file: str):
    if sys.platform == "linux":
        # paplay comes from PulseAudio and should be installed by default on
        # most systems.
        _play_sound_unix(sound_file, program="paplay")
    elif sys.platform == "darwin":
        # Afplay comes installed by default on Macintosh
        _play_sound_unix(sound_file, program="afplay")
    else:
        # A windows implementation should be possible with the winsound
        # implementation, but that does not play ogg audio.
        raise NotImplementedError(
            "Playing sounds not supported by pytest-notification on {}"
            "".format(sys.platform))


def _play_sound_unix(sound_file: str, program):
    """
    Play a sound file on unix with the program.
    :param sound_file: Path to the sound file.
    :param program: Which program to use.
    :return: No returns. Plays a sound file.
    """
    # Play the sound non blocking, use Popen.
    subprocess.Popen([program, sound_file])
