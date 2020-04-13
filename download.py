#! /usr/bin/env python3.4
'Download all the class files to a local directory'

import os, urllib.request, urllib.error, urllib.parse, re, dbm.dumb, time, gzip, io, threading, sys
from collections import namedtuple
from multiprocessing.pool import ThreadPool as Pool
import ssl

no_cert = ssl.SSLContext()      # context without certificate checking

host = 'http://[2001:420:291:1258:2811:f429:13f6:8215]:8080'
host = 'http://127.0.0.1:8080'
host = 'http://10.155.73.99:8080'
shared_dir = '/shared'
class_dir = '/sj195'
dest_dir = 'notes'

Response = namedtuple('Response', ['code', 'msg', 'compressed', 'written'])

def urlretrieve(url, filename, cache={}, lock=threading.Lock()):
    'Read contents of an open url, use etags and decompress if needed'    

    request = urllib.request.Request(url)
    request.add_header('User-Agent', "Raymond's Downloader")
    request.add_header('Accept-Encoding', 'gzip')
    with lock:
        if ('etag ' + url) in cache:
            request.add_header('If-None-Match', cache['etag ' + url])
        if ('mod ' + url) in cache:
            request.add_header('If-Modified-Since', cache['mod ' + url])

    try:
        u = urllib.request.urlopen(request, context=no_cert)
    except urllib.error.HTTPError as e:
        return Response(e.code, e.msg, False, False)
    content = u.read()
    u.close()

    compressed = u.getheader('Content-Encoding') == 'gzip'
    if compressed:                                       
        content = gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb').read()

    written = writefile(filename, content) 

    with lock:
        etag = u.getheader('Etag')
        if etag:
            cache['etag ' + url] = etag
        timestamp = u.getheader('Last-Modified')
        if timestamp:
            cache['mod ' + url] = timestamp

    return Response(u.code, u.msg, compressed, written)

def writefile(filename, content):
    "Only write content if it is not already written."
    try:
        with open(filename, 'rb') as f:
            curr_content = f.read()
            if curr_content == content:
                return False
    except IOError:
        pass
    with open(filename, 'wb') as f:
        f.write(content)
    return True

def download(target, dest_dir=dest_dir):
    'Retrieve a target url and return the download status as a string'
    filename = target.rsplit('/', 1)[-1]
    fullname = os.path.join(dest_dir, filename)
    
    if target.startswith('$'):
        path = shared_dir
    elif target.startswith('~'):
        path = class_dir
    elif target.startswith('!'):
        path = ''
    target = host + path + target[1:]

    r = urlretrieve(target, fullname, etags)

    if r.code != 200:
        if r.code != 404:
            return '%3d  %-16s %s' % (r.code, r.msg, target)
        return '\033[0;31m%3d\033[0m  %-16s %s' % (r.code, r.msg, target)
    compressed = '*' if r.compressed else ' '
    written = '(updated)' if r.written else '(current)'
    return '%3d%1s %-16s %-55s --> %-25s %s ' % \
           (r.code, compressed, r.msg, target, fullname, written)

if __name__ == '__main__':
    try:
        os.mkdir(dest_dir)
    except OSError:
        pass

    links_url = host + class_dir + '/links.txt'
    print((' Source: %s ' % links_url).center(117, '='))
    print((' Starting download at %s ' % time.ctime()).center(117))

    etags = dbm.dumb.open(os.path.join(dest_dir, 'etag_db'))
    links_text = urllib.request.urlopen(links_url, context=no_cert).read().decode('utf-8')
    targets = re.findall(r'^[~$!]/.+', links_text, re.M)
    mapper = Pool(25).imap_unordered
    #mapper = map
    for line in mapper(download, targets):
        print(line)
    etags.close()
