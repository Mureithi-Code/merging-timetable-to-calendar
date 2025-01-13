from ics import Calendar, Event
from datetime import datetime, timedelta

# Updated Timetable details
timetable = [
    ("Focused Coding Work", "Learning, project development, debugging, and advanced practice.", "13:00", "15:30"),
    ("Break", "Take a short 15-minute break.", "15:30", "15:45"),
    ("Trading Activities", "Market analysis, strategy practice, journal updates, and review.", "15:45", "18:00"),
]

# Generate the calendar
cal = Calendar()
start_date = datetime(2025, 1, 13)  # Starting Monday

# Loop through each weekday
for day_offset in range(5):  # Monday to Friday
    for activity in timetable:
        name, description, start_time, end_time = activity
        # Calculate start and end times for each activity
        start_datetime = start_date + timedelta(
            days=day_offset,
            hours=int(start_time.split(":")[0]),
            minutes=int(start_time.split(":")[1]),
        )
        end_datetime = start_date + timedelta(
            days=day_offset,
            hours=int(end_time.split(":")[0]),
            minutes=int(end_time.split(":")[1]),
        )
        
        # Create an event
        event = Event()
        event.name = name
        event.begin = start_datetime.isoformat()  # Use ISO format to ensure correct time is saved
        event.end = end_datetime.isoformat()
        event.description = description
        
        # Add the event to the calendar
        cal.events.add(event)

# Save the calendar to a file
file_path = "Timetable.ics"
with open(file_path, "w") as f:
    f.writelines(cal.serialize_iter())

print(f"Timetable saved as {file_path}")
