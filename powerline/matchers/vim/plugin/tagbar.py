# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

import os
import re

from powerline.bindings.vim import buffer_name


TAGBAR_RE = re.compile(b'__Tagbar__')


def tagbar(matcher_info):
	name = buffer_name(matcher_info)
	return name and TAGBAR_RE.match(os.path.basename(name))
