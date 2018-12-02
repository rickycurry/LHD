class Demo:
    translation = ""

    def __init__(self, url, startTime, endTime, translation):
        self.url = url
        self.startTime = startTime
        self.endTime = endTime
        self.translation = translation
    
    def addTranscript(self, transcript):
        self.transcript = transcript
    
    def removeTranscript(self):
        self.transcript = ""
    
    def translate(self, language):
        pass  