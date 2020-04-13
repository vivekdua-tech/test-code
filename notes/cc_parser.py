'Parse the CC file and store the data in dict'

import collections
import glob
import re
from pprint import pprint
from operator import itemgetter
import pdb
from myplot import plotFromList

#visited = collections.Counter()
#for filename in glob.glob('notes/*.log'):
#    with open(filename) as f:
#        for line in f:
#            mo = re.search(r'GET\s+(\S+)\s+200', line)
#            if mo is not None:
#                url = mo.group(1)
#                visited[url] += 1
#pprint.pprint(visited.most_common(20))

XrCcStore={}
NxCcStore={}
XeCcStore={}

def ccstore(name):
    if name == 'xr':
        return XrCcStore
    if name == 'nx':
        return NxCcStore
    if name == 'xe':
        return XeCcStore
    else:
        return None

def parse_and_store(name):
    if name == 'xr':
        ccfile = 'xr-code-complexity'
    if name == 'nx':
        ccfile = 'nx-code-complexity'
    if name == 'xe':
        ccfile = 'xe-code-complexity'
        
    for filename in glob.glob(ccfile):
        with open(filename) as f:
            for line in f:
                #pdb.set_trace()
                p = re.compile(r':\d+:')
                line = p.sub(' ',line)
                p = re.compile(r'warning:|has|NLOC|CCN|token|PARAM|length|\n')
                line = p.sub('', line)
                print
                # Get the module instead of file-name 
                p = re.compile(r'^[\w,-]+\/[\w,-]+')
                if not p.search(line):
                    pdb.set_trace()
                modulename = p.search(line).group(0) 
                p = re.compile(r'^\S+')
                line = p.sub(modulename, line)
                p = re.compile(r'\s+ | ,')
                matchList = p.split(line)
                #matchList is [mod-name, api-name, nloc, ccn, token, param, length]
                # CC store: {mod-name : [(mod-name, api-name, nloc, ccn, token, param...)]}
                matchTuple = (modulename,
                              matchList[1], #api-name
                              int(matchList[2]), #nloc
                              int(matchList[3]), #ccn
                              int(matchList[4]), #token
                              int(matchList[5]), #param
                              int(matchList[6]))
                if matchList[0] in ccstore(name):
                    ccstore(name)[matchList[0]] += [matchTuple]
                else:
                    ccstore(name)[matchList[0]] = [matchTuple]
               

def LookupTopForModule(name, modname, num):
    store = ccstore(name)[modname]
    sortedStore = sorted(store, key=itemgetter(3), reverse=True)
    return [sortedStore[x] for x in range(min(num + 1, len(sortedStore)))] 

def LookupTopAcrossAllModule(name, num):
    AggList=[]
    for modname in ccstore(name):
        AggList += LookupTopForModule(name, modname, num)
    sortedAggList = sorted(AggList, key=itemgetter(3), reverse=True)
    return [sortedAggList[x] for x in range(min(num + 1, len(sortedAggList)))]

def ListAllModule(name):
    for modname in ccstore(name):
        print(modname)

def PrintEntries(lst):
    print('ModuleName                     ApiName                       Token            CCN')
    print('==================================================================================')
    for tpl in lst:
        #tpl is the tuple
        print('{:30s} {:30s} {:10d} {:10d}'.format(tpl[0],tpl[1],tpl[4],tpl[3]))


def MostUnhygienic(name, num, modname=None, pattern=None):
    pprint('ModuleName                    Pattern                    Num-of-Unhygienic-Api')
    pprint('==========================================================================')
    retList=[]
    if pattern == None:
        if modname == None:
            Unglist=[(x, len(ccstore(name)[x])) for x in ccstore(name)]
            sortedList=sorted(Unglist, key=itemgetter(1), reverse=True)
            for i in range(min(len(sortedList), num + 1)):
                pprint('{:30s} {:30s} {:10d}'.format(sortedList[i][0], 'None', sortedList[i][1]))
                retList += [(sortedList[i][0], sortedList[i][1])]
                
        else:
            #modname is available - Just print the num of Ung APIs
            count = len(ccstore(name)[modname])
            pprint('{:30s} {:30s} {:10d}'.format(modname, 'None', count))
            retList += [(modname, count)]
    else:
        UngDict={}
        if modname == None:
            for x in ccstore(name):
                if pattern in x:
                    UngDict[x] = len(ccstore(name)[x])
            sortedDict=sorted(UngDict.items(), key=itemgetter(1), reverse=True)
            for se in sortedDict:
                pprint('{:30s} {:30s} {:10d}'.format(se[0], pattern, se[1]))
                retList += [(se[0], se[1])]
        else:
            #modname and pattern both are available
            count = 0
            for x in ccstore(name)[modname]:
                #search for pattern in the api-name
                if pattern in x[1]:
                    count += 1
            pprint('{:30s} {:30s} {:10d}'.format(modname, pattern, count))
            retList += [(modname, count)]
    return retList
        
        
if __name__=='__main__':
    parse_and_store('xr')    
    #ListAllModule()
    PrintEntries(LookupTopAcrossAllModule('xr', 20))
    PrintEntries(LookupTopForModule('xr', 'ipv4/multicast', 20))
    PrintEntries(LookupTopForModule('xr', 'ipv4/bgp', 20))
    

    parse_and_store('nx')    
    ListAllModule('nx')
    PrintEntries(LookupTopAcrossAllModule('nx', 20))
    #PrintEntries(LookupTopForModule('nx', 'ipv4/multicast', 20))
    #PrintEntries(LookupTopForModule('nx', 'ipv4/bgp', 20))
    l = MostUnhygienic('nx', 20)
    plotFromList(l).show()
    l = MostUnhygienic('xr', 20)
    plotFromList(l).show()
    l = MostUnhygienic('nx', 20, None, 'routing')
    plotFromList(l).show()
    #plot the mcast UNG bar graph
    mcastlst = [('pim',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'pim')[0][1])]
    mcastlst += [('mrib',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'mrib')[0][1])]
    mcastlst += [('mfwd',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'mfwd')[0][1])]
    mcastlst += [('igmp',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'igmp')[0][1])]
    mcastlst += [('lib',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'lib')[0][1])]
    mcastlst += [('autorp',
                 MostUnhygienic('xr', 270, 'ipv4/multicast', 'autorp')[0][1])]
    plotFromList(mcastlst).show()
    
    
        
