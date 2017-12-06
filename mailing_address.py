# Created by: Kay Lin
# Created on: Dec-4th 2017
# Created for: ICS3U
# This program displays mailing address information

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type, city_name, province_initials, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code

a_mailing_address = MailAddress(raw_input("First Name: "), raw_input("Last Name: "), raw_input("House Number: "), raw_input("Street Name: "), raw_input("Street Type: "), raw_input("City Name: "), raw_input("Province (initials): "), raw_input("Postal Code: "))

print("\n" + a_mailing_address.first_name + " " + a_mailing_address.last_name + "\n" + a_mailing_address.house_number + " " + a_mailing_address.street_name + " " + a_mailing_address.street_type + "\n" + a_mailing_address.city_name + ", " + a_mailing_address.province_initials + " " + a_mailing_address.postal_code + "\n")
