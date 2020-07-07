from typing import Tuple


class IdTools:
    base_url = 'https://www.webnovel.com/book/'

    @staticmethod
    def to_novel_url(novel_id):
        """
        :return: novel url
        """
        return f'{IdTools.base_url}/{novel_id}'

    @staticmethod
    def from_novel_url(novel_url):
        """
        :return: url of novel
        """
        return int(novel_url.split('/')[4])

    @staticmethod
    def to_chapter_url(novel_id, chapter_id):
        """
        :return: chapter url
        """
        return f'{IdTools.base_url}/{novel_id}/{chapter_id}'

    @staticmethod
    def from_chapter_url(chapter_url) -> Tuple[int, int]:
        """
        :return: novel_id, chapter_id
        """
        pieces = chapter_url.split('/')
        return int(pieces[4]), int(pieces[5])

    @staticmethod
    def to_profile_url(profile_id):
        """
        :return: profile url
        """
        return f'https://www.webnovel.com/profile/{profile_id}?appId=10'

    @staticmethod
    def from_profile_url(profile_url):
        """
        :return: profile id
        """
        return int(profile_url.split('/')[4].split('?')[0])