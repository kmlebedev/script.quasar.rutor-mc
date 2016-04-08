# coding: utf-8
__author__ = 'mancuniancol'

import common
from bs4 import BeautifulSoup
from quasar import provider

# this read the settings
settings = common.Settings()
# define the browser
browser = common.Browser()
# create the filters
filters = common.Filtering()


def extract_torrents(data):
    filters.information()  # print filters settings
    sint = common.ignore_exception(ValueError)(int)
    results = []
    cont = 0
    if data is not None:
        soup = BeautifulSoup(data, 'html5lib')
        links = soup.findAll('table')
        if len(links) > 3:
            links = links[2].tbody.findAll('tr')
            for link in links:
                columns = link.findAll('td')
                if len(columns) == 5:
                    name = columns[1].text.strip()  # name
                    magnet = columns[1].select('a + a')[0]['href']  # torrent
                    size = columns[3].text.strip()  # size
                    temp = columns[4].text.split()
                    seeds = temp[0]  # seeds
                    peers = temp[1]  # peers
                    # info_magnet = common.Magnet(magnet)
                    if filters.verify(filters.title, size):
                        cont += 1
                        # magnet = common.getlinks(magnet)
                        results.append({"name": name,
                                        "uri": magnet,
                                        # "info_hash": info_magnet.hash,
                                        "size": size,
                                        "seeds": sint(seeds),
                                        "peers": sint(peers),
                                        "language": settings.value.get("language", "en"),
                                        "provider": settings.name
                                        })  # return the torrent
                        if cont >= int(settings.value.get("max_magnets", 10)):  # limit magnets
                            break
                    else:
                        provider.log.warning(filters.reason)
    provider.log.info('>>>>>>' + str(cont) + ' torrents sent to Quasar<<<<<<<')
    return results


def search(query):
    info = {"query": query,
            "type": "general"}
    return search_general(info)


def search_general(info):
    info["extra"] = settings.value.get("extra", "")  # add the extra information
    query = filters.type_filtering(info, '%20')  # check type filter and set-up filters.title
    url_search = "%s/search/%s" % (settings.value["url_address"], query)
    provider.log.info(url_search)
    browser.open(url_search)
    return extract_torrents(browser.content)


def search_movie(info):
    info["type"] = "movie"
    query = common.translator(info['imdb_id'], 'ru', False)  # Just title
    info["query"] = query
    return search_general(info)


def search_episode(info):
    if info['absolute_number'] == 0:
        info["type"] = "show"
        info["query"] = info['title'].encode('utf-8') + ' s%02de%02d' % (
            info['season'], info['episode'])  # define query
    else:
        info["type"] = "anime"
        info["query"] = info['title'].encode('utf-8') + ' %02d' % info['absolute_number']  # define query anime
    return search_general(info)


def search_season(info):
    info["type"] = "show"
    info["query"] = info['title'].encode('utf-8') + ' %s %s' % (
        common.season_names["ru"], info['season'])  # define query
    return search_general(info)


# This registers your module for use
if "false" == settings.value.get("episodes", "false"):
    provider.register(search, search_movie, search_episode, search_season)
else:
    provider.register(search, search_movie, search_season, search_season)

del settings
del browser
del filters
