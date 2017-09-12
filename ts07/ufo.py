# -*- coding: utf-8 -*-
#
# Simple python driver for the LEDENET Magic UFO LED WiFi Controller
#
# License: 3-Clause BSD
# Copyright 2017 Kale J. Franz
#
# Redistribution and use in source and binary forms, with or without modification, are permitted
# provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of
#    conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of
#    conditions and the following disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to
#    endorse or promote products derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
# WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import absolute_import, division, print_function, unicode_literals

from collections import namedtuple
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, SO_REUSEADDR, socket, timeout
from struct import pack, unpack
from time import sleep

# Resources:
#   https://github.com/sidoh/ledenet_api/blob/master/lib/ledenet/api.rb
#   https://github.com/home-assistant/home-assistant/issues/530#issuecomment-150887786
#   https://github.com/home-assistant/home-assistant/issues/530#issuecomment-157218268

API_PORT = 5577
Status = namedtuple('Status', ('packet_id', 'device_name', 'power_status', 'mode',
                               'run_status', 'speed', 'red', 'green', 'blue', 'warm_white',
                               'unused_1', 'unused_2', 'unused_3', 'checksum'))


class Ufo(object):

    @classmethod
    def discover_all(cls):
        s = socket(AF_INET, SOCK_DGRAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        s.sendto(b'HF-A11ASSISTHREAD', (b'<broadcast>', 48899))
        s.settimeout(1)

        discovered = []
        try:
            while True:
                data = s.recv(1024)
                discovered.append(cls(*data.decode('utf-8').split(',')[:2]))
        except timeout:
            s.close()

        return tuple(sorted(discovered, key=lambda x: x.ip_address))

    @classmethod
    def all_on(cls):
        for ufo in cls.discover_all():
            ufo.on()

    @classmethod
    def all_off(cls):
        for ufo in cls.discover_all():
            ufo.off()

    @classmethod
    def all_rgbw(cls, r, g, b, w):
        for ufo in cls.discover_all():
            ufo.rgbw(r, g, b, w)

    @classmethod
    def all_status(cls):
        builder = []
        for ufo in cls.discover_all():
            print(ufo)
            builder.append(str(ufo))
        builder.append('')
        return '\n'.join(builder)

    def __init__(self, ip_address, hw_address=None):
        self.ip_address = ip_address
        self.hw_address = hw_address

    @property
    def status(self):
        s = socket()
        try:
            s.connect((self.ip_address, API_PORT))

            status_request = pack(">BBBB", 0x81, 0x8A, 0x8B, 0x96)
            s.send(status_request)
            sleep(0.2)

            data = b''
            while len(data) < 14:
                data += s.recv(14)
            stts = Status(*unpack(">" + "B" * 14, data))
            assert stts.checksum == sum(stts[:-1]) % 0x100
            return stts
        finally:
            s.close()

    @property
    def is_on(self):
        return (self.status.power_status & 0x01) == 0x01

    def __str__(self):
        status = self.status
        is_on = (status.power_status & 0x01) == 0x01
        builder = []
        if self.hw_address:
            hw_addr = ':'.join(self.hw_address[i:i + 2] for i in range(0, 12, 2)).lower()
            builder.append("%s is %s" % (self.ip_address, hw_addr))
        else:
            builder.append(self.ip_address)
        builder.append("  power: %s" % ('on' if is_on else 'off'))
        builder.append("  rgbw: %s, %s, %s, %s" % (
            status.red, status.green, status.blue, status.warm_white
        ))
        return '\n'.join(builder)

    def _send_bytes(self, *bytes):
        s = socket()
        checksum = sum(bytes) % 0x100
        payload = bytes + (checksum,)
        try:
            s.connect((self.ip_address, API_PORT))
            s.send(pack(">" + "B" * len(payload), *payload))
        finally:
            s.close()

    def on(self):
        self._send_bytes(0x71, 0x23, 0x0F)
        return self

    def off(self):
        self._send_bytes(0x71, 0x24, 0x0F)
        return self

    def rgbw(self, r, g, b, w):
        packet_id = 0x31
        unused_payload = 0
        remote_or_local = 0x0F
        self._send_bytes(packet_id, r, g, b, w, unused_payload, remote_or_local)
        return self


if __name__ == "__main__":
    Ufo.all_status()
