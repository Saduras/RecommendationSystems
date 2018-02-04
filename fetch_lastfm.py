import zipfile
from lightfm.datasets import _common

def _read_raw_data(path):
    with zipfile.ZipFile(path) as datafile:
        return (datafile.read('artists.dat').decode().split('\n'),
                datafile.read('user_artists.dat').decode().split('\n'))

def _parse_artists(raw_artists):
    
    # remove header line
    raw_artists = raw_artists[1:]

    for line in raw_artists:

        if not line: 
            continue

        raw_aid, name, url, pictureURL = [str(x) for x in line.split('\t')]
        aid = int(raw_aid)
        yield aid, name, url, pictureURL

def _parse_users(raw_users):

    # remove header line
    raw_users = raw_users[1:]

    for line in raw_users:

        if not line:
            continue

        uid, aid, weight = [int(x) for x in line.split('\t')]
        yield uid, aid, weight

def fetch_lastfm():
    """
    Fetch the 'hetrec 2011 lastfm 2k data set <https://grouplens.org/datasets/hetrec-2011/>' 
    """

    zip_path = './hetrec2011-lastfm-2k.zip'

    (raw_artists, raw_users) = _read_raw_data(zip_path)

    artists = _parse_artists(raw_artists)
    users = _parse_users(raw_users)

    
    # print(users)
    # for user in users:
    #     user['artistID'] = artists


fetch_lastfm()
