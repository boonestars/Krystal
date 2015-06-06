from distutils.core import setup
import py2exe
setup(
	options= {
		'build': {'build_base': 'c:/FSSM'},
		'py2exe': {
			"dll_excludes":[ "mswsock.dll", "powrprof.dll", "w9xpopen.exe" ],
			"bundle_files": 1,
			"compressed": True }},
	windows = [{'script': "FSSM.py"}],
	zipfile = None,
	)