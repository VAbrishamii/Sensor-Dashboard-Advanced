from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Sensor

router = APIRouter()
sensors: List[Sensor] = []

for i in range (1, 6):
    sensors.append(Sensor(id=i, name=f"Sensor {i}", location=f"Room {i}", temperature=20.0 + i, humidity=30.0 + i, pressure=40.0 + i))

@router.get("/sensors", response_model=List[Sensor])
async def get_sensors():
    return sensors

@router.get("/sensors/{sensor_id}", response_model=Sensor)
async def get_sensor(sensor_id: int):
    for sensor in sensors:
        if sensor.id == sensor_id:
            return sensor
    raise HTTPException(status_code=404, detail="Sensor not found")