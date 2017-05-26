#!/usr/bin/python
import json
import sys
import jinja2
import os

sep = "."
output_name = "index"
output_ext  = "html"
template_file =  sep.join( [ output_name, "jinja", output_ext ] )
output_file =  sep.join( [ output_name, output_ext ] )
working_dir = "."
out_fd = open( output_file, "w+" )

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader( working_dir ))
JINJA_ENVIRONMENT.line_comment_prefix = "#//"
JINJA_ENVIRONMENT.line_statement_prefix = "%"


jinja_vars = { 
    "tests" : ["foo", "bar", "buz" ]
}
template = JINJA_ENVIRONMENT.get_template(template_file)
output = template.render(jinja_vars)

print(output)
out_fd.write( output ) 
out_fd.close()
