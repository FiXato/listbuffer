# DEPRECATED

This repository is no longer maintained. Please see https://github.com/FiXato/weechat_scripts instead.

# listbuffer.py, version 0.8.1 for WeeChat version 0.3
******************************************************************************

Show /list results in a common buffer and interact with them.

This script allows you to easily join channels from the /list output.
It will open a common buffer for the /list result, through which you
browse with your cursor keys, and join with the meta-enter keys.
Adjust sorting with meta->, meta-< and meta-/ keybindings.

This is a script for the WeeChat chat client, www.weechat.org


## Configuration instructions
******************************************************************************


## Features
******************************************************************************

### Current:

* One common buffer for all your /list results
* Navigate through the channels with your cursor keys
* Join a channel with the enter key after highlighting its line
* Scroll to the top/bottom of the channel list
* Invert the sort order of the channel list
* Padded channel names, user counts and modes for a clean overview
* Tested (and passed) on the following IRCds:
    * UnrealIRCd (tested at Chat4All.org)
    * Charybdis (tested at Esper.net)
    * ircd-seven-1.0.3 (tested at freenode) 
    * IRCnet (irc2.11.2p3)
    * Hybrid (hybrid-7.2.3+plexus-3.0.1) (tested at Rizon.net)
    * Bahamut (bahamut-1.8(06))

### Future:

* See ToDo in listbuffer.py for now

## History
******************************************************************************

### 2011-09-08: FiXato:

* version 0.1:  initial release.
    * added a common buffer for /list results
    * added highlighting for currently selected line
    * added /join support via enter key
    * added scroll_top and scroll_bottom support

* version 0.2:  /list format bugfix
    * added support for /list results without modes
    * some servers don't send 321 (/list start). Taken into account.

* version 0.3: Sorting support
    * Added some basic sorting support. Scroll through sort options
      with meta-> and meta-< (users, channel, topic, modes)

### 2011-09-19: FiXato

* version 0.4: 
    * Case-insensitive buffer lookup fix.
    * Removed default enter keybind

### 2011-12-28: troydm:

* version 0.5: It's an upside-down-world
    * Added inverted sorting support provided by Dmitry "troydm" Geurkov
      Use meta-/ to switch between inverted and regular sorting.

### 2012-02-10: FiXato:

* version 0.6: Stop shoving that buffer in my face!
    * The listbuffer should no longer pop up by itself when you load the script.
      It should only pop up now when you actually do a /list query.

* version 0.7: .. but please pop it up in my current window when I ask for it
    * Added setting plugins.var.python.listbuffer.autofocus
      This will autofocus the listbuffer in the current window if another window isn't
      already showing it, and of course only when the user issues /list

### 2012-07-10: FiXato:

* version 0.7.1: Forgetful bugfix
    * Made sure lb_curline global variable is defined

### 2013-03-19: FiXato:

* version 0.8: Sorted out the sorting
    * Added automatically updating options for sorting: 
      * plugins.var.python.listbuffer.sort_inverted
      * plugins.var.python.listbuffer.sort_order 
* version 0.8.1: Pad it baby!
    * Channel modes are equally padded even when there are no channel modes.
    * Added padding options: 
      * plugins.var.python.listbuffer.modes_min_width
      * plugins.var.python.listbuffer.channel_min_width
      * plugins.var.python.listbuffer.users_min_width

## ToDo
******************************************************************************

  - Auto-scroll selected line upon window scroll.
  - Add option to hide already joined channels.
  - Improve sorting methods
  - Add auto-join support
  - Detect if channel is already in auto-join
  - Allow automatically switching to the listbuffer
  - Add support for ALIS (/squery alis LIST * -mix 100 (IRCNet)
  - Make colours configurable
  - Limit number of channels to parse
  - Add filter support a la iset
  - Allow selecting multiple channels
  - Add optional command redirection.

## Notes on Patches/Pull Requests
******************************************************************************

1. Fork the project.
2. Make your feature addition or bug fix.
3. Preferably add tests for it (even though I don't have tests myself at the moment). 
  This is important so I don't break it in a future version unintentionally.
4. Commit, but do not mess with gemspec, version, history, or README.
  Want to have your own version? Bump version in a separate commit!
  That way I can ignore that commit when I pull.
5. Send me a pull request. Bonus points for topic branches.
6. You'll be added to the credits.

## Acknowledgements
******************************************************************************

Thanks go out to:

* Dmitry "troydm" Geurkov, for providing the inverse-sorting patch to the project.
* Sebastien "Flashcode" Helleu, for developing the kick-ass IRC client WeeChat
    and the iset.pl script which inspired me to this script.
* Nils "nils_2" Görs, for his contributions to iset.pl which served as
    example code.
* David "drubin" Rubin, for his urlgrab.py script, which also served
    as example code.
* ArZa, whose listsort.pl script helped me getting started with 
    grabbing the /list results. Parts of his code have been shamelessly
    copied and ported to Python.
* Khaled Mardam-Bey, for making me yearn for similar /list support in 
    WeeChat as mIRC already offered. :P
* mave_, for pointing out that sort orders weren't remembered.

## Copyright
******************************************************************************

Copyright (c) 2011,2012,2013 Filip H.F. "FiXato" Slagter,
    <FiXato [at] Gmail [dot] com>
    http://profile.fixato.org

See LICENSE for details.
