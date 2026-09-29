import sys
from pathlib import Path

parent_dir = str( Path( __file__).resolve().parent.parent )
if parent_dir not in sys.path:
  sys.path.append( parent_dir )

# print( sys.path )

from datetime import timedelta
from script_generater import _generate_script

import os

file_dir = Path(__file__).resolve().parent

submit_command = [ 'sbatch' ]
status_command = 'squeue -O JobArrayID,StateCompact,Reason -t all --me'.split()
cancel_command = 'scancel -Q'.split()

# def __init__( self ):
#   pass

# def get_submit_cmd( self ) -> str:
#   return self._submit_command
def get_submit_cmd() -> str:
  return submit_command

# def get_status_cmd( self ) -> str:
#   return self._status_command
def get_status_cmd() -> str:
  return status_command

# def get_cancel_cmd( self ) -> str:
#   return self._cancel_command
def get_cancel_cmd() -> str:
  return cancel_command

# def job_id_from_submit_output( output: str ):
#   return output.strip().split()[ -1 ]

def time_formatting( d: timedelta ):
  return f"{d.days}-{d.seconds // 3600:02}:{(d.seconds // 60) % 60:02}:{d.seconds % 60:02}"

def generate_script( job_spec: dict ):
  ## In case job_spec need to correcting the format do it before render
  formatted_duration = None
  if type( job_spec['duration'] ) is timedelta:
    formatted_duration = time_formatting( job_spec['duration'] )
  elif type( job_spec['duration'] ) is str:
    formatted_duration = job_spec['duration']
  job_spec['formatted_duration'] = formatted_duration
  return _generate_script( file_dir, 'slurm.jinja', job_spec )

# response from submit "Submitted batch job 638725"
def get_job_id_from_submit( response ):
  return response.split()[ 3 ]

def is_submitted( response ) -> bool:
  keyword = "Submitted"
  if keyword in response.split():
    return True
  else:
    return False