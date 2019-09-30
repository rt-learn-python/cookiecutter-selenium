import logging

instance = logging.getLogger('{{cookiecutter.project_slug}}')
instance.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

{% raw %}
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s {%(pathname)s:%(lineno)d} - %(message)s',
    '%Y-%m-%d %H:%M:%S')
{% endraw %}

# add formatter to ch
ch.setFormatter(formatter)
instance.addHandler(ch)
