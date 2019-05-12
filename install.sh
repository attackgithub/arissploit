#!/bin/bash

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

CE="\033[0m"
RS="\033[1;31m"
YS="\033[1;33m"

cd 
if [[ -d arissploit ]]
then
clear
cd arissploit
else
git clone https://github.com/entynetproject/arissploit.git
cd arissploit 
chmod +x install.sh
./install.sh
fi

printf '\033]2;Arissploit INSTALLER\a'
clear
cat banner/banner7.py
echo -e "\033[1;33mBy Entynetproject\033[0m"
sleep 3
echo -e "More on our site:"
sleep 3
echo -e "==> \033[1;33mhttp://entynetproject.simplesite.com/\033[0m"
sleep 3
echo -e "Creators of Arissploit Framework:"
sleep 3
echo -e "\033[4;34mEntynetproject\033[0m - Main Developer"
sleep 3
echo -e "\033[4;33mDJ Mobley\033[0m      - Ascii Designer"
sleep 3
echo -e "Press \033[1;33many key\033[0m to install arissploit"
read -n 1

clear
{
cp bin/arissploit /bin
chmod +x /bin/arissploit
cp bin/arissploit /usr/local/bin
chmod +x /usr/local/bin/arissploit
} &> /dev/null

sleep 1
echo -e "Install arissploit on amd or arm("$YS"amd"$CE"/"$YS"arm"$CE")?"
echo -e "Our programm supports two popular architectures "$YS"amd"$CE" and "$YS"arm"$CE"!"
echo -e "Select your architecture to install compatible arissploit dependences!"
read -p $'(\033[4;93march\033[0m)> ' CONF

if [[ "$CONF" = "amd" ]]
then
clear
cd Install
chmod +x installgnuroot.sh
./installgnuroot.sh
pip install -r requirements.txt
fi

if [[ "$CONF" = "arm" ]]
then
clear
cd Install
chmod +x installtermux.sh
./installtermux.sh
pip install -r requirements.txt
fi

printf '\033]2;Arissploit INSTALLER\a'
sleep 3
echo -e "Open a NEW terminal and type '"$YS"arissploit"$CE"' to launch framework"
