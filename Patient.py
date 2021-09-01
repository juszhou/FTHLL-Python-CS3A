class Patient:
    def __init__(self, first, middle, last, address, city, state, zip_code, phone):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

#   setters
    def set_first(self, first):
        self.first = first

    def set_middle(self, middle):
        self.middle = middle

    def set_last(self, last):
        self.last = last

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_phone(self, phone):
        self.phone = phone

#   getters
    def get_first(self):
        return self.name

    def get_middle(self):
        return self.middle

    def get_last(self):
        return self.last

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def __str__(self):
       return 'First Name: ' + self.first +\
              '\nMiddle Name: ' + self.middle +\
              '\nLast Name: ' + self.last +\
              '\nAddress: ' + self.address +\
              '\nCity: ' + self.city +\
              '\nState: ' + self.state +\
              '\nZIP: ' + self.zip_code +\
              '\nPhone: ' + self.phone

