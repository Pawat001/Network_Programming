import threading
from queue import Queue
from getpass import getpass
from netmiko import ConnectHandler

USER = 'cisco'
PASSWORD = 'cisco'

routers = ['',]

def ssh_session(router, output_q)