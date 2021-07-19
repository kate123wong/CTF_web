#!/bin/bash
set -e
echo `service mysql status`
service mysql start
mysql < /mysql/schema.sql
tail -f /dev/null
