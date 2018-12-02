class SettingsManager:

    learningLang = "en"
    langs = {"English" : "en", \
    "Korean" :"ko", \
    "French" : "fr",\
    "Italian" : "it",\
    "Japanese" : "ja"}

    def __init__(self, fluentLang):
        self.fluentLang = fluentLang

    def setFluentLang(self, langAbbrev):
        self.fluentLang = langAbbrev
    
    def getFluentLang(self):
        pass