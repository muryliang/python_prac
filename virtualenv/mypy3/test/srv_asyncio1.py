#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter07/zen_utils.py

import socket, zen_utils

class ZenServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection rom {}'.format(self.address))

    def data_received(self, data):
        self.data += data
        if self.data.endswith(b'?'):
            answer = zen_utils.get_answer(self.data)
            self.transport.write(answer)
            self.data = b''

    def connection_lost(self, exc):
        if exc:
            print('client {} error: {}'.format(self.address, exc))
        elif self.data:
            print('cilent {} sent {} but then closed'
                    .format(self.address, self.data))
        else:
            print('client {} closed normally socket'.format(self.address))

if __name__ == '__main__':
    address = zen_utils.parse_command_line('asyuncio server using callbakcs')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ZenServer, *address)
    server = loop.run_until_complete(coro)
    print('listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
