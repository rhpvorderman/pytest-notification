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
maintained.

