#!/bin/bash

# Steps to install wikipedia2text:-

# git clone https://github.com/chrisbra/wikipedia2text 
# sudo mv wikipedia2text/wikipedia2text /bin/wiki-cli
# rm -Rf wikipedia2text



while true
do
 echo "Enter the Topic to be searched "  
 read topic_name
 echo -ne '#####                     (33%)\r'
 sleep 1
 echo -ne '#############             (66%)\r'
 sleep 1
 echo -ne '#######################   (100%)\r'
 echo -ne '\n'

 url=`wiki-cli -u $topic_name`
 echo $url >> output.txt
done
