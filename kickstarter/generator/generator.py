import os


class Generator:

    def __init__(self, renderer):
        self._renderer = renderer

    def generate(self, output_dir, name, num_hosts, disk):
        for i in range(num_hosts):
            hostname = "%s%d" % (name, i)

            variables = {
                'hostname': hostname
            }

            filename = "%s.cfg" % hostname
            target_path = os.path.join(output_dir, filename)

            self._renderer.render(variables, target_path)
