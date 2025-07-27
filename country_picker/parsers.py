
def parse_country_data(data: list[dict]) -> list[str]:
        """Parse the country data from the API response."""
        return sorted([country["name"] for country in data])
