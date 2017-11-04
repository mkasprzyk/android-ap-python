#!/usr/bin/env python


from jnius import (
  cast,
  reflect,
  autoclass,
  JavaMethod,
  java_method,
  PythonJavaClass
)

reflect.Method.invoke = JavaMethod('(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;')

Boolean = autoclass('java.lang.Boolean')
Context = autoclass('android.content.Context')
WifiManager = autoclass('android.net.wifi.WifiManager')

from plyer.platforms.android import activity



class WiFiApControl(PythonJavaClass):

  __javainterfaces__ = ['java/util/ListIterator']

  
  AP_STATE = 'getWifiApState'
  AP_ENABLED = 'isWifiApEnabled'
  AP_CONFIGURATION = 'getWifiApConfiguration'
  SET_AP_CONFIGURATION = 'setWifiApConfiguration'
  SET_AP_ENABLED = 'setWifiApEnabled'

  def __init__(self):

    super(WiFiApControl, self).__init__()
    service = activity.getSystemService(Context.WIFI_SERVICE)
    self.WiFiManager = cast('android.net.wifi.WifiManager', service)
    self.methods = {
        self.AP_CONFIGURATION: None,
        self.AP_STATE: None,
        self.AP_ENABLED: None,
        self.SET_AP_ENABLED: None,
        self.SET_AP_CONFIGURATION: None
    }

    for method in self.WiFiManager.getClass().getDeclaredMethods():
        method_name = method.getName()
        if method_name in self.methods:
            self.methods[method_name] = method

  def _invoke(self, method, args=None):
    return self.methods[method].invoke(self.WiFiManager, args)

  def enabled(self):
    return self._invoke(self.AP_ENABLED)

  def change_state(self, configuration, enabled):
    return self._invoke(self.SET_AP_ENABLED, (configuration, Boolean(enabled),))

  def state(self):
    return self._invoke(self.AP_STATE)

  def configuration(self):
    return self._invoke(self.AP_CONFIGURATION)

  def set_configuration(self, configuration):
    return self._invoke(self.SET_AP_CONFIGURATION, (configuration,))
    

if __name__ == '__main__':
  ap = WiFiApControl()
