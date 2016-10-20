import sys
sys.path.insert(0, "/home/pawel1/Pulpit/PyLabDevice/Py3LabDevice/Device")

from Device import Device

dev = Device()
print(dev.available_device())
ldc = dev.get_ldc4005_instance()