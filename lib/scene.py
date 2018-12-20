print('scene.py loading...')

class Scene:
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.ownerComp.par.parentshortcut = 'Scene'
		self._InitParams()

	def _InitParams(self):
		page = self.ownerComp.appendCustomPage('Scene')
		p = page.appendToggle('Active')[0]
		p.default = True
		p = page.appendFloat('Fade')[0]
		p.min, p.max = 0, 1
		p.clampMin = p.clampMax = True
		p.default = 1
		page.appendPulse('Reset')
