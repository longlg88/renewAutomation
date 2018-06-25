#!/bin/bash

apt-get -y install expect

expect << EOF
spawn sh -c "wsdown"
expect {
"WebtoB? (y : n):" { send "y\r"; exp_continue }
eof
}
EOF

sed -i -e '100,108d' /root/.bashrc
