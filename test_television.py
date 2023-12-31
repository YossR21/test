import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv_on = Television()
    tv_on.power()
    assert str(tv_on) == "Power = True, Channel = 0, Volume = 0"

    tv_off = Television()
    assert str(tv_off) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.unmute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    tv.unmute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.power()
    tv.mute()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

def test_channel_up():
    tv_off = Television()
    tv_off.channel_up()
    assert str(tv_off) == "Power = False, Channel = 0, Volume = 0"

    tv_on = Television()
    tv_on.power()
    tv_on.channel_up()
    assert str(tv_on) == "Power = True, Channel = 1, Volume = 0"

    tv_on_max_channel = Television()
    tv_on_max_channel.power()
    tv_on_max_channel.channel_up()
    tv_on_max_channel.channel_up()
    tv_on_max_channel.channel_up()
    tv_on_max_channel.channel_up()
    assert str(tv_on_max_channel) == "Power = True, Channel = 0, Volume = 0"

def test_channel_down():
    tv_off = Television()
    tv_off.channel_down()
    assert str(tv_off) == "Power = False, Channel = 0, Volume = 0"

    tv_on = Television()
    tv_on.power()
    tv_on.channel_down()
    assert str(tv_on) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up():
    tv_off = Television()
    tv_off.volume_up()
    assert str(tv_off) == "Power = False, Channel = 0, Volume = 0"

    tv_on = Television()
    tv_on.power()
    tv_on.volume_up()
    assert str(tv_on) == "Power = True, Channel = 0, Volume = 1"

    tv_on_muted = Television()
    tv_on_muted.power()
    tv_on_muted.mute()
    tv_on_muted.volume_up()
    assert str(tv_on_muted) == "Power = True, Channel = 0, Volume = 1"

    tv_on_max_volume = Television()
    tv_on_max_volume.power()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_up()
    assert str(tv_on_max_volume) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv_off = Television()
    tv_off.volume_down()
    assert str(tv_off) == "Power = False, Channel = 0, Volume = 0"

    tv_on = Television()
    tv_on.power()
    tv_on.volume_down()
    assert str(tv_on) == "Power = True, Channel = 0, Volume = 0"

    tv_on_max_volume = Television()
    tv_on_max_volume.power()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_up()
    tv_on_max_volume.volume_down()
    assert str(tv_on_max_volume) == "Power = True, Channel = 0, Volume = 2"

    tv_on_muted = Television()
    tv_on_muted.power()
    tv_on_muted.mute()
    tv_on_muted.volume_down()
    assert str(tv_on_muted) == "Power = True, Channel = 0, Volume = 0"

    tv_on_min_volume = Television()
    tv_on_min_volume.power()
    tv_on_min_volume.volume_down()
    tv_on_min_volume.volume_down()
    tv_on_min_volume.volume_down()
    assert str(tv_on_min_volume) == "Power = True, Channel = 0, Volume = 0"
