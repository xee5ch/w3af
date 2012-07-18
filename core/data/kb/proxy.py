'''
proxy.py

Copyright 2007 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''

from core.controllers.misc.commonAttackMethods import commonAttackMethods
from core.data.kb.exploitResult import exploitResult
from core.controllers.w3afException import w3afException
from core.controllers.intrusionTools.execMethodHelpers import *

# python stuff
import time

class proxy(exploitResult, commonAttackMethods):
    '''
    This class represents the output of an attack plugin that gives a proxy to the w3af user.
    
    @author: Andres Riancho ( andres.riancho@gmail.com )
    '''

    def __init__(self, proxyDaemonObject):
        exploitResult.__init__(self)
        
        self._proxyDaemon = proxyDaemonObject
        
    def end( self ):
        '''
        This method is called when the proxy is not going to be used anymore. It should be used to remove the
        auxiliary files (local and remote) generated by the proxy.
        
        @return: None
        '''
        raise w3afException('You should implement the end method of classes that inherit from "proxy"')
    
    def getName( self ):
        '''
        This method is called when the proxy is used, in order to create a prompt for the user.
        
        @return: The name of the proxy (rfi_proxy, dav_proxy, etc.)
        '''
        raise w3afException('You should implement the getName method of classes that inherit from "proxy"')

    def __repr__( self ):
        return '<proxy server at: '+self._proxyDaemon.getBindIP() + ':'+str(self._proxyDaemon.getBindPort()) + '>'
        
    __str__ = __repr__
