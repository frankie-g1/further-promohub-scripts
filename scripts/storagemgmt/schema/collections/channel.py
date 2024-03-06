
class Channel:
    def __init__(self, channelID): 
        self.channelID = channelID


    @staticmethod
    def from_dict(source):
        channel = Channel(
                    source["channelID"]
                )

        return channel


    def to_dict(self):
        channel = {  
                    "channelID": self.channelID
                }

        return channel
    

    def get_channelID(self):
        return self.channelID