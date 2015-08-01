from fabric.api import local, run
from fabric.context_managers import lcd
from mysite.version import get_git_version
from glob import glob
import os
import re
import deploy
import build
import test
import docs
import ci
