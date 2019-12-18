from dataclasses import dataclass

@dataclass
class MovieHistory:
    name:str
    url:str

@dataclass
class Episode:
    name:str
    url:str

@dataclass
class Movie:
    epName:str
    url:str
    subtitle:list