from kickstarter.common import logger

LOG = logger.get_logger(__name__)


class Renderer:

    def __init__(self, template):
        self._template = template

    def render(self, variables, target_path):
        LOG.info("Rendering file '%s' from variables: %s", target_path, variables)
        data = self._template.render(variables).encode('utf8')

        with open(target_path, "wb") as target:
            target.write(data)
