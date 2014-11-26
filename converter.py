import sys
import os
from urllib import unquote

import plistop
import eyed3


n_items = 0
processed_items = 0

def get_library_songs(library):

	with open(library) as f:
		plist = plistop.parse(f)

	return plist.get('Tracks').itervalues()

def change_track_tags(item):

	def _get_location(item):
		return unquote(item.get('Location')[7:])

	def _set(item, key):
		return u'%s' % item.get(key)

	def _get_percentage(processed_items):

		percentage = (processed_items / n_items) * 100.0
		return 'Processed %s out of %s (%3.2f)' % (processed_items, n_items, percentage)

	global processed_items

	path = _get_location(item)
	song = eyed3.load(path)

	song.tag.title = _set(item, 'Name')
	song.tag.artist = _set(item, 'Artist')
	song.tag.album = _set(item, 'Album')
	song.tag.track_num = (item.get('Track Number',0),None)

	song.tag.save()

	processed_items += 1

	print _get_percentage(processed_items)

if __name__ == '__main__':

	if len(sys.argv) >= 2:
		library = sys.argv[1]
		if os.path.isfile(library):
			library_items = list(get_library_songs(library))
			n_items = len(library_items)
			map(change_track_tags,library_items)
		else:
			print 'File \'%s\' does not exist' % library
	else:
		print 'Usage: python converter.py itunes_library.xml'

