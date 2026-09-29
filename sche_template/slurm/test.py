import sys
from pathlib import Path

parent_dir = str( Path( __file__).resolve().parent.parent )
if parent_dir not in sys.path:
  sys.path.append( parent_dir )

print( sys.path )

# from sche_template.script_generater import generate_script_
from script_generater import _generate_script
# from .. import script_generater
# import script_generater

print( _generate_script )

