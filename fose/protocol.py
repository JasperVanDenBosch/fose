import urlparse

class UriBuilder(object):

    def __init__(self, providerRootUrl):
        self.root = providerRootUrl

    def forDoi(self, doi):
        doiBase = urlparse.urljoin(self.root, 'doi/')
        return urlparse.urljoin(doiBase, doi)
