from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives


class Nugget(Directive):
    required_arguments = 0
    optional_arguments = 0
    option_spec = {'id': directives.unchanged_required,
                   'name': directives.unchanged_required,
                   'activity': directives.unchanged
                   }
    has_content = False
#    final_argument_whitespace = True

    def run(self):
        activity = self.options.get('activity')
        if not activity:
            activity="UNICO"

        nugget_url = "https://ip.festo-didactic.com/DigitalEducation/EITManufacturing/"+activity+"/FDRenderer/index.html?LearningNugget="+self.options.get('id')+"&Language=EN&FDEP=true" 
        nugget_name = self.options.get('name')
        paragraph_node = nodes.paragraph(...)
        ref_node = nodes.reference('', nugget_name, internal=False, refuri=nugget_url)
        #inner_node = nodes.emphasis("link", nugget_name)
        #ref_node.append(inner_node)
        paragraph_node.append(ref_node)

        html = '<iframe class="nugget" src="'+nugget_url+'"></iframe>'
        raw_node = nodes.raw('', html, format='html')
        return [paragraph_node, raw_node]


def setup(app):
    app.add_directive("nugget", Nugget)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
