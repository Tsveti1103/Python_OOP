class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.express_software_count = 0
        self.light_software_count = 0

    def install(self, software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        self.software_components.remove(software)
        if software.software_type == "Express":
            self.express_software_count -= 1
        else:
            self.light_software_count -= 1

    def total_memory_consumption(self):
        return sum(software.memory_consumption for software in self.software_components)

    def total_capacity_consumption(self):
        return sum(software.capacity_consumption for software in self.software_components)
