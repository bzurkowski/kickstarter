import abc
import os
import re

from kickstarter.common import logger

LOG = logger.get_logger(__name__)


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self, args):
        """Executes command with arguments."""


class Generate(Command):

    def execute(self, args):
        LOG.info("Generating Kickstart files from arguments: %s", args)


def get_command(args):
    cmd_class = get_command_class(args)
    return cmd_class()


def get_command_class(args):
    if args['generate']:
        return Generate
