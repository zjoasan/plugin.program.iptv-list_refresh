"""
    Plugin for Launching programs
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon

# plugin constants
__plugin__ = "plugin.program.iptv-list_refresh"
__author__ = "Zjoasan"
__url__ = "https://github.com/zjoasan/"
__git_url__ = "https://github.com/zjoasan/"
__credits__ = "https://github.com/bmillham"
__version__ = "0.0.3"

dialog = xbmcgui.Dialog()
addon = xbmcaddon.Addon(id='plugin.program.iptv-list_refresh')
response = dialog.yesno('Reboot Warning', 'This will refresh you local m3u, but will reboot the system when it's done. Continue?', yeslabel='Yes', nolabel='NO!')
if resonse:
	
else:
	xbmc.executebuiltin('ActivateWindow(10000,return)')