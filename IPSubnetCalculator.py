import random
import sys

def subnet_calc():

    print("\n")
    
            print("Welcome to Canberk's IP Subnet Calculator!\n")
            ip_address = input("Enter an IP address: ")
            
                     
            ip_octets = ip_address.split('.')
                        
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and  != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            
            else:
                print("\nThe IP address is INVALID! Please retry!\n")
                continue
        
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        
        
    
            subnet_mask = input("Enter a subnet mask: ")
            
                      
            mask_octets = subnet_mask.split('.')
            
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks)):
                break
            
            else:
                print("\nThe subnet mask is INVALID! Please retry!\n")
                continue
                
                        mask_octets_binary = []
        
        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
    
            
            mask_octets_binary.append(binary_octet.zfill(8))
                
                
        binary_mask = "".join(mask_octets_binary)

        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2) #return a positive value for the /32 mask (all 255s)
        
        wildcard_octets = []
        
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
            
             
        wildcard_mask = ".".join(wildcard_octets)
   
        ip_octets_binary = []
        
        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')

            
            ip_octets_binary.append(binary_octet.zfill(8))

        
        binary_ip = "".join(ip_octets_binary)

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros

        
        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros

        net_ip_octets = []
        

        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)
        
        net_ip_address = []
        
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        
        network_address = ".".join(net_ip_address)
        
subnet_calc()
