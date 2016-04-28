# coding: utf-8
from quasar.provider import *

__author__ = 'mancuniancol'


def extract_torrents(html=None):
    if html is not None:
        dom = ParseHtml().feed(html)
        tables = ParseHtml.find_all(dom, 'table')
        if len(tables) > 3:
            for elem in tables[2].find('tr'):
                columns = ParseHtml.find_all(elem, 'td')
                if len(columns) == 5:
                    print columns[1]
                    name = ParseHtml.select(html=columns[1])  # name
                    magnet = ParseHtml.select(html=columns[1], tag='a', order=2, element='href')  # magnet
                    size = ParseHtml.select(html=columns[3])  # size
                    seeds = ParseHtml.select(html=columns[4], tag='span')  # seeds
                    peers = ParseHtml.select(html=columns[4], tag='span', order=2)  # peers
                    yield (name, magnet, size, seeds, peers)


def search(title):
    Filtering.type = "general"
    url = "%s/search/%s" % (Settings["url_address"], title)
    Filtering.add(title=title, url=url)
    return process(separator="%20", generator=extract_torrents)


def search_movie(info):
    Filtering.type = "movie"
    # title in russian
    title = translator(info['imdb_id'], 'ru', False)  # Just title
    url = "%s/search/%s" % (Settings["url_address"], title)
    Filtering.add(title=title, url=url)
    # title in english
    title = info["title"]  # Just title
    url = "%s/search/%s" % (Settings["url_address"], title)
    Filtering.add(title=title, url=url)

    return process(separator="%20", generator=extract_torrents)


def search_episode(info):
    if info['absolute_number'] == 0:
        Filtering.type = "show"
        # S00E00 format
        title = info['title'].encode('utf-8') + ' s%02de%02d' % (info['season'], info['episode'])
        url = "%s/search/%s" % (Settings["url_address"], title)
        Filtering.add(title=title, url=url)
        # [S00] format
        title = info['title'].encode('utf-8') + ' [S%02d]' % info['season']
        url = "%s/search/%s" % (Settings["url_address"], title)
        Filtering.add(title=title, url=url)
    else:
        info["type"] = "anime"
        title = info['title'].encode('utf-8') + ' %02d' % info['absolute_number']
        url = "%s/search/%s" % (Settings["url_address"], title)
        Filtering.add(title=title, url=url)
    return process(separator="%20", generator=extract_torrents)


def search_season(info):
    Filtering.type = "show"
    title = info['title'].encode('utf-8') + ' [S%02d]' % info['season']
    url = "%s/search/%s" % (Settings["url_address"], title)
    Filtering.add(title=title, url=url)
    return process(separator="%20", generator=extract_torrents)


# This registers your module for use
register(search, search_movie, search_episode, search_season)
