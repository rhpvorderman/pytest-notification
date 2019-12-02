Pytest-notification
===================

A plugin for pytest that sends notifications if a ``--notify`` flag is passed
to pytest on the command line. It plays sounds when a ``--sound`` or
``--play-sound`` flag is passed.

The notifications and sounds are different depending whether the test run
has passed or failed.

The messages and sounds are only played when the flags are passed. This allows
you to turn it on only for those tests for which you expect a long time is
needed.

Alternatives
============

`pytest-notifier <https://github.com/ratson/pytest-notifier>`_ always sends
a notification. It can be turned of with ``--notify-off``. This is a
fundamentally different design choice, which is why this package was created.
Pytest-notifier has been around for a long time and is still being actively
maintained. It does not support playing sounds, but it does support Mac OS X
notifications.

Installation
============

Linux
-----

pytest-notification can be installed with ``pip install pytest-notification``.

On Linux notifications are supported via the ``notify-send`` program. On Debian,
Ubuntu and derived distros this is available in the ``libnotify-bin`` package.

On Linux sound is supported via the ``paplay`` program. On Debian, Ubuntu and
derived distros this available in the ``pulseaudio-utils`` pacakge.

The installation for Ubuntu should be:

.. code-block::bash
    sudo apt update
    sudo apt install libnotify-bin pulseaudio-utils
    pip install pytest-notification


Mac OS X
--------

On Mac OS X sound is implemented via the ``afplay`` program, which should be
installed by default. Since I do not own a mac I can not test this feature.
pull requests are welcome.

On Mac OS X notifications are not supported. Feel free to make a pull request.
Alternatively you could take a look at `pytest-notifier
<https://github.com/ratson/pytest-notifier>`_, which does support Mac OS X.

Windows
-------
Windows is not supported. In theory the ``winsound`` module could be used to
play sounds, but this only supports wave files. These are very big and
cumbersome to distribute. I have not actively looked for a way to create a
message on windows. There will probably be some powershell command that can
pull this off. Pull requests are welcome.

