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

Generate Kickstart files:

```bash
kick generate \
    --name=orca \
    --num-hosts=3 \
    --part=mnt_point=/,size=122880 \
    --part=mnt_point=/nfs,size=460800 \
    --network=device=eth0,proto=static,start=172.17.80.128,end=172.17.80.191,net_mask=255.255.255.0,gateway=172.17.80.254,nameserver=172.29.128.101 \
    --network=device=eth1,proto=static,start=10.10.10.128,end=10.10.10.191,net_mask=255.255.255.0,gateway=10.10.10.1,nameserver=8.8.8.8 \
    --output-dir=/home/ubuntu/kickstart
```

Copy Kickstart files to VM host machine:

```
rsync -avz /home/ubuntu/kickstart/host1.cfg root@<MACHINE_IP>:/root/kickstart/host1.cfg
```

Provision VMs:

```bash
virt-install \
    --virt-type=kvm \
    --name host1 \
    --ram 57344 \
    --vcpus=32 \
    --cpu host \
    --accelerate \
    --os-type=linux \
    --os-variant=centos7.0 \
    --location=/home/libvirt/images/CentOS-7-x86_64-Minimal-2009.iso \
    --network=bridge=br0,model=virtio \
    --network=bridge=br1,model=virtio \
    --disk path=/home/libvirt/images/host1.raw,size=425,bus=virtio,format=raw \
    --graphics vnc \
    --initrd-inject=/root/kickstart/host1.cfg \
    --extra-args "ks=file:/host1.cfg"
```
