from pwmt import app

import markdown as markdown_module


@app.template_filter()
def render_markdown(text):
    return markdown_module.markdown(text, ['codehilite', 'extra', 'toc'])
