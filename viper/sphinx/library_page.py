from docutils import nodes
from docutils.parsers.rst import Directive


class Library(Directive):

    def run(self):
        # Add title based on the library directory name
        self.doc.title(os.path.basename(self.library_path))  # The title is taken from the directory name of the library
        library_node = nodes.title("")
        return [library_node]


def setup(app):
    app.add_directive("library", Library)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
