def ip_address_func(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

ipaddress = str(input("Enter IP Address : "))
ipaddress = ip_address_func(ipaddress)
print("Defang IP Address Is : "+ ipaddress)