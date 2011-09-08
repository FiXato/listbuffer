# -*- coding: utf-8 -*-
#
# ListBuffer, version 0.1 for WeeChat version 0.3
#
#   Show /list results in a common buffer and interact with them.
#
#   This script allows you to easily join channels from the /list output.
#   It will open a common buffer for the /list result, through which you
#   browse with your cursor keys, and join with the enter key.
#
# History:
# 2011-09-08: FiXato:
#   version 0.1:  initial release.
#                 - added a common buffer for /list results
#                 - added highlighting for currently selected line
#                 - added /join support via enter key
#                 - added scroll_top and scroll_bottom support
#
# Acknowledgements:
#   - Sebastien "Flashcode" Helleu, for developing a kick-ass IRC client
#     and the iset.pl script which inspired me to this script.
#   - Nils "nils_2" Görs, for his contributions to iset.pl which served as
#     example code.
#   - David "drubin" Rubin, for his urlgrab.py script, which also served
#     as example code.
#   - ArZa, whose listsort.pl script helped me getting started with 
#     grabbing the /list results. Parts of his code have been shamelessly
#     copied and ported to Python.
#   - Khaled Mardam-Bey, for making me yearn for similar /list support in 
#     WeeChat as mIRC already offered. :P
#
# TODO: 
#   - Auto-scroll selected line upon window scroll.
#   - Add option to hide already joined channels.
#   - Add sorting methods
#   - Add default sorting option
#   - Add channel padding length option
#   - Add usercount padding length option
#   - Add modes padding length option
#   - Add auto-join support
#   - Detect if channel is already in auto-join
#   - Allow automatically switching to the listbuffer
#
# Copyright (c) 2011 Filip H.F. "FiXato" Slagter,
#   <FiXato [at] Gmail [dot] com>
#   http://google.com/profiles/FiXato
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
SCRIPT_NAME    = "listbuffer"
SCRIPT_AUTHOR  = "Filip H.F. 'FiXato' Slagter <fixato [at] gmail [dot] com>"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "A common buffer for /list output."
SCRIPT_COMMAND = "listbuffer"

import_ok = True

try:
  import weechat
except ImportError:
  print "This script must be run under WeeChat."
  import_ok = False

import re

lb_buffer = None
lb_channels = []
lb_network = None
#                              server numeric Nick Chan  Users Modes/Topic
lb_channel_list_expression = '(:\S+) (\d{3}) (\S+) (\S+) (\d+) :\[(.*?)\] ?(.*)'


# Create listbuffer.
def lb_create_buffer():
  global lb_buffer, lb_curline

  if not lb_buffer:
    # Sets notify to 0 as this buffer does not need to be in hotlist.
    lb_buffer = weechat.buffer_new("listbuffer", "lb_input_cb", \
                "", "lb_close_cb", "")
    weechat.buffer_set(lb_buffer, "title", "/LIST buffer")
    weechat.buffer_set(lb_buffer, "notify", "0")
    weechat.buffer_set(lb_buffer, "nicklist", "0")
    weechat.buffer_set(lb_buffer, "type", "free")
    weechat.buffer_set(lb_buffer, "key_bind_ctrl-L", "/listbuffer **refresh")
    weechat.buffer_set(lb_buffer, "key_bind_meta2-A", "/listbuffer **up")
    weechat.buffer_set(lb_buffer, "key_bind_meta2-B", "/listbuffer **down")
    weechat.buffer_set(lb_buffer, "key_bind_meta2-1~", "/listbuffer **scroll_top")
    weechat.buffer_set(lb_buffer, "key_bind_meta2-4~", "/listbuffer **scroll_bottom")
    weechat.buffer_set(lb_buffer, "key_bind_meta-ctrl-J", "/listbuffer **enter")
    weechat.buffer_set(lb_buffer, "key_bind_ctrl-M", "/listbuffer **enter")
    weechat.buffer_set(lb_buffer, "key_bind_meta-ctrl-M", "/listbuffer **enter")
    lb_curline = 0

def lb_list_start(data, signal, message):
  global lb_channels, lb_network
  lb_create_buffer()
  lb_channels = []
  lb_network = signal.split(',')[0]
  return weechat.WEECHAT_RC_OK

def lb_list_chan(data, signal, message):
  global lb_channels, lb_buffer
  
  for chan_data in re.findall(lb_channel_list_expression,message):
    lb_channels.append({
      'server':  chan_data[0][1:-1],
      'numeric': chan_data[1],
      'nick':    chan_data[2], 
      'channel': chan_data[3], 
      'users':   chan_data[4],
      'modes':   chan_data[5],
      'topic':   weechat.hook_modifier_exec("irc_color_decode", "1", chan_data[6])
    })
  return weechat.WEECHAT_RC_OK


def lb_list_end(data, signal, message):
  global lb_channels
  global lb_buffer

  lb_refresh()
  return weechat.WEECHAT_RC_OK


def keyEvent (data, buffer, args):
  global lb_options
  
  lb_options[args]()

def lb_input_cb(data, buffer, input_data):
  global lb_options, lb_curline

  lb_options[input_data]()
  return weechat.WEECHAT_RC_OK
  
def lb_refresh():
  global lb_channels

  y = 0
  for list_data in lb_channels:
    lb_refresh_line(y)
    y += 1
  return

def lb_refresh_line(y):
  global lb_buffer, lb_curline, lb_channels

  if y >= 0 and y < len(lb_channels):
    formatted_line = lb_line_format(lb_channels[y], y == lb_curline)
    weechat.prnt_y(lb_buffer, y, formatted_line)
  
def lb_refresh_curline():
  global lb_curline

  lb_refresh_line(lb_curline-1)
  lb_refresh_line(lb_curline)
  lb_refresh_line(lb_curline+1)
  return
  
def lb_line_format(list_data,curr=False):
  str = ""
  if (curr):
    str += weechat.color("yellow,red")
  str += "%s%25s %6s " % (weechat.color("bold"), list_data['channel'], "(%s)" % list_data['users'])
  str += "%10s: " % ("[%s]" % list_data['modes'])
  str += "%s" % list_data['topic']
  return str

def lb_line_up():
  global lb_curline

  if lb_curline <= 0:
    return
  lb_curline -= 1
  lb_refresh_curline()
  lb_check_outside_window()
  return

def lb_line_down():
  global lb_curline, lb_channels

  if lb_curline+1 >= len(lb_channels):
    return
  lb_curline += 1
  lb_refresh_curline()
  lb_check_outside_window()
  return

def lb_line_run():
  global lb_channels, lb_curline, lb_network

  buffer = weechat.buffer_search("irc", "server.%s" % lb_network)
  channel = lb_channels[lb_curline]['channel']
  command = "/join %s" % channel
  weechat.command(buffer, command)
  return

def lb_line_select():
  return

def lb_scroll_top():
  global lb_curline

  old_y = lb_curline
  lb_curline = 0
  lb_refresh_curline()  
  lb_refresh_line(old_y)
  weechat.command(lb_buffer, "/window scroll_top")
  return

def lb_scroll_bottom():
  global lb_curline, lb_channels

  old_y = lb_curline
  lb_curline = len(lb_channels)-1
  lb_refresh_curline()
  lb_refresh_line(old_y)
  weechat.command(lb_buffer, "/window scroll_bottom")
  return

def lb_check_outside_window():
  global lb_buffer, lb_curline

  if (lb_buffer):
    infolist = weechat.infolist_get("window", "", "current")
    if (weechat.infolist_next(infolist)):
      start_line_y = weechat.infolist_integer(infolist, "start_line_y")
      chat_height = weechat.infolist_integer(infolist, "chat_height")
      if(start_line_y > lb_curline):
        weechat.command(lb_buffer, "/window scroll -%i" %(start_line_y - lb_curline))
      elif(start_line_y <= lb_curline - chat_height):
        weechat.command(lb_buffer, "/window scroll +%i"%(lb_curline - start_line_y - chat_height + 1))
    weechat.infolist_free(infolist)

def lb_close_cb(*kwargs):
  """ A callback for buffer closing. """
  global lb_buffer

  lb_buffer = None
  return weechat.WEECHAT_RC_OK

lb_options = {
  'refresh'     : lb_refresh,
  'up'          : lb_line_up,
  'down'        : lb_line_down,
  'enter'       : lb_line_run,
  'space'       : lb_line_select,
  'scroll_top'  : lb_scroll_top,
  'scroll_bottom': lb_scroll_bottom
}

def lb_command_main(data, buffer, args):
  if args[0:2] == "**":
    keyEvent(data, buffer, args[2:])
  return weechat.WEECHAT_RC_OK

if __name__ == "__main__" and import_ok:
  if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION,
                      SCRIPT_LICENSE, SCRIPT_DESC, "lb_close_cb", ""):
    #        # Set default settings
    #        for option, default_value in lb_settings.iteritems():
    #            if not weechat.config_is_set_plugin(option):
    #                weechat.config_set_plugin(option, default_value)

    lb_buffer = weechat.buffer_search("python", "listbuffer")

    lb_create_buffer()

    weechat.hook_signal("*,irc_in_321", "lb_list_start", "")
    weechat.hook_signal("*,irc_in_322", "lb_list_chan", "")
    weechat.hook_signal("*,irc_in_323", "lb_list_end", "")
    
    weechat.hook_command(SCRIPT_COMMAND, 
                          "List Buffer",
                          "", "", "", 
                          "lb_command_main", "")