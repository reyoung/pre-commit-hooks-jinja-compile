# *-* coding=utf-8 *-*
import sys
import jinja2
import json


def main():
    for filename in sys.argv[1:]:
        if filename.endswith(".json"):
            filename = filename[:-len(".json")] + ".tmpl"
        tmpl = jinja2.Template(open(filename).read().decode('utf-8'))
        with open(filename[:-len(".tmpl")] + ".json") as f:
            data = json.load(f)
        buf = tmpl.render(data).encode('utf-8')
        with open(filename[:-len(".tmpl")], 'w') as f:
            f.write(buf)


if __name__ == '__main__':
    main()
