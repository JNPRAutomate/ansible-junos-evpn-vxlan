from bracket_expansion import *
import yaml
import os
import jinja2
import ipaddress

mydir = "./temp"

datavars = yaml.load(open("topology.yml").read())

print datavars

try:
    os.stat(mydir)
except:
    os.mkdir(mydir) 
    

startUnderlayBgpAs = int(datavars['UnderlayStartBgpAs'])
startLinkIP = ipaddress.IPv4Address(unicode(datavars['p2pStartIp']))
deviceIfIpMap = {}
deviceAsMap = {}

for device in datavars['devices']:
    print device
    
    try:
        deviceIfIpMap[device]
    except:
        deviceIfIpMap[device] = {}

    try:
        deviceAsMap[device]
    except:
        deviceAsMap[device] = startUnderlayBgpAs
        startUnderlayBgpAs += 1
            
    devicedir = mydir + "/" + device
    try:
        os.stat(devicedir)
    except:
        os.mkdir(devicedir) 
        
    filename = mydir + "/" + device + "/" "underlay.conf.yaml"
    yamlfile = open(filename, "wb")
    yamlfile.write("underlay:\n")
    yamlfile.write("    local:\n")
    yamlfile.write("        asn:" + str(deviceAsMap[device]) + "\n")
    for links in datavars['core-links']:
        if (device == links['p1']):
            print deviceIfIpMap
            yamlfile.write("        - interface: " + str(links['if1']) + "\n")
            yamlfile.write("          name: " + str(links['p2'])  + "\n")
            try:
                deviceAsMap[links['p2']]
            except:
                deviceAsMap[links['p2']] = startUnderlayBgpAs
                startUnderlayBgpAs += 1
             
            yamlfile.write("          asn: " + str(deviceAsMap[links['p2']])  + "\n")   
            
            try:
                deviceIfIpMap[device][links['if1']]
            except:
                deviceIfIpMap[device][links['if1']] = startLinkIP

            try:
                deviceIfIpMap[links['p2']]
            except:
                deviceIfIpMap[links['p2']] = {}

            try:
                deviceIfIpMap[links['p2']][links['if2']]
            except:
                deviceIfIpMap[links['p2']][links['if2']] = startLinkIP + 1
                startLinkIP += 1
                
                                                        
            yamlfile.write("          peer_ip: " + str(deviceIfIpMap[links['p2']][links['if2']])  + "\n")
            yamlfile.write("          local_ip: " + str(deviceIfIpMap[device][links['if1']])  + "\n")
        elif (device == links['p2']):
            print deviceIfIpMap
            yamlfile.write("        - interface: " + str(links['if2'])  + "\n")
            yamlfile.write("          name: " + str(links['p1'])  + "\n")
            
            try:
                deviceAsMap[links['p1']]
            except:
                deviceAsMap[links['p1']] = startUnderlayBgpAs
                startUnderlayBgpAs += 1
             
            yamlfile.write("          asn: " + str(deviceAsMap[links['p1']])  + "\n") 
            
            try:
                deviceIfIpMap[device][links['if2']]
            except:
                deviceIfIpMap[device][links['if2']] = startLinkIP

            try:
                deviceIfIpMap[links['p1']]
            except:
                deviceIfIpMap[links['p1']] = {}

            try:
                deviceIfIpMap[links['p1']][links['if1']]
            except:
                deviceIfIpMap[links['p1']][links['if1']] = startLinkIP + 1
                startLinkIP += 1
                                                        
            yamlfile.write("          peer_ip: " + str(deviceIfIpMap[links['p1']][links['if1']])  + "\n")
            yamlfile.write("          local_ip: " + str(deviceIfIpMap[device][links['if2']])  + "\n")
            
        startLinkIP += 1
            
    yamlfile.close()