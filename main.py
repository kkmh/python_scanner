from general import *
from domain_name import *
from ip_address import *
from whois import *
from robots import *
from nmap import *

ROOT_DIR = 'sites'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip = get_ip_address(url)
    nmap = get_Nmap(' -F', ip)
    robots = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots, whois)


def create_report(name, url, domain_name, nmap, robots, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/url.txt', url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots)
    write_file(project_dir + '/whois.txt', whois)


gather_info('tistory', 'http://www.tistory.com/')