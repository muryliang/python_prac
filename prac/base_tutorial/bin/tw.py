from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols.basic import LineReceiver

class SimpleLogger(LineReceiver):
	def connectionMade(self):
		print "Got connection From", self.transport.client

	def connectionLost(self, reason):
		print self.transport.client, 'disconnect'

	def lineReceived(self, line):
		print line

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
