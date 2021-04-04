# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
from logging import getLogger
from concurrent.futures import ThreadPoolExecutor, as_completed

from .bottle import response, route, run, redirect
from .ufo import Ufo
from .phue import Bridge

log = getLogger(__name__)

hue_ip = '10.0.1.103'
ufo_ceiling_1 = '10.0.1.111'
ufo_under_bar = '10.0.1.112'
ufo_under_cabinets = '10.0.1.113'
ufo_back_bar_1 = '10.0.1.114'
ufo_ceiling_2 = '10.0.1.200'

# hue notes:
#  hue has max 65536
#  saturation has max 254
#  brightness has max 254


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
        light.hue = 430
        light.saturation = 252
        light.brightness = 252

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 0, 0, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 0, 0, 0).on(), ()),
        (set_hue_red, (0,)),
        (set_hue_red, (1,)),
        (set_hue_red, (2,)),
        (set_hue_red, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_green')
def set_green():
    b = Bridge(hue_ip)
    def set_hue_green(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 25699
        light.saturation = 254
        light.brightness = 253

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(0, 255, 0, 0).on(), ()),
        (set_hue_green, (0,)),
        (set_hue_green, (1,)),
        (set_hue_green, (2,)),
        (set_hue_green, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_green_purple')
def set_green_purple():
    b = Bridge(hue_ip)
    def set_hue_green(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 25699
        light.saturation = 254
        light.brightness = 253

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(128, 0, 128, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(0, 255, 0, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 0, 255, 0).on(), ()),
        (set_hue_green, (0,)),
        (set_hue_green, (1,)),
        (set_hue_green, (2,)),
        (set_hue_green, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_blue')
def set_blue():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 47112
        light.saturation = 253
        light.brightness = 252

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 0, 80, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(0, 0, 80, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 0, 128, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(0, 0, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(0, 0, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
        (set_hue_blue, (2,)),
        (set_hue_blue, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_purple')
def set_purple():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 52957
        light.saturation = 253
        light.brightness = 252

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(80, 0, 80, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(80, 0, 80, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(128, 0, 128, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 0, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 0, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
        (set_hue_blue, (2,)),
        (set_hue_blue, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_light_blue')
def set_light_blue():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 42690
        light.saturation = 216
        light.brightness = 254

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(155, 155, 255, 0).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(155, 155, 255, 0).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(129, 129, 192, 0).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(155, 155, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(155, 155, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
        (set_hue_blue, (2,)),
        (set_hue_blue, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_white')
def set_white():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 38373
        light.saturation = 254
        light.brightness = 254

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(0, 0, 0, 192).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(0, 0, 0, 192).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(0, 0, 0, 192).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 255, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 255, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
        (set_hue_blue, (2,)),
        (set_hue_blue, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_bright_white')
def set_bright_white():
    b = Bridge(hue_ip)
    def set_hue_blue(light_id):
        light = b.lights[light_id]
        light.on = True
        light.hue = 38373
        light.saturation = 254
        light.brightness = 254

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).rgbw(255, 255, 255, 255).on(), ()),
        (lambda: Ufo(ufo_ceiling_2).rgbw(255, 255, 255, 255).on(), ()),
        (lambda: Ufo(ufo_under_bar).rgbw(255, 255, 255, 255).on(), ()),
        (lambda: Ufo(ufo_under_cabinets).rgbw(255, 255, 255, 0).on(), ()),
        (lambda: Ufo(ufo_back_bar_1).rgbw(255, 255, 255, 0).on(), ()),
        (set_hue_blue, (0,)),
        (set_hue_blue, (1,)),
        (set_hue_blue, (2,)),
        (set_hue_blue, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/set_off')
def set_off():
    b = Bridge(hue_ip)
    def set_hue_off(light_id):
        light = b.lights[light_id]
        light.on = False

    tasks = (
        (lambda: Ufo(ufo_ceiling_1).off(), ()),
        (lambda: Ufo(ufo_ceiling_2).off(), ()),
        (lambda: Ufo(ufo_under_bar).off(), ()),
        (lambda: Ufo(ufo_under_cabinets).off(), ()),
        (lambda: Ufo(ufo_back_bar_1).off(), ()),
        (set_hue_off, (0,)),
        (set_hue_off, (1,)),
        (set_hue_off, (2,)),
        (set_hue_off, (3,)),
    )
    execute_tasks(tasks)
    redirect("/")


@route('/get_status')
def get_status():
    b = Bridge(hue_ip)
    def get_hue_status(light_id):
        light = b.lights[light_id]
        builder = []
        builder.append("hue id: %s" % light_id)
        builder.append("  power: %s" % ("on" if light.on else "off"))
        builder.append("  hue: %s" % light.hue)
        builder.append("  saturation: %s" % light.saturation)
        builder.append("  brightness: %s" % light.brightness)
        builder.append("")
        return '\n'.join(builder)

    result = Ufo.all_status()
    result += get_hue_status(0)
    result += get_hue_status(1)
    result += get_hue_status(2)
    result += get_hue_status(3)
    response.content_type = 'text/plain'
    return result


@route('/')
def index():
    response.content_type = 'text/html; charset=latin9'
    return index_html


index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/superhero/bootstrap.min.css">
  </head>
  <body>

<div class="container-fluid">
  <a href="/set_off" class="btn btn-outline-primary btn-lg btn-block">Off</a>
  <a href="/set_white" class="btn btn-primary btn-lg btn-block" style="background-color: #fff; color: #000; font-weight: bold;">White</a>
  <a href="/set_blue" class="btn btn-primary btn-lg btn-block" style="background-color: #00f; font-weight: bold;">Blue</a>
  <a href="/set_purple" class="btn btn-primary btn-lg btn-block" style="background-color: #f0f; font-weight: bold;">Purple</a>
  <a href="/set_green" class="btn btn-primary btn-lg btn-block btn-success" style="font-weight: bold;">Green</a>
  <a href="/set_light_blue" class="btn btn-primary btn-lg btn-block btn-info" style="font-weight: bold;">Light Blue</a>
  <a href="/set_red" class="btn btn-primary btn-lg btn-block btn-danger" style="font-weight: bold;">Red</a>
  <a href="/set_green_purple" class="btn btn-primary btn-lg btn-block btn-success" style="color: #f0f; font-weight: bold;">Green + Purple</a>
  <a href="/set_bright_white" class="btn btn-primary btn-lg btn-block" style="background-color: #fff; color: #000; font-weight: bold;">Bright White</a>
</div>

  </body>
</html>
"""


if __name__ == "__main__":
    run(host='0.0.0.0', port=3607, debug=True)
