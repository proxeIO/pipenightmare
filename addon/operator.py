import bpy

from bpy.types import Operator
from bpy.props import BoolProperty, IntProperty, FloatProperty

from . import interface
from .config import defaults as default
from .utils import generate


class pipe_nightmare(Operator):
	bl_idname = 'object.pipe_nightmare'
	bl_label = 'Add Pipes'
	bl_description = 'Generate random pipes.'
	bl_options = {'PRESET', 'REGISTER', 'UNDO'}


	amount = IntProperty(
		name = 'Amount',
		description = 'Maximum number of pipes',
		min = 0,
		max = 1000,
		default = default['amount']
	)

	width = FloatProperty(
		name = 'Width',
		description = 'Width of the area that the pipes occupy.',
		subtype = 'DISTANCE',
		min = 0,
		soft_max = 10,
		default = default['width']
	)

	height = FloatProperty(
		name = 'Height',
		description = 'Height of the area that the pipes occupy',
		subtype = 'DISTANCE',
		min = 0,
		soft_max = 10,
		default = default['height']
	)

	depth = FloatProperty(
		name = 'Depth',
		description = 'Depth of the area that the pipes occupy',
		subtype = 'DISTANCE',
		min = 0,
		soft_max = 10,
		default = default['depth']
	)

	length_x = FloatProperty(
		name = 'X',
		description = 'Maximum length of horizantal pipes.',
		subtype = 'DISTANCE',
		min = 0,
		soft_max = 10,
		default = default['length_x']
	)

	length_y = FloatProperty(
		name = 'Y',
		description = 'Maximum length of vertical pipes.',
		subtype = 'DISTANCE',
		min = 0,
		soft_max = 10,
		default = default['length_y']
	)

	min = FloatProperty(
		name = 'Minimum',
		description = 'The minimum thickness of the pipes.',
		subtype = 'DISTANCE',
		min = 0.0,
		max = 5.0,
		precision = 3,
		default = default['min']
	)

	max = FloatProperty(
		name = 'Maximum',
		description = 'The maximum thickness of the pipes.',
		subtype = 'DISTANCE',
		min = 0.0,
		max = 5.0,
		precision = 3,
		default = default['max']
	)

	straight = IntProperty(
		name = 'Straight Pipes',
		description = 'The amount of pipes that are straight',
		subtype = 'PERCENTAGE',
		min = 0,
		max = 100,
		default = default['straight']
	)

	decoration = IntProperty(
		name = 'Decorations',
		description = 'Amount of pipes that have additional decorations located along them.',
		subtype = 'PERCENTAGE',
		min = 0,
		max = 100,
		default = default['decoration']
	)

	rail = IntProperty(
		name = 'Rails',
		description = 'Amount of pipes that will have additional rails alongside them.',
		subtype = 'PERCENTAGE',
		min = 0,
		max = 100,
		default = default['rail']
	)

	split = IntProperty(
		name = 'Split',
		description = 'Amount of pipes that should be split up into smaller pipes that occupy the same path.',
		subtype = 'PERCENTAGE',
		min = 0,
		max = 100,
		default = default['split']
	)

	bevel = IntProperty(
		name = 'Bevel',
		description = 'Amount of pipes that should have rounded corners.',
		subtype = 'PERCENTAGE',
		min = 0,
		max = 100,
		default = default['bevel']
	)

	surface = IntProperty(
		name = 'Surface',
		description = 'The surface resolution of the pipes.',
		min = 0,
		max = 32,
		default = default['surface']
	)

	seed = IntProperty(
		name = 'Seed',
		description = 'The seed random basis for generating pipes.',
		default = default['seed']
	)

	convert = BoolProperty(
		name = 'Convert to Mesh',
		description = 'Convert the generated pipes into a single mesh object.',
		default = default['convert']
	)

	create_empty = BoolProperty(
		name = 'Create Empty',
		description = 'Create an empty as the parent for all the pipes. (Slower but allows for easier control)',
		default = default['create_empty']
	)

	hide_lines = BoolProperty(
		name = 'Hide Relationship Lines',
		description = 'Hide parent relationship lines in the 3D view.',
		default = default['hide_lines']
	)


	def check(self, context):

		return True


	def draw(self, context):

		interface.operator(self, context)


	def execute(self, context):

		generate(self, context)

		return {'FINISHED'}
