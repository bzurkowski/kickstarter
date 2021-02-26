# Kickstarter

## Installation

Create and activate virtual env:

```bash
$ virtualenv -p $(which python3) ~/.venvs/kickstarter
$ source ~/.venvs/kickstarter/bin/activate
```

Install the package:

```bash
$ pip install .
```

## Usage

```bash
kick generate \
    --name=orca \
    --num-hosts=3 \
    --part=mnt_point=/,size=10240 \
    --part=mnt_point=/nfs,size=30000 \
    --network=device=eth0,proto=static,start=172.17.80.128,end=172.17.80.191,net_mask=255.255.255.0,gateway=172.17.80.254,nameserver=172.29.128.101 \
    --network=device=eth1,proto=static,start=10.10.10.128,end=10.10.10.191,net_mask=255.255.255.0,gateway=10.10.10.1,nameserver=8.8.8.8
```
