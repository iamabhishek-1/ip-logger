# Conceptual device detection
import random

def get_device_info():
    """Return conceptual device information"""
    devices = [
        {"type": "mobile", "os": "Android", "model": "Pixel 6"},
        {"type": "mobile", "os": "iOS", "model": "iPhone 13"},
        {"type": "desktop", "os": "Windows 11", "model": "Dell XPS"},
        {"type": "desktop", "os": "macOS", "model": "MacBook Pro"}
    ]
    
    selected = random.choice(devices)
    return {
        "device_type": selected["type"],
        "operating_system": selected["os"],
        "device_model": selected["model"],
        "browser": random.choice(["Chrome", "Safari", "Firefox", "Edge"]),
        "screen_resolution": f"{random.randint(800, 3840)}x{random.randint(600, 2160)}",
        "connection_type": random.choice(["WiFi", "4G", "5G", "Ethernet"])
    }