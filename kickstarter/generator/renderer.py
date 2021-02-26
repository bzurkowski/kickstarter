from kickstarter.common import logger

LOG = logger.get_logger(__name__)


class Renderer:

    def __init__(self, template, variables):
        self._template = template
        self._variables = variables

    def render(self):
        LOG.info("Rendering file from template with variables: %s", self._variables)
        data = self._template.render(self._variables).encode('utf8')
        LOG.info("Rendered content: %s", data)
