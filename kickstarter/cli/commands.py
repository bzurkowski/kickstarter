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

        disk = int(args.get("--disk") or 10)

        output_dir = args.get("--output-dir") or os.getcwd()
        name = args.get("--name") or "kickstart"

        env = gen.Environment()
        template = env.get_template("kickstart.cfg.j2")
        renderer = gen.Renderer(template)

        generator = gen.Generator(renderer)
        generator.generate(output_dir, name, num_hosts, disk)


def get_command(args):
    cmd_class = get_command_class(args)
    return cmd_class()


def get_command_class(args):
    if args['generate']:
        return Generate
