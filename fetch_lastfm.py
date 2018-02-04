import zipfile

import numpy as np
import scipy.sparse as sp

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

def _get_dimensions(artists, users):

    uids = set()
    aids = set()

    for uid, _, _ in users:
        uids.add(uid)

    for aid, _, _, _ in artists:
        aids.add(aid)

    rows = max(uids) + 1
    cols = max(aids) + 1

    return rows, cols

def fetch_lastfm():
    """
    Fetch the 'hetrec 2011 lastfm 2k data set <https://grouplens.org/datasets/hetrec-2011/>' 
    """

    zip_path = './hetrec2011-lastfm-2k.zip'

    (raw_artists, raw_users) = _read_raw_data(zip_path)

    rows, cols = _get_dimensions(_parse_artists(raw_artists), 
                                _parse_users(raw_users))

    testSize = int(rows * 0.2)
    trainSize = rows - testSize

    artist_map = np.empty(cols, dtype=np.object)
    for aid, name, _, _ in _parse_artists(raw_artists):
        artist_map[aid] = name

    train_mat = sp.lil_matrix((trainSize, cols), dtype=np.int32)
    test_mat = sp.lil_matrix((testSize, cols), dtype=np.int32)
    for (uid, aid, weight) in _parse_users(raw_users):
        if uid < trainSize:
            train_mat[uid, aid] = weight
        else:
            test_mat[uid - trainSize, aid] = weight

    
    data = {
        'train' : train_mat.tocoo(),
        'test' : test_mat.tocoo(),
        'item_labels' : artist_map,
    }
    return data
