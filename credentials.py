class Credentials:
    credentions = []
def __init__(self, website_name, website_email, website_password):
    self.website_name = website_name
    self.website_email = website_email
    self.website_password = website_password

    def add_credentials(self):
        Credentials.credentions.append(self)
            