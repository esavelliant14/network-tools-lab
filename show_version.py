from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password'
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show version")
print(output)
