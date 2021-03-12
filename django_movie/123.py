# [Unit]
# Description=The NGINX HTTP and reverse proxy server
# After=syslog.target network.target remote-fs.target nss-lookup.target
#
# [Service]
# Type=forking
# PIDFile=/run/nginx.pid
# ExecStartPre=/usr/sbin/nginx -t
# ExecStart=/usr/sbin/nginx
# ExecReload=/bin/kill -s HUP $MAINPID
# ExecStop=/bin/kill -s QUIT $MAINPID
# PrivateTmp=true
#
# [Install]
# WantedBy=multi-user.target
#
