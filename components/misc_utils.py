def setUpTox(comp, dir1, dir2=None, omitclone=False):
	if not omitclone:
		comp.par.clone.expr = "op({!r}) or ''".format(comp.path)
	toxname = comp.name + '.tox'
	if not dir1:
		dir1 = ''
	elif not dir1.endswith('/'):
		dir1 += '/'
	pathexpr = "'{1}{0}' if mod.os.path.exists('{1}{0}') else ".format(toxname, dir1)
	if dir2:
		if not dir2.endswith('/'):
			dir2 += '/'
		pathexpr += "('{1}{0}' if mod.os.path.exists('{1}{0}') else '')".format(toxname, dir2)
	else:
		pathexpr += "''"
	if not omitclone:
		pathexpr = "'' if me.par.clone.eval() not in (me, None, '') else ({0})".format(pathexpr)
	comp.par.externaltox.expr = pathexpr
