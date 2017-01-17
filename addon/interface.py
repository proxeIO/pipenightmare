def operator(operator, context):

	layout = operator.layout

	column = layout.column(align=True)

	column.label(text='General:')
	column.prop(operator, 'amount', text='Max Pipes')
	column.prop(operator, 'width', text='Region Width')
	column.prop(operator, 'height', text='Region Height')
	column.prop(operator, 'depth', text='Region Depth')

	column.label(text='Length:')
	column.prop(operator, 'length_x')
	column.prop(operator, 'length_y')

	column.label(text='Thickness:')
	column.prop(operator, 'min')
	column.prop(operator, 'max')

	column.label(text='Details:')
	column.prop(operator, 'straight')
	column.prop(operator, 'decoration')
	column.prop(operator, 'rail')
	column.prop(operator, 'split')
	column.prop(operator, 'bevel')

	column.label(text='Resolution:')
	column.prop(operator, 'surface')

	column.label(text='Misc:')
	column.prop(operator, 'seed')

	column.prop(operator, 'convert')

	row = column.row()
	column = row.column()
	column.active = False if operator.convert else True
	column.prop(operator, 'create_empty')
	column.prop(operator, 'hide_lines')


def menu_entry(menu, context):

	layout = menu.layout

	layout.separator()

	layout.operator('object.pipe_nightmare', text='Pipes', icon='IPO')

