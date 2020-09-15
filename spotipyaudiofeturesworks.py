# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import spotipy.util as util

import spotipy.oauth2 as oauth2
import pprint




CLIENT_ID = "894a0b2883b6401781728255a20a9bde"
CLIENT_SECRET = "610654fe15d44e03b683fd950cbf30af"

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)






##if len(sys.argv) > 1:
##    artist_name = ' '.join(sys.argv[1:])
##    
##else:
##    artist_name = 'simon kilshaw'
##
##results = spotify.search(q=artist_name, limit=2)
##tids = []
##for i, t in enumerate(results['tracks']['items']):
##    print(' ', i, t['name'])
##    tids.append(t['uri'])
##
##
##
##features = spotify.audio_features(tids)
##print(features)
##print(features[0]['tempo'])
##print(features[1]['tempo'])


############ deeper audio analysis for one track
####https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/

if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    tid = 'spotify:track:02z6HdsV080Ld4z8ffgaMh'

start = time.time()
analysis = spotify.audio_analysis(tid)
delta = time.time() - start

##print(analysis['track']['key'])##0c1db2d3eb4e5f etcccc
##print(analysis['track']['mode'])##0 minor 1 major
key = analysis['track']['key']
mode = analysis['track']['mode']
tempo = analysis['track']['tempo']
sig = analysis['track']['time_signature']



track = spotify.track(tid)
print(track['name'])
print("BPM: " + str(tempo))
print (sig)

##print(json.dumps(analysis, indent=4))
##print("analysis retrieved in %.2f seconds" % (delta,))


if key == 5:
    print("F")
if mode == 0:
    print("Minor")
if mode == 1:
    print("Major")
    
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(analysis['sections'])






















