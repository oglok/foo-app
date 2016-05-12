"""
Scenario2 topology
"""

from mininet.topo import Topo

class scenario (Topo):
    "Simple topology example."

    def __init__( self ):
        "Scenario2 topology."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        client = self.addHost( 'client', ip='192.168.100.11', mac='000000000011' )
        vnf1 = self.addHost( 'vnf1', ip='192.168.100.101', mac='0000000000AA' )
        vnf2 = self.addHost( 'vnf2', ip='192.168.100.102', mac='0000000000BB' )
        vnf3 = self.addHost( 'vnf3', ip='192.168.100.103', mac='0000000000CC' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink( client, s1 )
        self.addLink( s1, s2 )
        self.addLink( s1, s3 )
        self.addLink( s1, s4 )
        self.addLink( s2, vnf1 )
        self.addLink( s3, vnf2 )
        self.addLink( s4, vnf3 )

topos = { 'scenario2topo': ( lambda: scenario() ) }

