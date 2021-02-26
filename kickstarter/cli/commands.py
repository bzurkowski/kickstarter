import abc
import os

from kickstarter.common import logger
from kickstarter import generator

LOG = logger.get_logger(__name__)


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self, args):
        """Executes command with arguments."""


class Generate(Command):

    def execute(self, args):
        LOG.info("Generating Kickstart files from arguments: %s", args)

        output_dir = args.get("--output-dir") or os.getcwd()
        name = args.get("--name") or "kickstart"

        env = generator.Environment()
        template = env.get_template("kickstart.cfg.j2")
        variables = {"test_value": "foobar"}

        filename = "%s.cfg" % name
        target_path = os.path.join(output_dir, filename)

        renderer = generator.Renderer(template)
        renderer.render(variables, target_path)


def get_command(args):
    cmd_class = get_command_class(args)
    return cmd_class()


def get_command_class(args):
    if args['generate']:
        return Generate
