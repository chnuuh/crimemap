class MockDBHelper:
    def connect(self, database='crimemap'):
        pass

    def get_all_inputs(self):
        return []

    def add_input(self):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return [{
            'latitude': -33.30,
            'longitude': 26.52,
            'date': '2000-1-1',
            'category': 'muggling',
            'description': 'mock description'
        }]


