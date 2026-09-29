
from jinja2 import Environment, FileSystemLoader

def _generate_script( job_template_dir, job_template_file, job_spec: dict ):
  env = Environment(
    loader = FileSystemLoader( searchpath = job_template_dir ),
    trim_blocks = True,
    lstrip_blocks = True
  )
  template = env.get_template( job_template_file )

  return template.render( job_spec )
