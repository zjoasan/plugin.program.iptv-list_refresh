"""
    Module for interacting with other addons
"""

# -*- coding: UTF-8 -*-
# main imports
import json
import xbmc
import xbmcaddon

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
        xbmcaddon.Addon(pvr.iptvsimple).setSettingInt(m3uPathType, 0)
        xbmcaddon.Addon(pvr.iptvsimple).setSettingString(m3uPath, newpath)
        xbmcaddon.Addon(pvr.iptvsimple).setSettingString(m3uUrl, "")
        xbmcaddon.Addon(pvr.iptvsimple).setSettingBool(m3uCache, False)
#right now it's locked to pvr.iptvsimple, could take param for addon and m3ulist