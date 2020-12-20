# coding=utf-8
import vk

session = \
    vk.Session(access_token='TOKEN')
vk_api = vk.API(session)


def get_photos():
    n = 0
    c = 0
    count = 1
    p_ids = []
    while c <= count:
        photos = vk_api.photos.get(album_id='saved', rev=0, v=5.92, count=1000, offset=c)
        count = photos['count']
        n = n + 1
        c = n * 1000
        for photo in photos['items']:
            p_ids.append(photo['id'])
    print(len(p_ids))
    return p_ids


def choose_photos(start, end):
    x = get_photos()[start:end]
    print(x)
    return x


def photo_del(ids):
    for p_id in ids:
        vk_api.photos.delete(photo_id=p_id, v=5.92)

