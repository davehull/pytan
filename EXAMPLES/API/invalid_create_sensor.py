
"""
Create a sensor (Unsupported!)
"""

import os
import sys
sys.dont_write_bytecode = True

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# determine the pytan lib dir and add it to the path
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)


# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "443"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import tempfile

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the arguments for the handler method
kwargs = {}


# call the handler with the create_sensor method, passing in kwargs for arguments
# this should throw an exception: pytan.exceptions.HandlerError
import traceback
try:
    handler.create_sensor(**kwargs)
except Exception as e:
    traceback.print_exc(file=sys.stdout)



'''Output from running this:
Handler for Session to 172.16.31.128:443, Authenticated: True, Version: Not yet determined!
Traceback (most recent call last):
  File "<string>", line 53, in <module>
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 708, in create_sensor
    raise pytan.exceptions.HandlerError(m)
HandlerError: Sensor creation not supported via PyTan as of yet, too complex
Use create_sensor_from_json() instead!

'''