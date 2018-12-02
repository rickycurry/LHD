class SettingsManager(object):

    learningLang = "en"
    fluentLang = "ko"
    langs = {"English" : "en", \
    "Korean" : "ko", \
    "French" : "fr",\
    "Italian" : "it",\
    "Japanese" : "ja"}


    def setFluentLang(self, language):
        #try:
            self.fluentLang = self.langs[language]
        #except:
        #    pass
    
    def getFluentLang(self):
        return self.fluentLang