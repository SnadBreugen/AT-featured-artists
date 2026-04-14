import urllib.request
import json
import time
import xml.etree.ElementTree as ET
import re

albums = [
    "https://www.audiotool.com/album/9pnx5/",
    "https://www.audiotool.com/album/hnwkpu4/",
    "https://www.audiotool.com/album/dgaoqtpm/",
    "https://www.audiotool.com/album/0poc9tl/",
    "https://www.audiotool.com/album/6pvw3rdg/",
    "https://www.audiotool.com/album/i0qv2qyt6/",
    "https://www.audiotool.com/album/zwhdmh/",
    "https://www.audiotool.com/album/agr87qx/",
    "https://www.audiotool.com/album/pts4e/",
    "https://www.audiotool.com/album/2gvqxec/",
    "https://www.audiotool.com/album/dfkvkal/",
    "https://www.audiotool.com/album/trxsjo/",
    "https://www.audiotool.com/album/rpzwcp4v/",
    "https://www.audiotool.com/album/xlv4lr4/",
    "https://www.audiotool.com/album/amg2pbi/",
    "https://www.audiotool.com/album/og6fd6z/",
    "https://www.audiotool.com/album/kcvqjvpm2/",
    "https://www.audiotool.com/album/8ktqn1orf/",
    "https://www.audiotool.com/album/t5tdmds/",
    "https://www.audiotool.com/album/76ipsvb/",
    "https://www.audiotool.com/album/0cszualx/",
    "https://www.audiotool.com/album/dgj432vk7/",
    "https://www.audiotool.com/album/fphr89zyy/",
    "https://www.audiotool.com/album/drwan2/",
    "https://www.audiotool.com/album/fg0yzv/",
    "https://www.audiotool.com/album/zgmrmokl0/",
    "https://www.audiotool.com/album/dyz0s22ey/",
    "https://www.audiotool.com/album/0hqoaaw/",
    "https://www.audiotool.com/album/s1xjwzjco/",
    "https://www.audiotool.com/album/dejfpldko/",
    "https://www.audiotool.com/album/q9ovx/",
    "https://www.audiotool.com/album/s1nfsuq/",
    "https://www.audiotool.com/album/8n41y2t4x/",
    "https://www.audiotool.com/album/ku50sqn/",
    "https://www.audiotool.com/album/vranm/",
    "https://www.audiotool.com/album/akswas7/",
    "https://www.audiotool.com/album/fpkdql8j/",
    "https://www.audiotool.com/album/pif3btmq/",
    "https://www.audiotool.com/album/ixieojt/",
    "https://www.audiotool.com/album/jvjotpw/",
    "https://www.audiotool.com/album/fckpbo/",
    "https://www.audiotool.com/album/pri3aji/",
    "https://www.audiotool.com/album/o15is/",
    "https://www.audiotool.com/album/huq36h9yv/",
    "https://www.audiotool.com/album/4oqrg5xs/",
    "https://www.audiotool.com/album/d6qdh/",
    "https://www.audiotool.com/album/qd3ss/",
    "https://www.audiotool.com/album/jbkwf/",
    "https://www.audiotool.com/album/mlzmzzie/",
    "https://www.audiotool.com/album/0oryk5/",
    "https://www.audiotool.com/album/gerzj5pa7/",
    "https://www.audiotool.com/album/ofu4hck4/",
    "https://www.audiotool.com/album/tzgcys/",
    "https://www.audiotool.com/album/8v9sxpke3/",
    "https://www.audiotool.com/album/blgcbm/",
    "https://www.audiotool.com/album/fegwtffwt/",
    "https://www.audiotool.com/album/qbtlhcu/",
    "https://www.audiotool.com/album/hbufuuw/",
    "https://www.audiotool.com/album/advfxu/",
    "https://www.audiotool.com/album/e0aqv0xnj/",
    "https://www.audiotool.com/album/0ybmt/",
    "https://www.audiotool.com/album/cvguob117/",
    "https://www.audiotool.com/album/ttfrr/",
    "https://www.audiotool.com/album/xmilsqmwn/",
    "https://www.audiotool.com/album/2sem3/",
    "https://www.audiotool.com/album/jkuptea/",
    "https://www.audiotool.com/album/ftnagxh/",
    "https://www.audiotool.com/album/rjggctqy/",
    "https://www.audiotool.com/album/7a9ktldnm/",
    "https://www.audiotool.com/album/3i0j5p/",
    "https://www.audiotool.com/album/mhksqxj/",
    "https://www.audiotool.com/album/rs5yxjze/",
    "https://www.audiotool.com/album/w3ob3/",
    "https://www.audiotool.com/album/naaejqfyw/",
    "https://www.audiotool.com/album/develp/",
    "https://www.audiotool.com/album/tzvj27b/",
    "https://www.audiotool.com/album/gw9cqiqr/",
    "https://www.audiotool.com/album/xdi9i0mh/",
    "https://www.audiotool.com/album/pohsz7b/",
    "https://www.audiotool.com/album/qbemlckoi/",
    "https://www.audiotool.com/album/ubguzjkis/",
    "https://www.audiotool.com/album/knl9rxjg/",
    "https://www.audiotool.com/album/bwjaynh12/",
    "https://www.audiotool.com/album/mzcfu/",
    "https://www.audiotool.com/album/pjpiou3l/",
    "https://www.audiotool.com/album/zxigd/",
    "https://www.audiotool.com/album/dvf4umd/",
    "https://www.audiotool.com/album/mogada75n/",
    "https://www.audiotool.com/album/p1yi4n/",
    "https://www.audiotool.com/album/x8x8lg2tm/",
    "https://www.audiotool.com/album/pevrv/",
    "https://www.audiotool.com/album/uq8tpudy/",
    "https://www.audiotool.com/album/mjv7t0sad/",
    "https://www.audiotool.com/album/9pfmz/",
    "https://www.audiotool.com/album/rwhjt2i/",
    "https://www.audiotool.com/album/jtpwkjj/",
    "https://www.audiotool.com/album/wmnofedc/",
    "https://www.audiotool.com/album/n2xjvl/",
    "https://www.audiotool.com/album/0i3ls/",
    "https://www.audiotool.com/album/fynka1b/",
    "https://www.audiotool.com/album/xe89crjwc/",
    "https://www.audiotool.com/album/dq1pabol/",
    "https://www.audiotool.com/album/qafr9/",
    "https://www.audiotool.com/album/djnov/",
    "https://www.audiotool.com/album/f1ailrc/",
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

def fetch_url(url, headers=None):
    req = urllib.request.Request(url, headers=headers or HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode('utf-8', errors='replace')

def fetch_track(track_id):
    url = f'https://www.audiotool.com/track/{track_id}/details.json'
    try:
        data = json.loads(fetch_url(url))
        name = data.get('name', track_id)
        creator_name = data.get('user', {}).get('name', '')
        creator_key = data.get('user', {}).get('key', '')
        # description not in details.json, try tracklist description from HTML
        desc = data.get('description', '')
        return {
            'url': f'https://www.audiotool.com/track/{track_id}/',
            'name': name,
            'track_artist': creator_name,
            'desc': desc,
            'creator_key': creator_key,
        }
    except Exception as e:
        return None

def fetch_album(album_url):
    html = fetch_url(album_url)

    # Extract track IDs - audiotool uses /track/{id}/ pattern in HTML
    track_ids = list(dict.fromkeys(re.findall(r'data-track-key="([a-zA-Z0-9_-]+)"', html)))
    track_ids = [t for t in track_ids if len(t) > 3][:11]

    if not track_ids:
        raise Exception(f'No track IDs found - HTML length: {len(html)}, sample: {html[400:450]}')

    # Extract user key
    user_keys = re.findall(r'["\'/]user/([a-z0-9_-]+)/', html)
    user_key = user_keys[0] if user_keys else ''
    at_profile = f'https://www.audiotool.com/user/{user_key}/' if user_key else ''

    # Extract artist name from album title "Edition Audiotool: {Artist}"
    artist_name = ''
    title_match = re.search(r'Edition Audiotool:\s*([^<"]+)', html)
    if title_match:
        artist_name = title_match.group(1).strip()

    # Fetch each track
    tracks = []
    for tid in track_ids:
        t = fetch_track(tid)
        if t:
            if not at_profile and t['creator_key']:
                at_profile = f"https://www.audiotool.com/user/{t['creator_key']}/"
            tracks.append({
                'url': t['url'],
                'name': t['name'],
                'track_artist': t['track_artist'],
                'desc': t['desc'],
            })
        time.sleep(0.1)

    if not tracks:
        raise Exception('No tracks loaded from API')

    return artist_name, at_profile, tracks

# Load existing
existing = []
try:
    with open('gen1_data.json', encoding='utf-8') as f:
        existing = json.load(f)
    print(f'Loaded {len(existing)} existing entries')
except:
    print('Starting fresh')

existing_by_url = {a.get('album_url','').rstrip('/'): a for a in existing}
results = []
failed = []

for i, album_url in enumerate(albums):
    clean_url = album_url.rstrip('/')
    existing_entry = existing_by_url.get(clean_url)

    print(f'[{i+1}/{len(albums)}] {album_url}', end=' ', flush=True)
    try:
        artist_name, at_profile, tracks = fetch_album(album_url)

        if existing_entry:
            # Update artist name and tracks, keep everything else
            existing_entry['artist'] = artist_name
            existing_entry['tracks'] = tracks
            if not existing_entry.get('at_profile'):
                existing_entry['at_profile'] = at_profile
            results.append(existing_entry)
            print(f'UPDATED - {artist_name} ({len(tracks)} tracks)')
        else:
            entry = {
                'artist': artist_name,
                'real_name': '',
                'date': '',
                'album_number': len(results) + 1,
                'at_profile': at_profile,
                'album_url': album_url,
                'photo': '',
                'intro': '',
                'about': '',
                'interview': [],
                'tracks': tracks,
                'social': {},
                'color1': '', 'color2': '', 'color_accent': '',
                'desc_bg': '', 'links_bar_color': '',
                'bar_color': '#111111', 'bar_text_color': '#ffffff',
                'is_hidden': False
            }
            results.append(entry)
            print(f'NEW - {artist_name} ({len(tracks)} tracks)')
    except Exception as e:
        print(f'FAILED - {e}')
        if existing_entry:
            results.append(existing_entry)
        failed.append(album_url)

    time.sleep(0.4)

with open('gen1_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f'\nDone. {len(results)} artists saved.')
if failed:
    print(f'\nFailed ({len(failed)}):')
    for u in failed:
        print(f'  {u}')