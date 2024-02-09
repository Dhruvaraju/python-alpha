class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name} {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print(f"{self.name} has disconnected.")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        print(f"{super().__str__()} {self.remaining_pages} pages")

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected.")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

    def refill(self):
        self.remaining_pages = self.capacity
        print(f"Your printer has been refilled.")

office_printer = Printer("Printer", "USB", 500)
office_printer.__str__()
office_printer.print(100)
office_printer.__str__()
office_printer.disconnect()
office_printer.print(100)