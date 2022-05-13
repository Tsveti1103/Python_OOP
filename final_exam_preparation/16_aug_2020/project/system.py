from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new = PowerHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new = HeavyHardware(name, capacity, memory)
        System._hardware.append(new)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        hardware = System.find_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)
        hardware.express_software_count += 1

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        hardware = System.find_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)
        hardware.light_software_count += 1

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_by_name(hardware_name, System._hardware)
        software = System.find_by_name(software_name, System._software)
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum(hardware.memory for hardware in System._hardware)
        total_memory_consumption = sum(hardware.total_memory_consumption() for hardware in System._hardware)
        total_capacity = sum(hardware.capacity for hardware in System._hardware)
        total_capacity_consumption = sum(hardware.total_capacity_consumption() for hardware in System._hardware)
        return f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_memory_consumption} / {total_memory}\n" \
               f"Total Capacity Taken: {total_capacity_consumption} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            if not hardware.software_components:
                hardware.software_components.append("None")
            result += f"Hardware Component - {hardware.name}\n" \
                      f"Express Software Components: {hardware.express_software_count}\n" \
                      f"Light Software Components: {hardware.light_software_count}\n" \
                      f"Memory Usage: {hardware.total_memory_consumption()} / {hardware.memory}\n" \
                      f"Capacity Usage: {hardware.total_capacity_consumption()} / {hardware.capacity}\n" \
                      f"Type: {hardware.hardware_type}\n" \
                      f"Software Components: {', '.join([software.name for software in hardware.software_components])}\n"
        return result.strip()

    @staticmethod
    def find_by_name(name, all_obj):
        for obj in all_obj:
            if obj.name == name:
                return obj
