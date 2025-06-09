# Conceptual GeoIP information
import random
from datetime import datetime

def get_geo_info(ip):
    """Return conceptual geo information about an IP"""
    cities = ["New York", "London", "Tokyo", "Mumbai", "Sydney"]
    isps = ["ISP A", "ISP B", "ISP C", "ISP D"]
    
    return {
        "ip": ip,
        "type": "IPv4" if "." in ip else "IPv6",
        "continent": random.choice(["Asia", "Europe", "North America"]),
        "country": random.choice(["US", "UK", "IN", "JP", "AU"]),
        "city": random.choice(cities),
        "postal": f"{random.randint(10000, 99999)}",
        "isp": random.choice(isps),
        "timezone": random.choice(["UTC-5", "UTC+0", "UTC+9", "UTC+5:30"]),
        "coordinates": {
            "lat": f"{random.uniform(-90, 90):.4f}",
            "lon": f"{random.uniform(-180, 180):.4f}"
        },
        "timestamp": datetime.now().isoformat()
    }