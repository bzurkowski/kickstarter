import jinja2


class Environment(jinja2.Environment):

    def __init__(self):
        loader = jinja2.PackageLoader('kickstarter', 'templates')
        super(Environment, self).__init__(
            loader=loader,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True)
