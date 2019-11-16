#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<pre>Hello, world. You're at the teammate index</pre>")
