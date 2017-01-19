import os


def get_Nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results


print(get_Nmap('-F', '180.70.93.117'))
