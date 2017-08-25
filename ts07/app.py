# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from logging import getLogger
from concurrent.futures import ThreadPoolExecutor, as_completed

log = getLogger(__name__)

from .bottle import route, run
from .ufo import Ufo
from .phue import Bridge


hue_ip = '10.0.1.103'
ufo_ceiling_1 = '10.0.1.111'
ufo_under_bar = '10.0.1.112'
ufo_under_cabinets = '10.0.1.113'
ufo_back_bar_1 = '10.0.1.114'


def execute_tasks(tasks):
    executor = ThreadPoolExecutor(10)
    futures = (executor.submit(task[0], *task[1]) for task in tasks)
    result = tuple(future.result() for future in as_completed(futures))
    executor.shutdown(wait=True)


@route('/set_red')
def set_red():
    b = Bridge(hue_ip)
    def set_hue_red(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 0
        light.saturation = 255
        light.brightness = 160

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 0, 0, 0).on(), ()),
        (set_hue_red, (0,)),
        (set_hue_red, (1,)),
    )
    execute_tasks(tasks)


@route('/set_green')
def set_green():
    b = Bridge(hue_ip)
    def set_hue_green(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 0
        light.saturation = 255
        light.brightness = 160

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(0, 255, 0, 0).on(), ()),
        (set_hue_green, (0,)),
        (set_hue_green, (1,)),
    )
    execute_tasks(tasks)


@route('/set_blue')
def set_blue():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 43690
        light.saturation = 255
        light.brightness = 92

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 0, 128, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 0, 128, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(0, 0, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(0, 0, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
    )
    execute_tasks(tasks)


@route('/set_light_blue')
def set_light_blue():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 43690
        light.saturation = 255
        light.brightness = 92

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(155, 155, 255, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(129, 129, 192, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(155, 155, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(155, 155, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
    )
    execute_tasks(tasks)


@route('/set_white')
def set_white():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 37736
        light.saturation = 230
        light.brightness = 255

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 0, 0, 192).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 0, 0, 192).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 255, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 255, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
    )
    execute_tasks(tasks)


@route('/set_off')
def set_off():
    b = Bridge(hue_ip)
    def set_hue_off(light_id):
        light = b.lights[light_id]
        light.on = False

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).off(), ()),
        (lambda: Ufo(ufo_under_bar).off(), ()),
        (lambda: Ufo(ufo_under_cabinets).off(), ()),
        (lambda: Ufo(ufo_back_bar_1).off(), ()),
        (set_hue_off, (0,)),
        (set_hue_off, (1,)),
    )
    execute_tasks(tasks)


if __name__ == "__main__":
    run(host='localhost', port=3607)
