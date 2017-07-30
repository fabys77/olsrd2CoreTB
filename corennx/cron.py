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

class MyServiceCRON(CoreService):
    ''' This is a sample user-defined service. 
    '''
    # a unique name is required, without spaces
    _name = "cron"
    # you can create your own group here
    _group = "Ninux"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ('/etc/ninux','/etc/cron.daily','/etc/cron.monthly','cron.weekly','cron.d','/var/log/nnx',)
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ('etc/ninux/cron', )
    # this controls the starting order vs other enabled services
    _startindex = 57
    # list of startup commands, also may be generated during startup
    _startup = ('/bin/sh /etc/ninux/cron',)
    # list of shutdown commands
    _shutdown = ()

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
        cfg = "#Put hear yor custom cmd\n"
        cfg += "/home/fabio/nday/compublicd.sh &\n"
        return cfg

# this line is required to add the above class to the list of available services
addservice(MyServiceCRON)

