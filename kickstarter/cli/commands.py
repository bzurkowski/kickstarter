import abc
import os

from kickstarter.common import logger
from kickstarter import generator as gen

LOG = logger.get_logger(__name__)


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self, args):
        """Executes command with arguments."""


class Generate(Command):

    def execute(self, args):
        LOG.info("Generating Kickstart files from arguments: %s", args)

        num_hosts = int(args.get("--num-hosts") or 1)

        raw_partitions = args.get("--part")
        raw_networks = args.get("--network")

        output_dir = args.get("--output-dir") or os.getcwd()
        name = args.get("--name") or "kickstart"

        env = gen.Environment()
        template = env.get_template("kickstart.cfg.j2")
        renderer = gen.Renderer(template)

        generator = gen.Generator(renderer)
        generator.generate(output_dir, name, num_hosts, raw_partitions, raw_networks)


def get_command(args):
    cmd_class = get_command_class(args)
    return cmd_class()


def get_command_class(args):
    if args['generate']:
        return Generate
