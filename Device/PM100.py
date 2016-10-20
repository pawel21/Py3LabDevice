from IODevice import IODevice, BadDeviceException


class PM100:
    def __init__(self, usb_port):
        try:
            self.device = IODevice(usb_port)
            self._check_if_device_is_correct()
        except BadDeviceException:
            print("Bad device. This is not PM100")

    def _check_if_device_is_correct(self):
        correct_name = b'Thorlabs,PM100USB,P2001205,1.3.0\n'
        device_name = self.device.get_name()
        if correct_name != device_name:
            raise BadDeviceException

    def get_current_wavelength_in_nm(self):
        self.device.write("CORRection:WAVelength? ")
        current_wavelength = self.device.read(100)
        return float(current_wavelength)

    def set_wavelength_in_nm(self, value):
        self.device.write("CORRection:WAVelength " + str(value))

    def get_power(self):
        self.device.write("INITiate")
        self.device.write("MEASure:POWer")
        self.device.write("FETCh?")
        value = self.device.read(100)
        return float(value)