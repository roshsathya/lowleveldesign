class DismissalBaseClass:
    def __init__(self, batsman, bowler) -> None:
        self.batsman = batsman
        self.bowler = bowler
        self.description = None

    def add_dismissal(self):
        raise Exception()

    def get_description(self):
        raise Exception()

    def get_brief_description(self):
        raise Exception()


class CaughtDismissal(DismissalBaseClass):
    def __init__(self, batsman, bowler) -> None:
        super().__init__(batsman, bowler)
        self.catcher = None

    def add_dismissal(self, catcher, description):
        self.catcher = catcher
        self.description = description

    def get_description(self):
        brief_descr = self.get_brief_description()
        return f"{brief_descr} \n {self.description}"

    def get_brief_description(self):
        return f"c {self.batsman.name} b {self.bowler.name}"


class DismissalFactory:
    types = {
        "CAUGHT": CaughtDismissal,
        "BOWLED": None,
        "RUN_OUT": None,
        "HIT_WICKET": None
    }

    @classmethod
    def get_dismissal(cls, dismissal_type, batsman, bowler):
        if dismissal_type not in cls.types:
            raise Exception()
        return cls.types[dismissal_type](batsman, bowler)
