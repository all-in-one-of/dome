def setUpTox(comp, optionaldir=None):
	comp.par.clone.expr = "op({!r}) or ''".format(comp.path)
	toxname = comp.name + '.tox'
	pathexpr = "'{0}' if mod.os.path.exists('{0}') else ".format(toxname)
	if optionaldir:
		if not optionaldir.endswith('/'):
			optionaldir += '/'
		pathexpr += "('{1}{0}' if mod.os.path.exists('{1}{0}') else '')".format(toxname, optionaldir)
	else:
		pathexpr += "''"
	pathexpr = "'' if me.par.clone.eval() not in (me, None, '') else ({0})".format(pathexpr)
	comp.par.externaltox.expr = pathexpr