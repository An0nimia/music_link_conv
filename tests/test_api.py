from unittest import TestCase

from music_link_conv import Music_Link_Conv


class Test_Types_Serialization(TestCase):
	# trunk-ignore(bandit/B106)
	__API = Music_Link_Conv(
		spotify_client_id = 'c6b23f1e91f84b6a9361de16aba0ae17',
		spotify_client_secret = '237e355acaa24636abc79f1a089e6204' # trunk-ignore(gitleaks/generic-api-key)
	)


	def test_spo_track_2_dee_track(self):
		links = ('1VK5JYdgrJZENDl1taa2cS', '11dFghVXANMlKmJXsNCbNl')
		result = (None, 'https://www.deezer.com/track/363747251')

		for i, link in enumerate(links):
			link = self.__API.conv_spo_track_2_dee_track(link)
			assert link == result[i] # trunk-ignore(bandit/B101)


	def test_spo_album_2_dee_album(self):
		links = ('58syBUrmo8UCiWFF2BuszZ', '1XXSHevNKbENDXqH5iRSEC', '6G0POeSml1dY0l8SuvhY6s')
		result = ('https://www.deezer.com/album/171125712', None, 'https://www.deezer.com/album/48667542')

		for i, link in enumerate(links):
			link = self.__API.conv_spo_album_2_dee_album(link)
			assert link == result[i] # trunk-ignore(bandit/B101)


	def test_spo_artist_2_dee_artist(self):
		links = ('2hhLQDmEJqObRlCHWbyeQF', '1U0dn9EFyhTfKS4xvFrUSR')
		result = ('https://www.deezer.com/artist/10091060', 'https://www.deezer.com/artist/14081395')

		for i, link in enumerate(links):
			link_dee = self.__API.conv_spo_artist_2_dee_artist(link)

			assert link_dee == result[i] # trunk-ignore(bandit/B101)
