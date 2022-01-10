#!/usr/bin/python3
#

# pip3 install m3u-parser
import sys
import os
import json
import xbmc
import xbmcgui
import xbmcaddon
addon = xbmcaddon.Addon('plugin.program.iptv-list_refresh')
providerURL = addon.getSetting('entry1')
groupsallow = addon.getSetting('entry2')
userAgent = addon.getSetting('entry3')
localout = addon.getSetting('entry4')

#from m3u_parser import M3uParser
from m3u_parser.m3u_parser import M3uParser

def disable_addon(addon_id):
    request = {
        "jsonrpc": "2.0",
        "method": "Addons.SetAddonEnabled",
        "params": {
            "addonid": "%s" % addon_id,
            "enabled": False
        },
        "id": 1
    }

    xbmc.log('MyAddonName -> disabling %s' % addon_id, xbmc.LOGDEBUG)
    response = xbmc.executeJSONRPC(json.dumps(request))
    response = json.loads(response)
    try:
        return response['result'] == 'OK'
    except KeyError:
        xbmc.log('MyAddonName -> disable_addon received an unexpected response',
                 xbmc.LOGERROR)
        return False

def enable_addon(addon_id):
    request = {
        "jsonrpc": "2.0",
        "method": "Addons.SetAddonEnabled",
        "params": {
            "addonid": "%s" % addon_id,
            "enabled": True
        },
        "id": 1
    }

    xbmc.log('MyAddonName -> enabling %s' % addon_id, xbmc.LOGDEBUG)

    response = xbmc.executeJSONRPC(json.dumps(request))
    response = json.loads(response)
    try:
        return response['result'] == 'OK'
    except KeyError:
        xbmc.log('MyAddonName -> enable_addon received an unexpected response',
                 xbmc.LOGERROR)
        return False
    
def  change_m3u(newpath):
    xbmcaddon.Addon("pvr.iptvsimple").setSettingInt(m3uPathType, 0)
    xbmcaddon.Addon("pvr.iptvsimple").setSettingString(m3uPath, newpath)
    xbmcaddon.Addon("pvr.iptvsimple").setSettingString(m3uUrl, "")
    xbmcaddon.Addon("pvr.iptvsimple").setSettingBool(m3uCache, False)

parser = M3uParser()
# You could set check_live to True to only grab streams that are tested and working.
# I have not tested this.
parser.parse_m3u(path=providerURL, check_live=False)
# I used ^$ around all the filters except [VOD] so that *only* that word is matched
# as the group-title (the module calls it category).
# The reason is that filter_by uses regex, so US would match on *anything* with
# US in the category. US$ will only match on something ending in US. To ensure
# that just a single word is matched, use ^ at the start of the word.
# For the [VOD] we only want to match when it's the last part of the category.
parser.filter_by(key='category', filters=['^Sverige$',
                                     '^UK$',
                                     '^US$',
                                     '^Australien$',
                                     '^For Adults$',
                                     '\[VOD\]$'])
disable_addon("pvr.iptvsimple")
parser.to_file(localout, format="m3u")
change_m3u(localout)
enable_addon("pvr.iptvsimple")

mess = xbmcgui.Dialog()
mess.ok("Update done","New m3u-file downloaded, filtered and saved at loation set in settings.")
