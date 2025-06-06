SUPPLIERS = [
    {
        "name": "Safran",
        "component": "Moteur",
        "criticality": "High",
        "dual_sourcing": False,
        "sites": [
            {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522, "stock_days": 14, "lead_time": 90},
            {"city": "Casablanca", "country": "Maroc", "lat": 33.5731, "lon": -7.5898, "stock_days": 7, "lead_time": 110},
        ]
    },
    {
        "name": "Spirit AeroSystems",
        "component": "Fuselage",
        "criticality": "High",
        "dual_sourcing": False,
        "sites": [
            {"city": "Wichita", "country": "USA", "lat": 37.6872, "lon": -97.3301, "stock_days": 10, "lead_time": 120},
        ]
    },
    {
        "name": "Liebherr",
        "component": "Train d'atterrissage",
        "criticality": "Medium",
        "dual_sourcing": True,
        "sites": [
            {"city": "Lindenberg", "country": "Allemagne", "lat": 47.6029, "lon": 10.0113, "stock_days": 30, "lead_time": 80},
        ]
    },
    {
        "name": "Collins Aerospace",
        "component": "Avionique",
        "criticality": "Medium",
        "dual_sourcing": True,
        "sites": [
            {"city": "Cedar Rapids", "country": "USA", "lat": 41.9779, "lon": -91.6656, "stock_days": 22, "lead_time": 95},
        ]
    },
]
