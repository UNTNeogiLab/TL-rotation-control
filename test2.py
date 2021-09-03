import elliptec
from time import sleep

ports = elliptec.find_ports()
port = ports[0].device
m = elliptec.Motor(port)
m.do_('home')
sleep(1)
m.do_('forward')
sleep(1)
m.do_('home')
sleep(1)
