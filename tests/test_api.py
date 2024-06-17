from pprint import pp

from unittest import TestCase

from music_link_conv import Music_Link_Conv


class Test_Types_Serialization(TestCase):
	__API = Music_Link_Conv(
		spotify_client_id = 'c6b23f1e91f84b6a9361de16aba0ae17',
		spotify_client_secret = '237e355acaa24636abc79f1a089e6204'
	)


	def test_spo_track_2_dee_track(self):
		links = ('1VK5JYdgrJZENDl1taa2cS', '11dFghVXANMlKmJXsNCbNl')
		result = (None, 'https://www.deezer.com/track/363747251')

		for i, link in enumerate(links):
			link = self.__API.conv_spo_track_2_deezer_track(link)
			assert link == result[i]


	def test_spo_album_2_dee_album(self):
		links = ('58syBUrmo8UCiWFF2BuszZ', '1XXSHevNKbENDXqH5iRSEC', '6G0POeSml1dY0l8SuvhY6s')
		result = ('https://www.deezer.com/album/171125712', None, 'https://www.deezer.com/album/48667542')

		for i, link in enumerate(links):
			link = self.__API.conv_spo_album_2_deezer_album(link)
			assert link == result[i]
