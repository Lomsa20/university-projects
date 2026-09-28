class Device:
    def __init__(self, _id):
        self._id = _id
        self._status = False
    @property
    def id(self):
        return self._id
    @property
    def status(self):
        return self._status
    def turn_on(self):
        self._status = True
    def turn_off(self):
        self._status = False
    def __str__(self):
        state = 'On'if self._status else 'Off'
        return f'ID: {self._id} Status: {state}'
class Light(Device):
    pass
class Thermostat(Device):
    pass
class Camera(Device):
    pass
class Room:
    def __init__(self, name):
        self._name = name
        self._devices = []
    @property
    def devices(self):
        return self._devices
    def add_device(self, device):
        if not isinstance(device, Device):
            raise TypeError('Device must be of type Device')
        if device not in self._devices:
            self._devices.append(device)
    def remove_device(self, device):
        if device in self._devices:
            self._devices.remove(device)
    def turn_all_on(self):
        for d in self._devices:
            d.turn_on()
    def turn_all_off(self):
        for d in self._devices:
            d.turn_off()
    def __str__(self):
        dev = ', '.join(str(d) for d in self._devices)
        return (
                f"Id: {self._name} "
                f"\nDevice: {dev}"
                )
class SmartHouse:
    def __init__(self):
        self._rooms = []
    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError('Room must be of type Room')
        if room not in self._rooms:
            self._rooms.append(room)
    def remove_room(self, room):
        if room in self._rooms:
            self._rooms.remove(room)
    def turn_device_on(self):
        for room in self._rooms:
            room.turn_on()
    def turn_device_off(self):
        for room in self._rooms:
            room.turn_off()
    def turn_all_devices_on(self):
        for room in self._rooms:
            room.turn_all_on()
    def turn_all_devices_off(self):
        for room in self._rooms:
            room.turn_all_off()
    def show_status(self):
        for room in self._rooms:
            print(room)
            print('-'*30)
living_room = Room("Living Room")
living_room.add_device(Light("L1"))
living_room.add_device(Thermostat("T1"))
living_room.add_device(Camera("C1"))

bedroom = Room("Bedroom")
bedroom.add_device(Light("L2"))
bedroom.add_device(Camera("C2"))

house = SmartHouse()
house.add_room(living_room)
house.add_room(bedroom)

print("=== Initial Status ===")
house.show_status()

print("=== Turn All Devices On ===")
house.turn_all_devices_on()
house.show_status()

print("=== Turn All Devices Off ===")
house.turn_all_devices_off()
house.show_status()