import fnmatch
import os
from IODevice import IODevice
from LDC4005 import LDC4005
from PM100 import PM100

class DeviceFactory:
    def create_virtual_device(self, name):
        pass

class Device:
    _PATH_TO_DEV_DIR="/dev"
    map_device = {}
    available_port = ["/dev/usbtmc0", "/dev/usbtmc1"]

    def available_device(self):
        list_of_path_usb_device = self._create_list_of_usb_device()
        for path_usb_device in list_of_path_usb_device:
            self.map_device[path_usb_device] = (IODevice(path_usb_device).get_name())
        return self.map_device

    def _create_list_of_usb_device(self):
        list_of_device = os.listdir(self._PATH_TO_DEV_DIR)
        list_of_path_usb_device = []
        for device in list_of_device:
            if fnmatch.fnmatch(device, 'usb*'):
                list_of_path_usb_device.append(os.path.join(self._PATH_TO_DEV_DIR, device))
        return list_of_path_usb_device

    def get_ldc4005_instance(self):
        map_of_available_device = self.available_device()
        for port in self.available_port:
            if b"LDC4005" in map_of_available_device[port]:
                return LDC4005(port)

    def get_pm100_instance(self):
        map_of_available_device = self.available_device()
        for port in self.available_port:
            if b"PM100" in map_of_available_device[port]:
                return PM100(port)

dev = Device()
dev.available_device()
ldc = dev.get_ldc4005_instance()
print(ldc)
