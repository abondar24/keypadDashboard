import serial
import sys
import time
import stomp
import json
from artemis_listener import Listener

def read_serial(sr):
    line = sr.readline()
    decoded = line[0:len(line)-2].decode('utf-8')
    return decoded



def send_to_queue(msg,conn):

    #demo credentials
    conn.connect("admin", "keypadAdmin", wait=True)
    body = json.dumps({"msg":msg})
    print("Sending message {0} to queue".format(body))
    conn.send(body=body, destination="keypad")

    conn.disconnect()



## example of port /dev/ttyACM1
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Missing serial port")
        sys.exit(1)

    artemis_hosts = [("localhost", 61613)]
    conn = stomp.Connection(host_and_ports=artemis_hosts)
    conn.set_listener('', Listener())

    port = sys.argv[1]
    sr = serial.Serial(port)
    sr.flushInput()
    print("ready recieve input")


    while True:
        try:
            msg = read_serial(sr)
            send_to_queue(msg,conn)
        except:
            print("Keyboard interrupt")
            break
