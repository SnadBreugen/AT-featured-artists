import urllib.request
import json
import time
import re
import datetime

albums = [
    ("https://www.audiotool.com/album/9pnx5/", "https://www.audiotool.com/user/ewan_mcculloch/"),
    ("https://www.audiotool.com/album/hnwkpu4/", "https://www.audiotool.com/user/xavrockbeats/"),
    ("https://www.audiotool.com/album/dgaoqtpm/", "https://www.audiotool.com/user/intracktion/"),
    ("https://www.audiotool.com/album/0poc9tl/", "https://www.audiotool.com/user/flying-baby-seal/"),
    ("https://www.audiotool.com/album/6pvw3rdg/", "https://www.audiotool.com/user/zonemusic/"),
    ("https://www.audiotool.com/album/i0qv2qyt6/", "https://www.audiotool.com/user/trancefreak12/"),
    ("https://www.audiotool.com/album/zwhdmh/", "https://www.audiotool.com/user/tocaknox/"),
    ("https://www.audiotool.com/album/agr87qx/", "https://www.audiotool.com/user/mbelow/"),
    ("https://www.audiotool.com/album/pts4e/", "https://www.audiotool.com/user/beat123/"),
    ("https://www.audiotool.com/album/2gvqxec/", "https://www.audiotool.com/user/vltra2/"),
    ("https://www.audiotool.com/album/dfkvkal/", "https://www.audiotool.com/user/shakey63/"),
    ("https://www.audiotool.com/album/trxsjo/", "https://www.audiotool.com/user/opaqity/"),
    ("https://www.audiotool.com/album/rpzwcp4v/", "https://www.audiotool.com/user/whitegrizzly/"),
    ("https://www.audiotool.com/album/xlv4lr4/", "https://www.audiotool.com/user/psychosismusic/"),
    ("https://www.audiotool.com/album/amg2pbi/", "https://www.audiotool.com/user/1n50mn1ac/"),
    ("https://www.audiotool.com/album/og6fd6z/", "https://www.audiotool.com/user/jordynth/"),
    ("https://www.audiotool.com/album/kcvqjvpm2/", "https://www.audiotool.com/user/nionsomnia/"),
    ("https://www.audiotool.com/album/8ktqn1orf/", "https://www.audiotool.com/user/farcio/"),
    ("https://www.audiotool.com/album/t5tdmds/", "https://www.audiotool.com/user/jambam/"),
    ("https://www.audiotool.com/album/76ipsvb/", "https://www.audiotool.com/user/musicmanpw/"),
    ("https://www.audiotool.com/album/0cszualx/", "https://www.audiotool.com/user/bocar_b-st/"),
    ("https://www.audiotool.com/album/dgj432vk7/", "https://www.audiotool.com/user/grotzo/"),
    ("https://www.audiotool.com/album/fphr89zyy/", "https://www.audiotool.com/user/oedipax/"),
    ("https://www.audiotool.com/album/drwan2/", "https://www.audiotool.com/user/oedipax/"),
    ("https://www.audiotool.com/album/fg0yzv/", "https://www.audiotool.com/user/fontana/"),
    ("https://www.audiotool.com/album/zgmrmokl0/", "https://www.audiotool.com/user/bluedude/"),
    ("https://www.audiotool.com/album/dyz0s22ey/", "https://www.audiotool.com/user/khoi98/"),
    ("https://www.audiotool.com/album/0hqoaaw/", "https://www.audiotool.com/user/cihangir/"),
    ("https://www.audiotool.com/album/s1xjwzjco/", "https://www.audiotool.com/user/cihangir/"),
    ("https://www.audiotool.com/album/dejfpldko/", "https://www.audiotool.com/user/zedger/"),
    ("https://www.audiotool.com/album/q9ovx/", "DELETED"),
    ("https://www.audiotool.com/album/s1nfsuq/", "https://www.audiotool.com/user/yack-fou/"),
    ("https://www.audiotool.com/album/8n41y2t4x/", "https://www.audiotool.com/user/agrippa/"),
    ("https://www.audiotool.com/album/ku50sqn/", "https://www.audiotool.com/user/amoeba/"),
    ("https://www.audiotool.com/album/vranm/", "https://www.audiotool.com/user/crazydruminator/"),
    ("https://www.audiotool.com/album/akswas7/", "https://www.audiotool.com/user/markolmx/"),
    ("https://www.audiotool.com/album/fpkdql8j/", "https://www.audiotool.com/user/tenji240/"),
    ("https://www.audiotool.com/album/pif3btmq/", "https://www.audiotool.com/user/nmgbeats/"),
    ("https://www.audiotool.com/album/ixieojt/", "https://www.audiotool.com/user/southbronxden/"),
    ("https://www.audiotool.com/album/jvjotpw/", "https://www.audiotool.com/user/tornsage/"),
    ("https://www.audiotool.com/album/fckpbo/", "https://www.audiotool.com/user/vort/"),
    ("https://www.audiotool.com/album/pri3aji/", "https://www.audiotool.com/user/djcandie/"),
    ("https://www.audiotool.com/album/o15is/", "https://www.audiotool.com/user/perrier/"),
    ("https://www.audiotool.com/album/huq36h9yv/", "https://www.audiotool.com/user/daftwill/"),
    ("https://www.audiotool.com/album/4oqrg5xs/", "https://www.audiotool.com/user/slopo/"),
    ("https://www.audiotool.com/album/d6qdh/", "https://www.audiotool.com/user/cgman/"),
    ("https://www.audiotool.com/album/qd3ss/", "https://www.audiotool.com/user/joa/"),
    ("https://www.audiotool.com/album/jbkwf/", "https://www.audiotool.com/user/manuege_el/"),
    ("https://www.audiotool.com/album/mlzmzzie/", "DELETED"),
    ("https://www.audiotool.com/album/0oryk5/", "https://www.audiotool.com/user/tottenhauser/"),
    ("https://www.audiotool.com/album/gerzj5pa7/", "https://www.audiotool.com/user/fauko/"),
    ("https://www.audiotool.com/album/ofu4hck4/", "https://www.audiotool.com/user/nowai/"),
    ("https://www.audiotool.com/album/tzgcys/", "https://www.audiotool.com/user/trance10/"),
    ("https://www.audiotool.com/album/8v9sxpke3/", "https://www.audiotool.com/user/gabriel_evangelistaadao/"),
    ("https://www.audiotool.com/album/blgcbm/", "DELETED"),
    ("https://www.audiotool.com/album/fegwtffwt/", "https://www.audiotool.com/user/infyuthsion/"),
    ("https://www.audiotool.com/album/qbtlhcu/", "https://www.audiotool.com/user/universecosmic/"),
    ("https://www.audiotool.com/album/hbufuuw/", "https://www.audiotool.com/user/khman750/"),
    ("https://www.audiotool.com/album/advfxu/", "DELETED"),
    ("https://www.audiotool.com/album/e0aqv0xnj/", "https://www.audiotool.com/user/mikke5885/"),
    ("https://www.audiotool.com/album/0ybmt/", "https://www.audiotool.com/user/mrstandfast/"),
    ("https://www.audiotool.com/album/cvguob117/", "https://www.audiotool.com/user/kahliel/"),
    ("https://www.audiotool.com/album/ttfrr/", "https://www.audiotool.com/user/dabrig/"),
    ("https://www.audiotool.com/album/xmilsqmwn/", "https://www.audiotool.com/user/bart_van_eynde/"),
    ("https://www.audiotool.com/album/2sem3/", "https://www.audiotool.com/user/jakeleavey_ymail_com/"),
    ("https://www.audiotool.com/album/jkuptea/", "https://www.audiotool.com/user/apolloeuphoria/"),
    ("https://www.audiotool.com/album/ftnagxh/", "https://www.audiotool.com/user/flooroneooneremixes/"),
    ("https://www.audiotool.com/album/rjggctqy/", "https://www.audiotool.com/user/erdbeerquark/"),
    ("https://www.audiotool.com/album/7a9ktldnm/", "https://www.audiotool.com/user/floydpjasper/"),
    ("https://www.audiotool.com/album/3i0j5p/", "https://www.audiotool.com/user/brainwalker/"),
    ("https://www.audiotool.com/album/mhksqxj/", "https://www.audiotool.com/user/zerod/"),
    ("https://www.audiotool.com/album/rs5yxjze/", "https://www.audiotool.com/user/sandburgen/"),
    ("https://www.audiotool.com/album/w3ob3/", "https://www.audiotool.com/user/kepz/"),
    ("https://www.audiotool.com/album/naaejqfyw/", "https://www.audiotool.com/user/sharkyyo/"),
    ("https://www.audiotool.com/album/develp/", "https://www.audiotool.com/user/mygrandpascool/"),
    ("https://www.audiotool.com/album/tzvj27b/", "DELETED"),
    ("https://www.audiotool.com/album/gw9cqiqr/", "https://www.audiotool.com/user/dublion/"),
    ("https://www.audiotool.com/album/xdi9i0mh/", "https://www.audiotool.com/user/notoz/"),
    ("https://www.audiotool.com/album/pohsz7b/", "https://www.audiotool.com/user/oscarollie/"),
    ("https://www.audiotool.com/album/qbemlckoi/", "https://www.audiotool.com/user/sumad/"),
    ("https://www.audiotool.com/album/ubguzjkis/", "https://www.audiotool.com/user/callycus/"),
    ("https://www.audiotool.com/album/knl9rxjg/", "https://www.audiotool.com/user/granpaw/"),
    ("https://www.audiotool.com/album/bwjaynh12/", "https://www.audiotool.com/user/christian-chrom/"),
    ("https://www.audiotool.com/album/mzcfu/", "https://www.audiotool.com/user/audioarchitect/"),
    ("https://www.audiotool.com/album/pjpiou3l/", "https://www.audiotool.com/user/statistik/"),
    ("https://www.audiotool.com/album/zxigd/", "https://www.audiotool.com/user/john_cavanaugh/"),
    ("https://www.audiotool.com/album/dvf4umd/", "https://www.audiotool.com/user/beatbob/"),
    ("https://www.audiotool.com/album/mogada75n/", "https://www.audiotool.com/user/arche289/"),
    ("https://www.audiotool.com/album/p1yi4n/", "https://www.audiotool.com/user/exist/"),
    ("https://www.audiotool.com/album/x8x8lg2tm/", "https://www.audiotool.com/user/almate/"),
    ("https://www.audiotool.com/album/pevrv/", "https://www.audiotool.com/user/spacehorse/"),
    ("https://www.audiotool.com/album/uq8tpudy/", "DELETED"),
    ("https://www.audiotool.com/album/mjv7t0sad/", "https://www.audiotool.com/user/bit-tron/"),
    ("https://www.audiotool.com/album/9pfmz/", "https://www.audiotool.com/user/hangoo/"),
    ("https://www.audiotool.com/album/rwhjt2i/", "https://www.audiotool.com/user/superneonsonvegasairwaves/"),
    ("https://www.audiotool.com/album/jtpwkjj/", "https://www.audiotool.com/user/twerk/"),
    ("https://www.audiotool.com/album/wmnofedc/", "https://www.audiotool.com/user/clu/"),
    ("https://www.audiotool.com/album/n2xjvl/", "https://www.audiotool.com/user/herlufsew/"),
    ("https://www.audiotool.com/album/0i3ls/", "https://www.audiotool.com/user/virtuousduck/"),
    ("https://www.audiotool.com/album/fynka1b/", "https://www.audiotool.com/user/carlyon/"),
    ("https://www.audiotool.com/album/xe89crjwc/", "https://www.audiotool.com/user/iwanbeflylo23/"),
    ("https://www.audiotool.com/album/dq1pabol/", "https://www.audiotool.com/user/djflashbang/"),
    ("https://www.audiotool.com/album/qafr9/", "https://www.audiotool.com/user/rodrigo_del_canto/"),
    ("https://www.audiotool.com/album/djnov/", "https://www.audiotool.com/user/mark-lewis_ndikintum/"),
    ("https://www.audiotool.com/album/f1ailrc/", "https://www.audiotool.com/user/flowerrr/"),
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

def fetch_url(url, headers=None):
    req = urllib.request.Request(url, headers=headers or HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode('utf-8', errors='replace')

def fetch_user_avatar(user_key):
    # Direct avatar URL - no need to parse XML
    return f'https://api.audiotool.com/user/{user_key}/avatar/512.jpg'

def fetch_album(album_url, user_url=''):
    html = fetch_url(album_url)

    # Extract artist name from title "Edition Audiotool: {Artist}"
    artist_name = ''
    title_match = re.search(r'Edition Audiotool:\s*([^<"]+)', html)
    if title_match:
        artist_name = title_match.group(1).strip()

    # Extract album cover image (artist portrait) - og:image or first album cover
    photo = ''
    og_image = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', html)
    if og_image:
        photo = og_image.group(1)
    if not photo:
        # Try cover image from CDN
        cover_match = re.search(r'(https://at-cdn[^"]+cover[^"]+\.(?:jpg|png|jpeg))', html)
        if cover_match:
            photo = cover_match.group(1)

    # Extract date from album HTML
    date = ''
    date_match = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})', html)
    if not date_match:
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', html)
    if date_match:
        date = date_match.group(1)

    # Extract track IDs from data-track-key attributes
    track_ids = list(dict.fromkeys(re.findall(r'data-track-key="([a-zA-Z0-9_-]+)"', html)))
    track_ids = [t for t in track_ids if len(t) > 3][:11]

    if not track_ids:
        raise Exception('No track IDs found in HTML')

    # Extract track names and artists from HTML
    # Pattern: track link and author link side by side
    tracks = []
    track_rows = re.findall(
        r'href="/track/([a-zA-Z0-9_-]+)/"[^>]*class="[^"]*_track-name[^"]*"[^>]*>([^<]+)</a>.*?href="/user/([a-zA-Z0-9_-]+)/"',
        html, re.DOTALL
    )

    # Get track names from title attributes or link text
    track_names = re.findall(r'href="/track/[a-zA-Z0-9_-]+/"[^>]*>([^<]+)</a>', html)
    track_artists = re.findall(r'class="[^"]*_author-name[^"]*"[^>]*>([^<]+)</a>', html)
    track_user_keys = re.findall(r'href="/user/([a-zA-Z0-9_-]+)/"', html)

    for idx, tid in enumerate(track_ids):
        name = track_names[idx] if idx < len(track_names) else tid
        track_artist = track_artists[idx] if idx < len(track_artists) else ''
        tracks.append({
            'url': f'https://www.audiotool.com/track/{tid}/',
            'name': name.strip(),
            'track_artist': track_artist.strip(),
            'desc': '',
        })

    if not tracks:
        raise Exception('No tracks parsed from HTML')

    # Get at_profile and cover from user_url if provided, else from last track
    at_profile = user_url if user_url else ''
    cover_url = ''
    if at_profile:
        m = re.search(r'/user/([^/]+)/?$', at_profile)
        if m:
            cover_url = fetch_user_avatar(m.group(1))
    elif track_user_keys:
        last_user_key = track_user_keys[-1]
        at_profile = f'https://www.audiotool.com/user/{last_user_key}/'
        cover_url = fetch_user_avatar(last_user_key)

    return artist_name, at_profile, date, photo, cover_url, tracks

# Load existing
existing = []
try:
    with open('gen1_data.json', encoding='utf-8') as f:
        existing = json.load(f)
    print(f'Loaded {len(existing)} existing entries')
except:
    print('Starting fresh')

existing_by_url = {a.get('album_url', '').rstrip('/'): a for a in existing}
results = []
failed = []

for i, entry in enumerate(albums):
    album_url, user_url = entry if isinstance(entry, tuple) else (entry, '')
    clean_url = album_url.rstrip('/')
    existing_entry = existing_by_url.get(clean_url)

    print(f'[{i+1}/{len(albums)}] {album_url}', end=' ', flush=True)

    # Handle deleted artists
    if user_url == 'DELETED':
        if existing_entry:
            existing_entry['is_hidden'] = True
            results.append(existing_entry)
        else:
            results.append({'album_url': album_url, 'is_hidden': True, 'artist': '', 'tracks': []})
        print('HIDDEN')
        continue

    try:
        artist_name, at_profile, date, photo, cover_url, tracks = fetch_album(album_url, user_url)

        if existing_entry:
            existing_entry['artist'] = artist_name
            existing_entry['tracks'] = tracks
            if not existing_entry.get('at_profile') and at_profile:
                existing_entry['at_profile'] = at_profile
            if not existing_entry.get('photo') and photo:
                existing_entry['photo'] = photo
            if cover_url and user_url:
                existing_entry['cover_url'] = cover_url  # Always update if we have explicit user_url
            elif not existing_entry.get('cover_url') and cover_url:
                existing_entry['cover_url'] = cover_url
            if not existing_entry.get('date') and date:
                existing_entry['date'] = date
            results.append(existing_entry)
            print(f'UPDATED - {artist_name} ({len(tracks)} tracks) photo={bool(photo)} cover={bool(cover_url)} date={date}')
        else:
            entry = {
                'artist': artist_name,
                'real_name': '',
                'date': date,
                'album_number': len(results) + 1,
                'at_profile': at_profile,
                'album_url': album_url,
                'photo': photo,
                'cover_url': cover_url,
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
            print(f'NEW - {artist_name} ({len(tracks)} tracks) photo={bool(photo)} cover={bool(cover_url)} date={date}')

    except Exception as e:
        print(f'FAILED - {e}')
        if existing_entry:
            results.append(existing_entry)
        failed.append(album_url)

    time.sleep(0.5)

with open('gen1_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f'\nDone. {len(results)} artists saved.')
if failed:
    print(f'\nFailed ({len(failed)}):')
    for u in failed:
        print(f'  {u}')