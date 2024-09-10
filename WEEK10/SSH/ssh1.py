from netmiko import ConnectHandler

SW4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.200.140',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**SW4)

output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address ']