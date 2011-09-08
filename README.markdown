# listbuffer.py, version 0.1 for WeeChat version 0.3
******************************************************************************

Show /list results in a common buffer and interact with them.

This script allows you to easily join channels from the /list output. 
It will open a common buffer for the /list result, through which you 
browse with your cursor keys, and join with the enter key.

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
* Padded channel names, user counts and modes for a clean overview


### Future:

* See ToDo for now

## History
******************************************************************************

*   2011-09-08: FiXato:
    version 0.1:  initial release.

        - added a common buffer for /list results
        - added highlighting for currently selected line
        - added /join support via enter key
        - added scroll_top and scroll_bottom support

## ToDo
******************************************************************************

- Auto-scroll selected line upon window scroll.
- Add option to hide already joined channels.
- Add sorting methods
- Add default sorting option
- Add channel padding length option
- Add usercount padding length option
- Add modes padding length option
- Add auto-join support
- Detect if channel is already in auto-join
- Allow automatically switching to the listbuffer

## Notes on Patches/Pull Requests
******************************************************************************

1. Fork the project.
2. Make your feature addition or bug fix.
3. Add tests for it (even though I don't have tests myself at the moment). 
  This is important so I don't break it in a future version unintentionally.
4. Commit, but do not mess with gemspec, version, history, or README.
  Want to have your own version? Bump version in a separate commit!
  That way I can ignore that commit when I pull.
5. Send me a pull request. Bonus points for topic branches.
6. You'll be added to the credits.

## Acknowledgements
******************************************************************************

Thanks go out to:

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


## Copyright
******************************************************************************

Copyright (c) 2011 Filip H.F. "FiXato" Slagter,
    <FiXato [at] Gmail [dot] com>
    http://google.com/profiles/FiXato

See LICENSE for details.