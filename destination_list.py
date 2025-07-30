destinations = [
    {
        "name": "Goa",
        "type": "local",
        "cost_per_person": [9000, 16000],
        "group_type": ["solo", "friends", "family"],
        "visa_required": False,
        "purpose": ["Relaxation", "Adventure", "Luxury"],
        "ideal_months": ["November", "December", "January", "February"],
        "not_ideal_months": ["June", "July", "August", "September"],
        "month_reasons": {
            "November": "Pleasant weather, start of tourist season",
            "December": "Festivals and peak tourist season",
            "January": "Cool and comfortable, great for outdoor activities",
            "February": "Ideal weather for beach and parties",
            "June": "Heavy monsoon rains, beaches less accessible",
            "July": "Monsoon season, poor outdoor conditions",
            "August": "Continued monsoon rains, not ideal for tourists",
            "September": "Monsoon ends late, still wet and humid"
        }
    },
    {
        "name": "Manali",
        "type": "local",
        "cost_per_person": [7000, 13000],
        "group_type": ["solo", "family", "friends"],
        "visa_required": False,
        "purpose": ["Adventure", "Nature", "Relaxation"],
        "ideal_months": ["March", "April", "May", "September", "October"],
        "not_ideal_months": ["December", "January", "February"],
        "month_reasons": {
            "March": "Snow starts melting, good for trekking",
            "April": "Pleasant weather, ideal for sightseeing",
            "May": "Warm and great for adventure activities",
            "September": "Post monsoon, clear skies",
            "October": "Mild weather, perfect for nature walks",
            "December": "Heavy snowfall, some roads may be closed",
            "January": "Very cold and harsh winter conditions",
            "February": "Cold with occasional snowfall"
        }
    },
    {
        "name": "Jaipur",
        "type": "local",
        "cost_per_person": [6000, 11000],
        "group_type": ["family", "solo"],
        "visa_required": False,
        "purpose": ["Culture", "Luxury", "Relaxation"],
        "ideal_months": ["October", "November", "December", "January", "February"],
        "not_ideal_months": ["June", "July", "August", "September"],
        "month_reasons": {
            "October": "Start of cool season, good for sightseeing",
            "November": "Pleasant weather, cultural festivals",
            "December": "Cool and comfortable, peak tourist time",
            "January": "Chilly but great for outdoor tours",
            "February": "Mild weather, ideal for visiting forts",
            "June": "Very hot, not comfortable for sightseeing",
            "July": "Monsoon rains begin, humid weather",
            "August": "Wet and humid, low tourist activity",
            "September": "End of monsoon, still humid"
        }
    },
    {
        "name": "Ladakh",
        "type": "local",
        "cost_per_person": [12000, 21000],
        "group_type": ["solo", "friends"],
        "visa_required": False,
        "purpose": ["Adventure", "Nature"],
        "ideal_months": ["May", "June", "July", "August", "September"],
        "not_ideal_months": ["December", "January", "February", "March", "April", "October", "November"],
        "month_reasons": {
            "May": "Snow melts, perfect for biking and trekking",
            "June": "Clear skies and warm days",
            "July": "Ideal for adventure and sightseeing",
            "August": "Pleasant weather, fewer tourists",
            "September": "Great for photography and nature",
            "December": "Extreme cold, roads mostly closed",
            "January": "Severe winter, very harsh conditions",
            "February": "Snowbound and inaccessible",
            "March": "Still cold with snow",
            "April": "Slow thaw, some areas inaccessible",
            "October": "Cold begins, short season ends",
            "November": "Start of winter, difficult travel"
        }
    },
    {
        "name": "Dubai",
        "type": "foreign",
        "cost_per_person": [40000, 60000],
        "group_type": ["family", "friends"],
        "visa_required": True,
        "purpose": ["Luxury", "Culture", "Relaxation"],
        "ideal_months": ["November", "December", "January", "February", "March"],
        "not_ideal_months": ["June", "July", "August", "September"],
        "month_reasons": {
            "November": "Pleasant weather, start of tourist season",
            "December": "Peak season with festivals",
            "January": "Cool and comfortable",
            "February": "Ideal for outdoor activities",
            "March": "Warm but pleasant",
            "June": "Extreme heat, not suitable for outdoor",
            "July": "Very hot and humid",
            "August": "Peak summer heat, avoid outdoor",
            "September": "Still very hot and humid"
        }
    },
    {
        "name": "Thailand",
        "type": "foreign",
        "cost_per_person": [30000, 45000],
        "group_type": ["solo", "friends"],
        "visa_required": True,
        "purpose": ["Beach", "Adventure", "Relaxation"],
        "ideal_months": ["November", "December", "January", "February", "March"],
        "not_ideal_months": ["May", "June", "July", "August", "September", "October"],
        "month_reasons": {
            "November": "End of rainy season, great beach weather",
            "December": "Peak tourist season",
            "January": "Pleasant weather, ideal for travel",
            "February": "Warm and sunny",
            "March": "Hot but manageable",
            "May": "Start of rainy season",
            "June": "Heavy rains, high humidity",
            "July": "Monsoon season, less ideal for tourists",
            "August": "Rain and humidity continue",
            "September": "Rainy and humid",
            "October": "Rainy, flooding risk"
        }
    },
    {
        "name": "Bali",
        "type": "foreign",
        "cost_per_person": [35000, 50000],
        "group_type": ["solo", "family", "friends"],
        "visa_required": False,
        "purpose": ["Beach", "Relaxation", "Luxury"],
        "ideal_months": ["April", "May", "June", "September"],
        "not_ideal_months": ["January", "February", "March", "October", "November", "December"],
        "month_reasons": {
            "April": "Start of dry season, great weather",
            "May": "Pleasant and sunny",
            "June": "Dry and comfortable",
            "September": "End of dry season, ideal for travel",
            "January": "Wet season with heavy rains",
            "February": "Rainy and humid",
            "March": "Wet season continues",
            "October": "Start of rainy season",
            "November": "Rain increases",
            "December": "Peak rainy season"
        }
    },
    {
        "name": "Sikkim",
        "type": "local",
        "cost_per_person": [8000, 14000],
        "group_type": ["solo", "family"],
        "visa_required": False,
        "purpose": ["Nature", "Culture", "Relaxation"],
        "ideal_months": ["March", "April", "May", "September", "October", "November"],
        "not_ideal_months": ["December", "January", "February"],
        "month_reasons": {
            "March": "Spring bloom, pleasant weather",
            "April": "Ideal for trekking and sightseeing",
            "May": "Warm and clear",
            "September": "Post monsoon, clear skies",
            "October": "Perfect for nature lovers",
            "November": "Cool and peaceful",
            "December": "Cold and foggy",
            "January": "Very cold, snow possible",
            "February": "Cold weather continues"
        }
    },
    {
        "name": "Andaman Islands",
        "type": "local",
        "cost_per_person": [10000, 18000],
        "group_type": ["family", "friends"],
        "visa_required": False,
        "purpose": ["Beach", "Relaxation", "Nature"],
        "ideal_months": ["October", "November", "December", "January", "February", "March"],
        "not_ideal_months": ["May", "June", "July", "August", "September"],
        "month_reasons": {
            "October": "End of monsoon, clear waters",
            "November": "Ideal for beach and water sports",
            "December": "Pleasant weather and festivals",
            "January": "Cool and comfortable",
            "February": "Great for snorkeling and diving",
            "March": "Warm and sunny",
            "May": "Start of monsoon, heavy rains",
            "June": "Monsoon season, rough seas",
            "July": "Heavy rainfall, not suitable for tourists",
            "August": "Monsoon continues, avoid water activities",
            "September": "Monsoon tapering off, still wet"
        }
    },
    {
        "name": "Singapore",
        "type": "foreign",
        "cost_per_person": [50000, 70000],
        "group_type": ["family", "friends"],
        "visa_required": True,
        "purpose": ["Luxury", "Culture", "Relaxation"],
        "ideal_months": ["February", "March", "April", "May", "June"],
        "not_ideal_months": ["November", "December", "January"],
        "month_reasons": {
            "February": "Warm and less rainy",
            "March": "Pleasant weather, good for city tours",
            "April": "Warm and humid, but manageable",
            "May": "Good for sightseeing and events",
            "June": "Start of rainy season, short showers",
            "November": "Heavy rain and humidity",
            "December": "Frequent thunderstorms",
            "January": "Cool but wet weather"
        }
    }
]
