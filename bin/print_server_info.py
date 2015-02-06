#!/usr/bin/env python
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''Get server info'''
__author__ = 'Jim Olsen (jim.olsen@tanium.com)'
__version__ = '1.0.2'

import os
import sys
import getpass
sys.dont_write_bytecode = True
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
lib_dir = os.path.join(parent_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)

import pytan
from pytan import utils

examples = [
    {
        'name': 'Print the server info in JSON format',
        'cmd': 'print_sensor.py $API_INFO --json',
        'tests': 'exitcode',
    },
]


def print_obj(d, indent=0):
    for k, v in d.iteritems():
        if utils.is_dict(v):
            print "{}{}: \n".format('  ' * indent, k),
            print_obj(v, indent + 1)
        elif utils.is_list(v):
            print "{}{}: ".format('  ' * indent, k)
            for a in v:
                print_obj(a, indent + 1)
        else:
            print "{}{}: {}".format('  ' * indent, k, v)


def process_handler_args(parser, all_args):
    handler_grp_names = ['Handler Authentication', 'Handler Options']
    handler_opts = utils.get_grp_opts(parser, handler_grp_names)
    handler_args = {k: all_args.pop(k) for k in handler_opts}

    try:
        h = pytan.Handler(**handler_args)
        print str(h)
    except Exception as e:
        print e
        sys.exit(99)
    return h


if __name__ == "__main__":

    utils.version_check(__version__)
    parent_parser = utils.setup_parser(__doc__)
    parser = utils.CustomArgParse(
        description=__doc__,
        parents=[parent_parser],
    )
    parser.add_argument(
        '--json',
        required=False,
        default=False,
        action='store_true',
        dest='json',
        help='Show a json dump of the server information',
    )

    args = parser.parse_args()
    all_args = args.__dict__
    if not args.username:
        username = raw_input('Tanium Username: ')
        all_args['username'] = username.strip()

    if not args.password:
        password = getpass.getpass('Tanium Password: ')
        all_args['password'] = password.strip()

    if not args.host:
        host = raw_input('Tanium Host: ')
        all_args['host'] = host.strip()

    handler = process_handler_args(parser, all_args)

    if args.json:
        print utils.jsonify(handler.session.server_info)
    else:
        print str(handler)
        print_obj(handler.session.server_info)
