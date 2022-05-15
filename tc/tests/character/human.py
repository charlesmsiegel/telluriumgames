from django.test import TestCase


# Create your tests here.
class TestHuman(TestCase):
    # add_X
    # has_X
    # filter_X
    
    # assign derived values
    # test special cases
    
    # get_absolute_url
    pass


class TestRandomHuman(TestCase):
    # test_random_X for X a thing
    # test_random
    pass


class TestHumanDetailView(TestCase):
    # test_X_detail_view_status_code
    # test_X_detail_view_template
    pass


class CharacterDetailView(TestCase):
    # test_character_detail_view_status_code for each character type
    # test_character_detail_view_templates for each character type
    pass


class TestIndexView(TestCase):
    # test_index_status_code
    # test_index_template
    # test_index_post
    pass
