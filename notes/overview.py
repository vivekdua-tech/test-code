'Scan a log file from a NASA server'

# Demonstration of how Python works

import collections
import glob
import re
import pprint
import pdb


visited = collections.Counter()
for filename in glob.glob('/Users/vidua/pyclass/notes/nasa1.log'):
    try:
        with open(filename) as f:
            for line in f:
                #pdb.set_trace()
                mo = re.search(r'GET\s+(\S+)\s+200', line)
                if mo is not None:
                    url = mo.group(1)
                    visited[url] += 1
    except (OSError, FileNotFoundError, IOError) as e:
        pdb.set_trace()
        print("Exception:%d" % e.errno)

pprint.pprint(visited.most_common(20))

