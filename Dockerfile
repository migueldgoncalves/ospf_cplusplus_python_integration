FROM ubuntu:16.04

#  Ubuntu 16.04 or earlier is required, as in more recent Linux kernel versions linux/ip.h and netinet/ip.h (included by
#  linux/if_tunnel.h) enter in conflict by defining data structure with same name 'iphdr'

WORKDIR /ospf

# DEBIAN_FRONTEND environement variable set to "noninteractive" to overcome tzdata prompt
# tcl is used by the base OSPF implementation - Development package is required

RUN apt update && DEBIAN_FRONTEND="noninteractive" apt install --yes python3 \
python3-pip \
iproute2 \
iputils-ping \
traceroute \
tcl-dev

VOLUME /ospf