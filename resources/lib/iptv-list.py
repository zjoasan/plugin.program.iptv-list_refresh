#!/usr/bin/python3
#

# pip3 install m3u-parser
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
from m3u_parser import M3uParser

parser = M3uParser()
# You could set check_live to True to only grab streams that are tested and working.
# I have not tested this.
parser.parse_m3u(path='http://alienstreams.fi:7070/playlist/joose.just.joose@gmail.com/Km9C4FP4Gp/m3u_plus', check_live=False)
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
parser.to_file("out.m3u", format="m3u")
