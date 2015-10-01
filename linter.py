#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Mario Harvey
# Copyright (c) 2015 Mario Harvey
#
# License: MIT
#

"""This module exports the Foodcritic plugin class."""

from SublimeLinter.lint import RubyLinter, highlight, util


class Foodcritic(RubyLinter):

    """Provides an interface to foodcritic."""

    syntax = 'ruby'
    cmd = ('foodcritic', '-t', '~FC011', '-t', '~FC031', '-t', '~FC033', '-t', '~FC045', '@')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.2.0'
    regex = r'(?P<message>FC\d+: .+): (?P<file>.+):(?P<line>.+)'
    default_type = highlight.WARNING
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'rb'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*#'
