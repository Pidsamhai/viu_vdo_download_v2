from dataclasses import dataclass

@dataclass
class MovieHistory:
    def __init__(self,name:str = "",url:str = ""):
        self.name = name
        self.url = url

@dataclass
class Episode:
    def __init__(self,name:str = "",url:str = ""):
        self.name = name 
        self.url = url

@dataclass
class Movie:
    def __init__(self, epName: str = "", dl_url: str = "", subtitle: list = []):
        self.epName = epName
        self.dl_url = dl_url
        self.subtitle = subtitle