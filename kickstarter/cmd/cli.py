"""Kickstarter
Usage:
    kick generate [--num-hosts=<num-hosts>]
                  [--disk=<disk>]
                  [--network=<network>]
                  [--output-dir=<output-dir>] [--name=<name>]
    kick -h | --help
"""

from docopt import docopt

from kickstarter import exceptions
from kickstarter.cli import commands as cmd
from kickstarter.common import logger

LOG = logger.get_logger(__name__)


def main():
    args = docopt(__doc__)
    try:
        cmd.get_command(args).execute(args)
    except exceptions.KickstarterError as ex:
        LOG.error("An error ocurred while executing the command: %s", str(ex))
