#!/bin/bash
function cleanup {
	rm -rf src dest rsyncd.conf
}
trap cleanup EXIT

mkdir src dest
cp -r files/ src/	
echo "[files]"$'\n'"path = $PWD/src" > rsyncd.conf

sudo rsync --daemon --config=rsyncd.conf
tshark.exe -i '\Device\NPF_Loopback' -a duration:10 -f "port 873" -w packet-hero.pcap &

sleep 5 # wait for tshark to start
rsync -rzv rsync://localhost:873/files/ dest/

sudo pkill -f rsyncd
# kill %1
wait
