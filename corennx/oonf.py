#
# CORE
# Copyright (c)2010-2012 the Boeing Company.
# See the LICENSE file included in this distribution.
#
''' Sample user-defined service.
'''

import os

from core.service import CoreService, addservice
from core.misc.ipaddr import IPv4Prefix, IPv6Prefix

class MyServiceOONF(CoreService):
    ''' This is a sample user-defined service. 
    '''
    # a unique name is required, without spaces
    _name = "OONF"
    # you can create your own group here
    _group = "Ninux"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ('/etc/olsrd2',)
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ('etc/olsrd2/olsrd2.conf', )
    # this controls the starting order vs other enabled services
    _startindex = 50
    # list of startup commands, also may be generated during startup
    _startup = ('/usr/sbin/olsrd2_static --load=/etc/olsrd2/olsrd2.conf',)
    # list of shutdown commands
    _shutdown = ()

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
        cfg = "#Autogenerate file\n"
        cfg += "[domain=0]\n\ttable 111\n"
        cfg += "[domain=1]\n\ttable 112\n"
        cfg += "[domain=150]\n\ttable 150\n"
        cfg += "[domain=151]\n\ttable 151\n"
        cfg += "[domain=152]\n\ttable 152\n"
        cfg += "[domain=153]\n\ttable 153\n"
        cfg += "[domain=154]\n\ttable 155\n"
        cfg += "[olsrv2]\n"
        for ifc in node.netifs():
	    if not(hasattr(ifc.net, 'type')):
            	cfg += "\n".join(map(cls.subnetentry2, ifc.addrlist))
	    else:
		if (ifc.net.type == "lanswitch"):	
	            	cfg += "\n".join(map(cls.subnetentry2, ifc.addrlist))

        for ifc in node.netifs():
	    if hasattr(ifc.net, 'type'):
			if (ifc.net.type == 'wlan'):	
				cfg+= '[interface=%s]\n' % (ifc.name)
        return cfg

    @staticmethod
    def subnetentry2(x):
        ''' Generate a subnet declaration block given an IPv4 prefix string
            for inclusion in the config file.
        '''
        if x.find(":") >= 0:
            # this is an IPv6 address
            return ""
        else:
            net = IPv4Prefix(x)
            return '\tlan   %s domain=0\n' % (net)

# this line is required to add the above class to the list of available services
addservice(MyServiceOONF)

