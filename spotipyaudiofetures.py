# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
import spotipy.util as util

import spotipy.oauth2 as oauth2





CLIENT_ID = "894a0b2883b6401781728255a20a9bde"
CLIENT_SECRET = "610654fe15d44e03b683fd950cbf30af"

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)






if len(sys.argv) > 1:
    artist_name = ' '.join(sys.argv[1:])
else:
    artist_name = 'jenn kirby'

results = spotify.search(q=artist_name, limit=2)
tids = []
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
    tids.append(t['uri'])


##start = time.time()
features = spotify.audio_features(tids)
print(features)
print(features[0]['tempo'])
print(features[1]['tempo'])





##delta = time.time() - start
##for feature in features:
##    print(json.dumps(feature, indent=4))
##    
##    analysis = spotify._get(feature['analysis_url'])
##    
##    print (analysis)
##    print(json.dumps(analysis, indent=4))
##    print()
##print("features retrieved in %.2f seconds" % (delta,))

