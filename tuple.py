# employees = [
#     (101, "Dhanraj", "Backend Developer", 55000),
#     (102, "Arun", "Frontend Developer", 48000),
#     (103, "Meena", "Data Analyst", 60000)
# ]

# # Print employee details
# for emp in employees:
#     emp_id, name, role, salary = emp
#     print(f"ID: {emp_id}, Name: {name}, Role: {role}, Salary: ₹{salary}")





weather_data = {
    (12.9716, 77.5946): "Bangalore",
    (13.0827, 80.2707): "Chennai",
    (28.6139, 77.2090): "Delhi"
}

location = (13.0827, 80.2707)
print(weather_data[location])