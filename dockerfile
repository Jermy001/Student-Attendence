
FROM python:3.12-slim

WORKDIR /app

COPY student_attendance.py .

CMD ["python", "-u", "student_attendance.py"]
