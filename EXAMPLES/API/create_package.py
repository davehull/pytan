
"""
Create a package called package49
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

# setup the arguments for the delete method (to remove the package in case it exists)
delete_kwargs = {}
delete_kwargs["objtype"] = 'package'
delete_kwargs["name"] = 'package49'


# setup the arguments for the handler method
kwargs = {}
kwargs["expire_seconds"] = 1500
kwargs["display_name"] = u'package49 API test'
kwargs["name"] = u'package49'
kwargs["parameters_json_file"] = u'../doc/example_of_all_package_parameters.json'
kwargs["verify_expire_seconds"] = 3600
kwargs["command"] = u'package49 $1 $2 $3 $4 $5 $6 $7 $8'
kwargs["file_urls"] = [u'3600::testing.vbs||https://content.tanium.com/files/initialcontent/bundles/2014-10-01_11-32-15-7844/custom_tagging_-_remove_tags_[non-windows]/CustomTagRemove.sh']
kwargs["verify_filter_options"] = [u'and']
kwargs["verify_filters"] = [u'Custom Tags, that contains:tag']
kwargs["command_timeout_seconds"] = 9999

# delete the object in case it already exists
try:
    handler.delete(**delete_kwargs)
except Exception as e:
    print e

# call the handler with the create_package method, passing in kwargs for arguments
response = handler.create_package(**kwargs)


print ""
print "Type of response: ", type(response)

print ""
print "print of response:"
print response

print ""
print "print the object returned in JSON format:"
print response.to_json(response)

# delete the object, we are done with it now
try:
    handler.delete(**delete_kwargs)
except Exception as e:
    print e



'''Output from running this:
Handler for Session to 172.16.31.128:443, Authenticated: True, Version: Not yet determined!
No results found searching for PackageSpec, name: 'package49'!!
2015-08-07 19:46:14,165 INFO     pytan.handler: New package 'package49' created with ID 82, command: 'package49 $1 $2 $3 $4 $5 $6 $7 $8'

Type of response:  <class 'taniumpy.object_types.package_spec.PackageSpec'>

print of response:
PackageSpec, name: 'package49', id: 82

print the object returned in JSON format:
{
  "_type": "package_spec", 
  "available_time": "2001-01-01T00:00:00", 
  "command": "package49 $1 $2 $3 $4 $5 $6 $7 $8", 
  "command_timeout": 9999, 
  "creation_time": "2001-01-01T00:00:00", 
  "deleted_flag": 0, 
  "display_name": "package49 API test", 
  "expire_seconds": 1500, 
  "files": {
    "_type": "package_files", 
    "file": [
      {
        "_type": "file", 
        "bytes_downloaded": 0, 
        "bytes_total": 0, 
        "download_seconds": 3600, 
        "file_status": {
          "_type": "file_status", 
          "status": [
            {
              "_type": "status", 
              "bytes_downloaded": 0, 
              "bytes_total": 0, 
              "cache_status": "Processing", 
              "server_id": 1, 
              "server_name": "JTANIUM1.localdomain:17472", 
              "status": 0
            }
          ]
        }, 
        "id": 184, 
        "name": "testing.vbs", 
        "size": 0, 
        "source": "https://content.tanium.com/files/initialcontent/bundles/2014-10-01_11-32-15-7844/custom_tagging_-_remove_tags_[non-windows]/CustomTagRemove.sh", 
        "status": 0
      }
    ]
  }, 
  "hidden_flag": 0, 
  "id": 82, 
  "last_update": "2001-01-01T00:00:00", 
  "modification_time": "2001-01-01T00:00:00", 
  "name": "package49", 
  "parameter_definition": "{\"parameterType\": \"com.tanium.components.parameters::ParametersArray\", \"model\": \"com.tanium.components.parameters::ParametersArray\", \"parameters\": [{\"parameterType\": \"com.tanium.components.parameters::TextInputParameter\", \"validationExpressions\": [{\"helpString\": \"must be word\", \"flags\": \"\", \"model\": \"com.tanium.models::ValidationExpression\", \"expression\": \"\\\\S\", \"parameterType\": \"com.tanium.models::ValidationExpression\"}], \"helpString\": \"helptext\", \"maxChars\": 10, \"defaultValue\": \"defaulttex\", \"value\": \"defaulttex\", \"label\": \"textinput\", \"restrict\": null, \"key\": \"$1\", \"model\": \"com.tanium.components.parameters::TextInputParameter\", \"promptText\": \"prompttext\"}, {\"parameterType\": \"com.tanium.components.parameters::DropDownParameter\", \"helpString\": \"helptext\", \"defaultValue\": \"\", \"value\": \"v1\", \"label\": \"dropdown\", \"requireSelection\": true, \"values\": [\"v1\", \"v2\"], \"key\": \"$2\", \"model\": \"com.tanium.components.parameters::DropDownParameter\", \"promptText\": \"prompttext\"}, {\"parameterType\": \"com.tanium.components.parameters::CheckBoxParameter\", \"helpString\": \"helptext\", \"defaultValue\": \"1\", \"value\": \"1\", \"label\": \"checkbox\", \"key\": \"$3\", \"model\": \"com.tanium.components.parameters::CheckBoxParameter\"}, {\"parameterType\": \"com.tanium.components.parameters::NumericParameter\", \"helpString\": \"helptext\", \"defaultValue\": \"1\", \"maximum\": 8, \"value\": \"1\", \"label\": \"numeric\", \"stepSize\": 4, \"minimum\": 1, \"key\": \"$4\", \"model\": \"com.tanium.components.parameters::NumericParameter\", \"snapInterval\": 2}, {\"parameterType\": \"com.tanium.components.parameters::DateTimeParameter\", \"key\": \"$5\", \"start_date_restriction\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": 1414814400000, \"interval\": null, \"intervalCount\": null, \"model\": \"com.tanium.models::PointInTime\", \"type\": 3}, \"helpString\": \"helptext\", \"defaultValue\": \"\", \"value\": \"\", \"label\": \"datetime\", \"componentType\": 3, \"start_time_restriction\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": null, \"interval\": 3600, \"intervalCount\": 5, \"model\": \"com.tanium.models::PointInTime\", \"type\": 1}, \"end_date_restriction\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": 1420174800000, \"interval\": null, \"intervalCount\": null, \"model\": \"com.tanium.models::PointInTime\", \"type\": 3}, \"end_time_restriction\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": 69923000, \"interval\": null, \"intervalCount\": null, \"model\": \"com.tanium.models::PointInTime\", \"type\": 3}, \"model\": \"com.tanium.components.parameters::DateTimeParameter\"}, {\"parameterType\": \"com.tanium.components.parameters::DateTimeRangeParameter\", \"helpString\": \"helptext\", \"defaultValue\": \"\", \"default_range_start\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": null, \"interval\": 86400, \"intervalCount\": 1, \"model\": \"com.tanium.models::PointInTime\", \"type\": 2}, \"value\": \"1417159750000|1417332550000\", \"label\": \"daterange\", \"default_range_end\": {\"parameterType\": \"com.tanium.models::PointInTime\", \"unix_time_stamp\": null, \"interval\": 86400, \"intervalCount\": 1, \"model\": \"com.tanium.models::PointInTime\", \"type\": 1}, \"key\": \"$6\", \"model\": \"com.tanium.components.parameters::DateTimeRangeParameter\"}, {\"parameterType\": \"com.tanium.components.parameters::ListParameter\", \"validationExpressions\": [], \"helpString\": null, \"defaultText\": \"\", \"defaultValue\": \"\", \"value\": \"\", \"label\": \"list\", \"restrict\": null, \"allowEmptyList\": false, \"key\": \"$7\", \"maxChars\": 0, \"values\": [\"\"], \"model\": \"com.tanium.components.parameters::ListParameter\", \"promptText\": \"\"}, {\"parameterType\": \"com.tanium.components.parameters::TextAreaParameter\", \"validationExpressions\": [{\"helpString\": \"word\", \"flags\": \"\", \"model\": \"com.tanium.models::ValidationExpression\", \"expression\": \"\\\\W\", \"parameterType\": \"com.tanium.models::ValidationExpression\"}], \"helpString\": \"helptext\", \"maxChars\": 2000, \"defaultValue\": \"defaulttext\", \"heightInLines\": 5, \"value\": \"defaulttext\", \"label\": \"textarea\", \"restrict\": null, \"key\": \"$8\", \"model\": \"com.tanium.components.parameters::TextAreaParameter\", \"promptText\": \"prompttext\"}]}", 
  "skip_lock_flag": 0, 
  "source_id": 0, 
  "verify_expire_seconds": 3600, 
  "verify_group": {
    "_type": "group", 
    "id": 211
  }, 
  "verify_group_id": 211
}
2015-08-07 19:46:14,174 INFO     pytan.handler: Deleted 'PackageSpec, id: 82'

'''