#!/usr/bin/env python
#import jnius_config
#jnius_config.set_classpath('.', 'lib/*')

from jnius import (
  cast,
  autoclass,
  java_method,
  PythonJavaClass
)

from plyer.platforms.android import activity

#List = autoclass('java.util.List')
#BufferReader = autoclass('java.io.BufferedReader')
#FileReader = autoclass('java.io.FileReader')
#IOException = autoclass('java.io.IOException')
#Method = autoclass('java.lang.reflect.Method')
#Inet4Address = autoclass('java.net.Inet4Address')
#Intet6Address = autoclass('java.net.Inet6Address')
#InetAddress = autoclass('java.net.InetAddress')
#NetworkInterface = autoclass('java.net.NetworkInterface')
#ArrayList = autoclass('java.util.ArrayList')
#Arrays = autoclass('java.util.Arrays')
#Enumeration = autoclass('java.util.Enumeration')
#Pattern = autoclass('java.util.regex.Pattern')
#CountDownLatch = autoclass('java.util.concurrent.CountDownLatch')
#ExecutorService = autoclass('java.util.concurrent.ExecutorService')
#Executors = autoclass('java.util.concurrent.Executors')
#InvocationTargetException = autoclass('java.lang.reflect.InvocationTargetException')

Context = autoclass('android.content.Context')
WifiManager = autoclass('android.net.wifi.WifiManager')


class WiFiApControl(PythonJavaClass):

  __javainterfaces__ = ['java/util/ListIterator']

  WIFI_AP_STATE_DISABLING = 10
  WIFI_AP_STATE_DISABLED  = 11
  WIFI_AP_STATE_ENABLING  = 12
  WIFI_AP_STATE_ENABLED   = 13
  WIFI_AP_STATE_FAILED    = 14

  STATE_DISABLING = WIFI_AP_STATE_DISABLING
  STATE_DISABLED  = WIFI_AP_STATE_DISABLED
  STATE_ENABLING  = WIFI_AP_STATE_ENABLING
  STATE_ENABLED   = WIFI_AP_STATE_ENABLED
  STATE_FAILED    = WIFI_AP_STATE_FAILED

  def __init__(self):
    super(WiFiApControl, self).__init__()
    service = activity.getSystemService(Context.WIFI_SERVICE)
    self.WiFiManager = cast('android.net.wifi.WifiManager', service)
    self.methods = {
        'getWifiApConfiguration': None,
        'getWifiApState': None,
        'isWifiApEnabled': None,
        'setWifiApEnabled': None
    }

    for method in self.WiFiManager.getClass().getDeclaredMethods():
        method_name = method.getName()
        if method_name in self.methods:
            self.methods[method_name] = method


if __name__ == '__main__':
  ap = WiFiApControl()
