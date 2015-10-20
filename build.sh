#!/usr/bin/env bash
#java -jar jython-standalone-2.7-b3.jar setup.py

#Cleanup previous build
rm output.jar 2>/dev/null
rm output.run 2>/dev/null
rm output 2>/dev/null
rm "${1}" 2>/dev/null

#Prepare fat Jar
cp jython-standalone-2.7.0.jar output.jar
zip -r output.jar app
zip output.jar __run__.py
jar ufm output.jar manifest.txt

#Prepare shell with embedded jar
if test -n "${1}"; then
    cat stub.sh output.jar > "${1}" && chmod +x "${1}"
    rm output.jar 2>/dev/null
    rm output 2>/dev/null

fi

