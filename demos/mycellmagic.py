from IPython.core.magic import register_cell_magic
@register_cell_magic
def run_and_save(line, cell):
    'Run and save python code block to a file'
    with open(line, 'wt') as fd:
        fd.write(cell)
    code = compile(cell, line, 'exec')
    exec(code, globals())

@register_cell_magic
def save2file(line, cell):
    'save python code block to a file'
    with open(line, 'wt') as fd:
        fd.write(cell)
