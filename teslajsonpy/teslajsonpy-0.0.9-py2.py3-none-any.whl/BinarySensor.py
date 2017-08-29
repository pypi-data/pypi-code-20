from teslajsonpy.vehicle import VehicleDevice


class ParkingSensor(VehicleDevice):
    def __init__(self, data, controller):
        VehicleDevice.__init__(self, data, controller)
        self.__id = data['id']
        self.__vehicle_id = data['vehicle_id']
        self.__vin = data['vin']
        self.__controller = controller
        self.__state = False

        self.type = 'parking sensor.'
        self.hass_type = 'binary_sensor'

        self.name = 'Tesla model {} {}'.format(
            str(self.__vin[3]).upper(), self.type)

        self.uniq_name = 'Tesla model {} {} {}'.format(
            str(self.__vin[3]).upper(), self.__vin, self.type)

        self.update()

    def update(self):
        self.__controller.update(self.__id)
        data = self.__controller.get_drive_params(self.__id)
        if not data['shift_state'] or data['shift_state'] == 'P':
            self.__state = True
        else:
            self.__state = False

    def get_value(self):
        return self.__state

    @staticmethod
    def has_battery():
        return False


class ChargerConnectionSensor(VehicleDevice):
    def __init__(self, data, controller):
        VehicleDevice.__init__(self, data, controller)
        self.__id = data['id']
        self.__vehicle_id = data['vehicle_id']
        self.__vin = data['vin']
        self.__controller = controller
        self.__state = False

        self.type = 'charger sensor.'
        self.hass_type = 'binary_sensor'
        self.name = 'Tesla model {} {}'.format(
            str(self.__vin[3]).upper(), self.type)

        self.uniq_name = 'Tesla model {} {} {}'.format(
            str(self.__vin[3]).upper(), self.__vin, self.type)

        self.update()

    def update(self):
        self.__controller.update(self.__id)
        data = self.__controller.get_charging_params(self.__id)
        if data['charging_state'] in ["Disconnected", "Stopped", "NoPower"]:
            self.__state = False
        else:
            self.__state = True

    def get_value(self):
        return self.__state

    @staticmethod
    def has_battery():
        return False
