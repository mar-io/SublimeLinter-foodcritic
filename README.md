SublimeLinter-contrib-foodcritic
================================

[![Build Status](https://travis-ci.org/mar-io/SublimeLinter-foodcritic.svg?branch=master)](https://travis-ci.org/mar-io/SublimeLinter-foodcritic)

This linter plugin for [SublimeLinter][docs] provides an interface to [foodcritic](http://acrmp.github.io/foodcritic/). It will be used with files that have the “ruby” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `foodcritic` is installed on your system. To install `foodcritic`, do the following:

1. Install [Ruby](http://www.ruby-lang.org).

1. Install `foodcritic` by typing the following in a terminal:
   ```
   [sudo] gem install foodcritic
   ```

1. If you are using `rbenv` or `rvm`, ensure that they are loaded in your shell’s correct startup file. See [here](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#shell-startup-files) for more information.


**Note:** This plugin requires `foodcritic` 2.2.0 or later.

### Linter configuration
In order for `foodcritic` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `foodcritic`, you can proceed to install the SublimeLinter-contrib-foodcritic plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `foodcritic`. Among the entries you should see `SublimeLinter-contrib-foodcritic`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

The only rules that are excluded by default is FC011,FC031,FC033,FC045. The reason these rules are excluded is that they match file names with metadata/template files within the cookbook structure. This was out of my scope. I simply want to lint the actual cookbook file. However, I am open to pull requests.

Foodcritic should still be used as part of your CI process to ensure the metadata files of your cookbook are properly annotated.


## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
