import os, string, random

from django.utils.text import slugify


def file_ext_catch(file):
    basename = os.path.basename(file)
    file_name, ext = os.path.splitext(basename)
    return file_name, ext


def random_string_generator(size=10, chars=string.ascii_letters + string.digits):
    new_str = ''.join(random.choice(chars) for _ in range(size))
    return new_str
