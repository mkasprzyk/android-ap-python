#!/usr/bin/env python

from jnius import (
  cast,
  reflect,
  autoclass,
  JavaMethod,
  PythonJavaClass
)

jnius.reflect.Method.invoke = JavaMethod('(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;')

Context = autoclass('android.content.Context')
WifiManager = autoclass('android.net.wifi.WifiManager')

from plyer.platforms.android import activity



class WiFiApControl(PythonJavaClass):

  __javainterfaces__ = ['java/util/ListIterator']

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

  def isWiFiApEnabled(self):
    result = self.methods['isWifiApEnabled'].invoke(self.WiFiManager, None)
    return result


if __name__ == '__main__':
  ap = WiFiApControl()
