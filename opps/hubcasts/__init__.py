
import pkg_resources

pkg_resources.declare_namespace(__name__)

VERSION = (0, 1, 1)

__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Streaming hub control, App for Opps Platform"

__author__ = u"Thiago Avelino"
__credits__ = []
__email__ = u"thiagoavelinoster@gmail.com"
__copyright__ = u"Copyright 2013, Opps Project"
