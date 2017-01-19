import os
import shutil

f = open("target.txt", 'r')  ## 타켓파일 읽기
while 1:
    line = f.readline()
    if not line:
        break
    line = line.split("\n")
    target_ip = line[0]
    # target_ip = line[0] + "-255"     # C class 대역 IP 읽어오기
    nmap_command = "nmap -T3 -sT -O -A -oA " + line[0] + " " + target_ip
    print("scanIP : ", nmap_command)
    os.system(nmap_command)


    if not os.path.exists(line[0]):
        os.makedirs(line[0])     # IP 별 폴더 생성

        nmap_xml = line[0] + ".xml"       # 파일확장자 설정
        nmap_nmap = line[0] + ".nmap"
        nmap_gnmap = line[0] + ".gnmap"
        target_dir = line[0]

        try:
            shutil.move(nmap_gnmap, target_dir)
            shutil.move(nmap_nmap, target_dir)
            shutil.move(nmap_xml, target_dir)
        except:
            pass
