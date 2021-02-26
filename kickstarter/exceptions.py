class KickstarterError(Exception):

    message = "An unknown exception occurred."

    def __init__(self, **kwargs):
        msg = self.message % kwargs
        super(KickstarterError, self).__init__(msg)
