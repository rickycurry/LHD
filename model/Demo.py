class Demo:

    def __init__(self, url, startTime, endTime):
        self.url = url
        self.startTime = startTime
        self.endTime = endTime
        transcript = ""
        translation = ""
    
    def addTranscript(self, transcript):
        self.transcript = transcript
    
    def removeTranscript(self):
        self.transcript = ""
    
    def translate(self, language):
        pass  