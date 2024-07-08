# examples for system.

from TeamDominationClasses import Vehicle, Maintenance, CallSchedule, FleetManagementSystem

# Create a fleet management system
fms = FleetManagementSystem()

# Add vehicles
vehicle1 = Vehicle(vehicle_id="V001", make="Ford", model="Transit", year=2020)
vehicle2 = Vehicle(vehicle_id="V002", make="Chevrolet", model="Express", year=2019)
fms.add_vehicle(vehicle1)
fms.add_vehicle(vehicle2)

# Add maintenance records
maintenance1 = Maintenance(date="2024-07-10", description="Oil Change")
maintenance2 = Maintenance(date="2024-07-20", description="Tire Rotation")
fms.add_maintenance_record(vehicle_id="V001", maintenance=maintenance1)
fms.add_maintenance_record(vehicle_id="V001", maintenance=maintenance2)

# Add call schedules
call_schedule1 = CallSchedule(call_id="C001", customer_name="John Doe", date="2024-07-15", time="09:00 AM")
call_schedule2 = CallSchedule(call_id="C002", customer_name="Jane Smith", date="2024-07-16", time="10:00 AM")
fms.add_call_schedule(call_schedule1)
fms.add_call_schedule(call_schedule2)

# Assign vehicle to call
fms.assign_vehicle_to_call(call_id="C001", vehicle_id="V001")

# Remove a maintenance record
fms.remove_maintenance_record(vehicle_id="V001", maintenance=maintenance1)

# Remove a call schedule
fms.remove_call_schedule(call_id="C002")

# Fetch and print vehicle details
fms.print_vehicle_details("V001")

# Fetch and print call schedule details
fms.print_call_schedule_details("C001")

# Fetch and print maintenance records
fms.print_maintenance_records("V001")