#!/bin/sh

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

#GNU
N="\033[1;37m"
C="\033[0m"
sleep 1
echo -e ""$N"Installing dependences..."$C""
apt-get install python
echo "done..."
apt-get install git
echo "done..."
apt-get update
echo "done..."
apt-get upgrade
echo "done..."
apt-get install wget
echo "done..."
apt-get install python2-pip
echo "done..."
apt-get install perl
echo "done..."
apt-get install Build essential
echo "done..."
apt-get install libany-uri-escape-perl
echo "done..."
apt-get install libhtml-html5-entities-perl
echo "done..."
apt-get install libhtml-entities-numbered-perl
echo "done..."
apt-get install libhtml-parser-perl
echo "done..."
apt-get install libwww-perl
echo "done..."
apt-get install php
echo "done..."
sleep 0.5
