import requests

# Specify your personal API key
API_KEY = "wfoltQG8uo2NEIXJuQj36mjWbdzsRz8dFEVfn--5DTQ"

def geocode_address(address: str) -> tuple:
    """
    Get latitude and longitude coordinates from an address using HERE Maps Geocoding API.

    Args:
        address (str): The address to geocode.

    Returns:
        tuple: A tuple containing (latitude, longitude).

    Raises:
        ValueError: If the address cannot be geocoded.
    """
    geocode_url = f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={API_KEY}"
    response = requests.get(geocode_url)
    response.raise_for_status()
    data = response.json()

    if data['items']:
        position = data['items'][0]['position']
        return position['lat'], position['lng']
    else:
        raise ValueError(f"No coordinates found for address: {address}")

def calculate_distance(coord1: tuple, coord2: tuple) -> tuple:
    """
    Calculate the distance and estimated travel time between two coordinates using HERE Maps Routing API.

    Args:
        coord1 (tuple): Origin coordinates as (latitude, longitude).
        coord2 (tuple): Destination coordinates as (latitude, longitude).

    Returns:
        tuple: A tuple containing (distance in meters, duration in seconds).

    Raises:
        ValueError: If no route is found.
    """
    routing_url = (
        f"https://router.hereapi.com/v8/routes?"
        f"transportMode=car&origin={coord1[0]},{coord1[1]}&destination={coord2[0]},{coord2[1]}"
        f"&return=summary&apiKey={API_KEY}"
    )
    response = requests.get(routing_url)
    response.raise_for_status()
    data = response.json()

    if data['routes']:
        summary = data['routes'][0]['sections'][0]['summary']
        return summary['length'], summary['duration']
    else:
        raise ValueError("No route found between the provided coordinates.")