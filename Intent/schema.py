#! /usr/bin/env python3.4

import os
import pdb

"""
   Schema class: Graph mode

   [] : nodes
   -> : relationship

    [system]--hosted_interfaces-->[interface]
    [system]--hosted_endpoints--->[virtual_endpoints]
    [virtual-network]--member_endpoints-->[virtual_endpoints]
    [system]--hosted_application-->[application]
    [interface]--pim_config-->[pim_interface]<--pim_adjacency-->[pim_interface]
   
"""
class node:

    def __init__(self, identity, Dict, relations):
        """
           constructor method
        """
        self.identity = identity
        self.nodeDict = Dict #Dict
        self.relationships = relations #Dict
        
    def dumpNode(self):
        if 'system' in self.identity.split(':')[0]:
            str = 'System:'
        if 'intf' in self.identity.split(':')[0]:
            str = 'Interface:'
        if 'pimIntf' in self.identity.split(':')[0]:
            str = 'Pim-Interface:'
        if 'Intent' in self.identity.split(':')[0]:
            str = 'Intent:'
        str += self.identity.split(':')[1]
        return str
    def dumpRelationship(self):
        
        for rel_type in self.relationships:
            if self.relationships[rel_type]['source'] == self.identity:
                return '<==>'
            if self.relationships[rel_type]['target'] == self.identity:
                return '<==>'
            
    def getTargetId(self):

        for rel_type in self.relationships:
            if self.relationships[rel_type]['source'] == self.identity:
                return self.relationships[rel_type]['target']
        return None

    def getSourceId(self):

        for rel_type in self.relationships:
            if self.relationships[rel_type]['target'] == self.identity:
                return self.relationships[rel_type]['source']
        return None

class intent:
    """
        Intent applied to a set of nodes(interface or systems).
        For Pim-adjacency telemetry sensor, it installs
        PIM adjacency sensor which senses adjacency every X hrs,
        Intent is applied to set of nodes, hence nodeDict is required.
    """
    def __init__(self, identity, nodeList):
        self.identity = identity
        self.nodeList = nodeList
        

class Schema:
    """
    class shark
    """
    nodes = {}
    intents = {}
    systems = []
    
    def __init__(self):
        """
           constructor method
        """
    def addNode(self, nodeIdentifier, nodeDict):
        """
            nodeType: 'system'
            nodeIdentifier: 'unique system id'
            node: system attributes in key-value pair.
        """
        self.nodes[nodeIdentifier] = node(nodeIdentifier, nodeDict, {})

    def lookupNode(self, nodeIdentifier):
        
        return self.nodes[nodeIdentifier]

    def drawGraph(self):
        
        for sys in self.systems:
            str = ''
            visited_nodes = {}
            visited_nodes[sys.identity] = 1
            str += '|' + sys.dumpNode() + '|'
            next = self.lookupNode(sys.getTargetId())
            prev = sys
            while  next != None and next.identity not in visited_nodes:
                visited_nodes[next.identity] = 1
                str += prev.dumpRelationship()
                str += '|' + next.dumpNode() + '|'
                prev = next
                if next.getTargetId():
                    next = self.lookupNode(next.getTargetId())
                else:
                    next = None
            if prev.getSourceId() and prev.getSourceId() not in visited_nodes:
                str += prev.dumpRelationship()
                srcNode = self.lookupNode(prev.getSourceId())
                str += srcNode.dumpNode()
            # get the intents
            for intent in self.intents:
                if sys.identity.split(':')[1] in intent:
                    str += '<==>'
                    str += self.intents[intent].dumpNode()
            print(str)
 
    def createSystem(self, label, system_type, role,
                         hostname, system_id, deploy_mode,
                         position):
        """
           {'label' : <>, 'system_type': <>, 'role': <>
            'hostname': <>, 'system_id': <>, 'deploy_mode': <>
            'position': <>}
        """
        identity = 'system:%s:%s' %(label, system_type)
        nodeDict = { 'label': label,
                 'system_type': system_type,
                 'role': role,
                 'hostname' : hostname,
                 'system_id' : system_id,
                 'deploy_mode' : deploy_mode,
                 'position' : position }
        self.addNode(identity, nodeDict)
        self.systems += [self.lookupNode(identity)]
        return identity

    def createInterface(self, label, if_type, mode, protocols):
        """
           'label': <>
           'iftype': <>
           'mode': <>
           'protocols':<>
        """
        identity =  'intf:%s:%s' %(label, if_type)
        nodeDict = { 'iftype' : if_type, 'mode' : mode, 'protocols' : protocols }
        self.addNode(identity, nodeDict)
        return identity

    def createPimInterface(self, label, v4, protocols):
        """
           'label': <>
           'v4': <>
           'protocols':<>
        """
        identity =  'pimIntf:%s:%s' %(label, v4)
        nodeDict = { 'label' : label, 'v4' : v4, 'protocols' : protocols }
        self.addNode(identity, nodeDict)
        return identity

    def createRelationship(self, source, rel_type, direction, target):
        """{
           'source': <>
           'type': <>
           'target': <>
           }
        """
        relationship = { 'source' : source.identity,
                         'rel_type' : rel_type,
                         'dir' : direction,
                         'target' : target.identity
                        }
        
        source.relationships[rel_type] = relationship
        target.relationships[rel_type] = relationship

    def getProtoConfig(self, targetId):
        """
            From the intent_type, get the config_type
        """
        if 'pim' in targetId:
            return 'pim_config'

    def lookupIntent(self, intent_type, interface, systemId):
        """
            Lookup intents with the identity:
                'Intent:<interface>:<systemId>'
        """
        identity = 'Intent:%s:%s:%s' %(intent_type, interface, systemId)
        return self.intents[identity]

    def deployIntent(self, intent_type, targetId):
        """
            create a intent node with 'intent_type' relationship to the target
        """
        ## id: 'Intent:<intent_type>:<interface>:<system>'
        ## targetId: 'pimIntf:label'
        interface = targetId.split(':')[1]
        ## get the system identity from the relationships
        interfaceId = self.lookupNode(targetId).relationships[self.getProtoConfig(targetId)]['source']
        intfNode = self.lookupNode(interfaceId)
        systemId = intfNode.relationships['hosted_intf']['source'].split(':')[1]
        identity = 'Intent:%s:%s:%s' %(intent_type, interface, systemId)
        nodeDict = { 'label' : identity,
                     'type' : intent_type,
                     'interface' : interface,
                     'system': systemId
                    }
        self.addNode(identity, nodeDict)
        node = self.lookupNode(identity)
        self.createRelationship(node, intent_type, 1, self.lookupNode(targetId))
        self.intents[identity]=node

if __name__ == '__main__':

    # Create Source-PE Intent Graph
    sch = Schema()
    sysId = sch.createSystem('PE1', 'asr9k', 'src-pe', 'asr9k-24', 1, 1, 1)
    intfId = sch.createInterface('ge-0/0', '10g', 'full', None)
    sys1 = sch.lookupNode(sysId)
    intf1 = sch.lookupNode(intfId)
    # System-->Interface relationsip
    sch.createRelationship(sys1, 'hosted_intf', 1, intf1)
    # Create PIM interface
    pimIntfId1 = sch.createPimInterface('ge-0/0', '10.10.10.1', 'PIM')
    # Interface--->PIM_interface
    sch.createRelationship(intf1, 'pim_config', 1, sch.lookupNode(pimIntfId1))
    sch.deployIntent('SENSOR_PIM_ADJACENCY', pimIntfId1)
    
    #Create Destination-PE Intent Graph
    sysId = sch.createSystem('PE2', 'asr9k', 'dst-pe', 'asr9k-24', 1, 1, 1)
    intfId = sch.createInterface('ge-0/0', '10g', 'full', None)
    sys1 = sch.lookupNode(sysId)
    intf1 = sch.lookupNode(intfId)
    # System-->Interface relationsip
    sch.createRelationship(sys1, 'hosted_intf', 1, intf1)
    # Create PIM interface
    pimIntfId2 = sch.createPimInterface('ge-0/0', '10.10.10.2', 'PIM')
    # Interface--->PIM_interface
    sch.createRelationship(intf1, 'pim_config', 1, sch.lookupNode(pimIntfId2))
    # Install PIM-ADJACENCY Sensor
    sch.deployIntent('SENSOR_PIM_ADJACENCY', pimIntfId2)
    assert(sch.lookupIntent('SENSOR_PIM_ADJACENCY', 'ge-0/0', 'PE1'))
    assert(sch.lookupIntent('SENSOR_PIM_ADJACENCY', 'ge-0/0', 'PE2'))
    sch.drawGraph()
            
