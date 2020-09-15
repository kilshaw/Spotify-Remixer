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
import webbrowser
import socket

HOST = "127.0.0.1"
UDP_IP = "127.0.0.1"
UDP_PORT = 3232

PORTA = 6255
PORTB = 6256
PORTC = 6257
PORTD = 6258
PORTE = 6259
PORTF = 6260
PORTG = 6261
PORTH = 6262
PORTI = 6263
PORTJ = 6264
PORTK = 6265
PORTL = 6266
PORTM = 6267
PORTN = 6268
PORTO = 6269
PORTP = 6270
PORTQ = 6271
PORTR = 6272
PORTS = 6273
PORTT = 6274
PORTU = 6275
PORTV = 6276
PORTW = 6277
PORTX = 6278
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
song = data.decode('utf-8')
     
     



market = [ "AD", "AR", "AT", "AU", "BE", "BG", "BO", "BR", "CA", "CH", "CL", "CO", "CR", "CY", 
      "CZ", "DE", "DK", "DO", "EC", "EE", "ES", "FI", "FR", "GB", "GR", "GT", "HK", "HN", "HU", 
      "ID", "IE", "IS", "IT", "JP", "LI", "LT", "LU", "LV", "MC", "MT", "MX", "MY", "NI", "NL", 
      "NO", "NZ", "PA", "PE", "PH", "PL", "PT", "PY", "SE", "SG", "SK", "SV", "TH", "TR", "TW", 
      "US", "UY", "VN" ]








CLIENT_ID = "894a0b2883b6401781728255a20a9bde"
CLIENT_SECRET = "610654fe15d44e03b683fd950cbf30af"

credentials = oauth2.SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET)

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)



##track = "simon kilshaw forget about you"
##track = "am ador ya"
##track = "simon kilshaw calon lan"
track = "jenn kirby sing in the shower"
track = song

res = spotify.search(track, type="track", market=market, limit=1)
pp = pprint.PrettyPrinter(indent=4)
##pp.pprint(res['tracks']['items'][0]['artists'])
##pp.pprint(res['tracks']['items'][0]['id'])
trackID = res['tracks']['items'][0]['id']

artist = res['tracks']['items'][0]['artists'][0]['name']
s.sendto(str(artist).encode('utf-8'),(HOST,PORTU))
link = res['tracks']['items'][0]['external_urls']['spotify']
s.sendto(str(link).encode('utf-8'),(HOST,PORTV))
##print(trackID)
print(artist)
##print(link)
webbrowser.get("chrome").open(link)










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

##print(features[0]['tempo'])
##print(features[1]['tempo'])


############ deeper audio analysis for one track
####https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-analysis/



if len(sys.argv) > 1:
    tid = sys.argv[1]
else:

    
    ##tid = 'spotify:track:02z6HdsV080Ld4z8ffgaMh'
    tid = 'spotify:track:' + trackID

start = time.time()
analysis = spotify.audio_analysis(tid)
delta = time.time() - start

##print(analysis['track']['key'])##0c1db2d3eb4e5f etcccc
##print(analysis['track']['mode'])##0 minor 1 major
key = analysis['track']['key']
mode = analysis['track']['mode']
tempo = analysis['track']['tempo']
sig = analysis['track']['time_signature']

##print(features)



track = spotify.track(tid)
print(track['name'])
print("BPM: " + str(tempo))
print (str(sig) +"/4")


features = spotify.audio_features(tid)
##pp = pprint.PrettyPrinter(width=41, compact=True)
##pp.pprint(features)
print (features[0]['danceability'])
s.sendto(str(features[0]['danceability']).encode('utf-8'),(HOST,PORTJ))
print (features[0]['acousticness'])
s.sendto(str(features[0]['acousticness']).encode('utf-8'),(HOST,PORTK))
print (features[0]['energy'])
s.sendto(str(features[0]['energy']).encode('utf-8'),(HOST,PORTL))
print (features[0]['instrumentalness'])
s.sendto(str(features[0]['instrumentalness']).encode('utf-8'),(HOST,PORTM))
print (features[0]['liveness'])
s.sendto(str(features[0]['liveness']).encode('utf-8'),(HOST,PORTN))
print (features[0]['loudness'])
s.sendto(str(features[0]['loudness']).encode('utf-8'),(HOST,PORTO))
print (features[0]['speechiness'])
s.sendto(str(features[0]['speechiness']).encode('utf-8'),(HOST,PORTP))
print (features[0]['valence'])
s.sendto(str(features[0]['valence']).encode('utf-8'),(HOST,PORTQ))
print (features[0]['mode'])
s.sendto(str(features[0]['mode']).encode('utf-8'),(HOST,PORTR))
print (features[0]['tempo'])
s.sendto(str(features[0]['tempo']).encode('utf-8'),(HOST,PORTS))
print (features[0]['time_signature'])
s.sendto(str(features[0]['time_signature']).encode('utf-8'),(HOST,PORTT))





##print(json.dumps(analysis, indent=4))
##print("analysis retrieved in %.2f seconds" % (delta,))

if key == 0:
    print("C")
    c = "C natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 1:
    print("C#")
    c = "C sharp"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 2:
    print("D")
    c = "D natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 3:
    print("D#")
    c = "D sharp"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 4:
    print("E")
    c = "e"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 5:
    print("F")
    c = "F natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 6:
    print("F#")
    c = "F sharp"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 7:
    print("G")
    c = "G natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 8:
    print("G#")
    c = "G sharp"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 9:
    print("A")
    c = "A natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 10:
    print("A#")
    c = "A sharp"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))
if key == 11:
    print("B")
    c = "B natural"
    s.sendto(str(c).encode('utf-8'),(HOST,PORTW))



    

if mode == 0:
    print("Minor")
    moder = "Minor"
    s.sendto(str(moder).encode('utf-8'),(HOST,PORTX))
if mode == 1:
    print("Major")
    moder = "Major"
    s.sendto(str(moder).encode('utf-8'),(HOST,PORTX))
    

print (len(analysis['bars']))
print (len(analysis['beats']))
print (len(analysis['tatums']))
print (len(analysis['sections']))
sectionnumber = len(analysis['sections'])

if sectionnumber == 1:
    a1 = analysis['sections'][0]
    print (analysis['sections'][0])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))

if sectionnumber == 2:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))

if sectionnumber == 3:
    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    a3 = analysis['sections'][2]
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(a3).encode('utf-8'),(HOST,PORTE))

if sectionnumber == 4:

    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    a3 = analysis['sections'][2]
    a4 = analysis['sections'][3]
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(a3).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(a4).encode('utf-8'),(HOST,PORTF))

if sectionnumber == 5:

    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    a3 = analysis['sections'][2]
    a4 = analysis['sections'][3]
    a5 = analysis['sections'][4]
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(a3).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(a4).encode('utf-8'),(HOST,PORTF))
    s.sendto(str(a5).encode('utf-8'),(HOST,PORTG))

if sectionnumber == 6:
    
    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    a3 = analysis['sections'][2]
    a4 = analysis['sections'][3]
    a5 = analysis['sections'][4]
    a6 = analysis['sections'][5]
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(a3).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(a4).encode('utf-8'),(HOST,PORTF))
    s.sendto(str(a5).encode('utf-8'),(HOST,PORTG))
    s.sendto(str(a6).encode('utf-8'),(HOST,PORTH))

if sectionnumber == 7:
    a1 = analysis['sections'][0]
    a2 = analysis['sections'][1]
    a3 = analysis['sections'][2]
    a4 = analysis['sections'][3]
    a5 = analysis['sections'][4]
    a6 = analysis['sections'][5]
    a7 = analysis['sections'][6]
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    s.sendto(str(a1).encode('utf-8'),(HOST,PORTC))
    s.sendto(str(a2).encode('utf-8'),(HOST,PORTD))
    s.sendto(str(a3).encode('utf-8'),(HOST,PORTE))
    s.sendto(str(a4).encode('utf-8'),(HOST,PORTF))
    s.sendto(str(a5).encode('utf-8'),(HOST,PORTG))
    s.sendto(str(a6).encode('utf-8'),(HOST,PORTH))
    s.sendto(str(a7).encode('utf-8'),(HOST,PORTI))

if sectionnumber == 8:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])

if sectionnumber == 9:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])
    print (analysis['sections'][8])

if sectionnumber == 10:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])
    print (analysis['sections'][8])
    print (analysis['sections'][9])

if sectionnumber == 11:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])
    print (analysis['sections'][8])
    print (analysis['sections'][9])
    print (analysis['sections'][10])

if sectionnumber == 12:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])
    print (analysis['sections'][8])
    print (analysis['sections'][9])
    print (analysis['sections'][10])
    print (analysis['sections'][11])

if sectionnumber == 13:
    print (analysis['sections'][0])
    print (analysis['sections'][1])
    print (analysis['sections'][2])
    print (analysis['sections'][3])
    print (analysis['sections'][4])
    print (analysis['sections'][5])
    print (analysis['sections'][6])
    print (analysis['sections'][7])
    print (analysis['sections'][8])
    print (analysis['sections'][9])
    print (analysis['sections'][10])
    print (analysis['sections'][11])
    print (analysis['sections'][12])




print (len(analysis['segments']))
print (analysis['segments'][0]['pitches'])
print (analysis['segments'][0]['timbre'])

json_data = analysis['segments']  

for item in json_data:
    for data_item in item['pitches']:
        print (data_item)
        pitchy = data_item
        s.sendto(str(pitchy).encode('utf-8'),(HOST,PORTA))



    for data_item in item['timbre']:
        print (data_item)
        s.sendto(str(data_item).encode('utf-8'),(HOST,PORTB))


















