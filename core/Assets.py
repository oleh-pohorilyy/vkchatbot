class Assets:

    @staticmethod
    def get_image(name):
        try:
            return Path(__file__).parent / f"../assets/img/{name}"
        except:
            return None