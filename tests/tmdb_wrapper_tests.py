from tmdbwrapper import tv
from pytest import fixture
import vcr


@fixture
def tv_info_keys():
    return ['episode_run_time', 'backdrop_path']


@vcr.use_cassette('tests/vcr_cassettes/tv-info.yml')
def tv_info_test():
    tv_instance = tv.TV(1396)
    response = tv_instance.info()
    #tests to pass
    assert isinstance(response, dict)
    assert response["id"] == 1396
    assert set(tv_info_keys()).issubset(response.keys())


def tv_credits_test():
    tv_instance = tv.TV(1396)
    response = tv_instance.credits()
    #tests to pass
    assert isinstance(response, dict)
    assert response["id"] == 1396
    assert set(["cast", "crew"]).issubset(response.keys())

tv_info_test()
tv_credits_test()
