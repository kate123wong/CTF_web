#!/bin/bash
set -e
echo `whereis mysql`
echo `mysql --version`

echo `find / -name mysql.sock`

echo `ps -ef |grep mysql`

echo `systemctl start mysql.service`

echo `systemctl status mysql.service`

#cp `whereis mysql`/etc/init.d/mysqld

echo "开始数据载入"
mysql < /var/lib/mysql/data.sql
echo "数据载入完成"
mysql < /var/lib/mysql/privileges.sql
echo "修改密码完成"
tail -f /dev/null
