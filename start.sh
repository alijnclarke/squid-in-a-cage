#!/bin/sh
mkdir -p /cache/squid3
mkdir -p /cache/apt-cacher-ng
mkdir -p /cache/logs/squid3
mkdir -p /cache/logs/apt-cacher-ng
mkdir -p /cache/logs/supervisor
mkdir -p /cache/apt-cacher-ng/_import

chown -R squid:squid /cache 
/usr/sbin/squid -N -f /etc/squid/squid.conf 
