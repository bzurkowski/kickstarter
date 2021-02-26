import copy
import ipaddress
import os


class Generator:

    def __init__(self, renderer):
        self._renderer = renderer

    def generate(self, output_dir, name, num_hosts, raw_paritions, raw_networks):
        net_generators = []
        for raw_network in raw_networks:
            network_args = self._normalize_args(raw_network)
            net_generators.append(NetworkGenerator(**network_args))

        partitions = []
        for raw_parition in raw_paritions:
            partition_args = self._normalize_args(raw_parition)
            partitions.append(partition_args)

        for i in range(num_hosts):
            hostname = "%s%d" % (name, i)
            host_networks = [net_generator.generate() for net_generator in net_generators]

            variables = {
                "hostname": hostname,
                "partitions": partitions,
                "networks": host_networks
            }

            filename = "%s.cfg" % hostname
            target_path = os.path.join(output_dir, filename)

            self._renderer.render(variables, target_path)

    def _normalize_args(self, raw_args):
        args = {}
        kv_pairs = raw_args.split(",")
        for kv_pair in kv_pairs:
            key, value = kv_pair.split("=")
            args[key] = value
        return args


class NetworkGenerator:

    def __init__(self, device, proto, start, end, net_mask, gateway, nameserver):
        self._device = device
        self._proto = proto
        self._start = ipaddress.ip_address(start)
        self._end = ipaddress.ip_address(end)
        self._net_mask = net_mask
        self._gateway = gateway
        self._nameserver = nameserver
        self._current_ip = copy.deepcopy(self._start)

    def generate(self):
        network = {
            "device": self._device,
            "proto": self._proto,
            "ip_address": self._current_ip,
            "net_mask": self._net_mask,
            "gateway": self._gateway,
            "nameserver": self._nameserver
        }
        self._current_ip += 1
        return network
