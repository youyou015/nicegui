from nicegui import ui

from . import doc


@doc.demo(ui.tooltip)
def tooltips_demo():
    with ui.button(icon='thumb_up'):
        ui.tooltip('I like this').classes('bg-green')


@doc.demo('Tooltip method', '''
    Instead of nesting a tooltip element inside another element, you can also use the `tooltip` method.
''')
def tooltip_method_demo():
    ui.label('Tooltips...').tooltip('...are shown on mouse over')


@doc.demo('Tooltip with HTML', '''
    You can use HTML in tooltips by nesting a `ui.html` element.
''')
def tooltip_html_demo():
    with ui.label('HTML...'):
        with ui.tooltip():
            ui.html('<b>b</b>, <em>em</em>, <u>u</u>, <s>s</s>')


@doc.demo('Tooltip with other content', '''
    You can use HTML in tooltips.
''')
def tooltip_html_demo():
    with ui.label('Mountains...'):
        with ui.tooltip().classes('bg-transparent'):
            ui.image('https://picsum.photos/id/377/640/360').classes('w-64')


doc.reference(ui.tooltip)
