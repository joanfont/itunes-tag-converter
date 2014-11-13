import sys
from xml.dom import minidom
from pprint import pprint

if __name__ == '__main__':
	if len(sys.argv) >= 2:
		library = sys.argv[1]
		#TODO: add file verification
		xml_library = minidom.parse(library)
	else:
		print 'Usage: python converter.py itunes_library.xml'

