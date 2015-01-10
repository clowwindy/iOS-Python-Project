#!/usr/bin/env python

# Copyright (c) 2014 clowwindy
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import absolute_import, division, print_function, \
  with_statement

import threading
import sys
from ctypes import cdll
from ctypes import util
from ctypes import CDLL, c_char_p, c_int, c_long, byref,\
  create_string_buffer, c_void_p
from rubicon.objc import ObjCClass, objc_method
from rubicon.objc.core_foundation import from_value, to_value

from myapp import web


UIKit = cdll.LoadLibrary(util.find_library('UIKit'))
UIKit.UIApplicationMain.restypes = (c_int, c_void_p, c_void_p,
                                    c_void_p)
UIKit.UIApplicationMain.restype = c_int
NSObject = ObjCClass("NSObject")


class MyAppDelegate(NSObject):
  @objc_method('@B')
  def application_didFinishLaunchingWithOptions_(self, launchOptions):
    # You can't store attributes directly on the object -
    # you need to put them manually on the Python object
    
    server_thread = threading.Thread(target=web.run_server)
    server_thread.start()
    return 0

if __name__ == '__main__':
  sys.exit(UIKit.UIApplicationMain(0, None, None, from_value('MyAppDelegate')))
