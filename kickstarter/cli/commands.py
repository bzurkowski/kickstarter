import abc
import os
import re

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

        env = generator.Environment()
        template = env.get_template("kickstart.cfg.j2")
        variables = {"test_value": "foobar"}
        renderer = generator.Renderer(template, variables)
        renderer.render()


def get_command(args):
    cmd_class = get_command_class(args)
    return cmd_class()


def get_command_class(args):
    if args['generate']:
        return Generate
