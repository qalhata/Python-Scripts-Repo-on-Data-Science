# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:05:22 2017

@author: Shabaka
"""

# Same as before, with a kivy-based UI

'''
Bluetooth/Pyjnius example
=========================
This was used to send some bytes to an arduino via bluetooth.
The app must have BLUETOOTH and BLUETOOTH_ADMIN permissions (well, i didn't
tested without BLUETOOTH_ADMIN, maybe it works.)
Connect your device to your phone, via the bluetooth menu. After the
pairing is done, you'll be able to use it in the app.
'''

from jnius import autoclass

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createRfcommSocketToServiceRecord(
                UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            recv_stream = socket.getInputStream()
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return recv_stream, send_stream

if __name__ == '__main__':
    kv = '''
BoxLayout:
    Button:
        text: '0'
        on_release: app.reset([b1, b2, b3, b4, b5])
    ToggleButton:
        id: b1
        text: '1'
        on_release: app.send(self.text)
    ToggleButton:
        id: b2
        text: '2'
        on_release: app.send(self.text)
    ToggleButton:
        id: b3
        text: '3'
        on_release: app.send(self.text)
    ToggleButton:
        id: b4
        text: '4'
        on_release: app.send(self.text)
    ToggleButton:
        id: b5
        text: '5'
        on_release: app.send(self.text)
    '''
    from kivy.lang import Builder
    from kivy.app import App

    class Bluetooth(App):
        def build(self):
            self.recv_stream, self.send_stream = get_socket_stream('linvor')
            return Builder.load_string(kv)

        def send(self, cmd):
            self.send_stream.write('{}\n'.format(cmd))
            self.send_stream.flush()

        def reset(self, btns):
            for btn in btns:
                btn.state = 'normal'
            self.send('0\n')

Bluetooth().run()
