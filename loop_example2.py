interface_list = ["interface g0/0", "interface g0/1", "interface g0/2", "interface loopback0"]

for interface in interface_list:
    print(f"{interface}\n description This is {interface}")