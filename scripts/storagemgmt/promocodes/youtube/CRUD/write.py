

class Write:
    #   Spec:
    #       C>D depth of 4
    #       cChannels > dChannelID > cVideos > dVideo_ID
    #       Create dVideo and append to dVideo fields
    #   Params:
    #       req Class d"Channel"
    #       req Class d"Video"
    @staticmethod
    def writeVideoDocumentToVideosCollection(db, dChannel, dVideo):
        
        channel_doc_ref = db.collection("channels").document(f"{dChannel.get_channelID()}")
        video_ref = channel_doc_ref.collection("videos").document(f"{dVideo.video_id}")
        video_ref.set(dVideo.to_dict())


    #   Spec:
    #       C > D depth of 2
    #       cChannels > dChannel
    #       To finish remote instantiation of CD:
    #           1. Create document named after channel id
    #           2. Append all channel fields to dChannel, for easier firebase querying in other parts of app
    #   Params:
    #       req Class d"Channel" Object
    @staticmethod
    def writeChannelDocumentID(db, dChannel):

        new_channel_doc_ref = db.collection("channels").document(f"{dChannel.get_channelID()}")
        new_channel_doc_ref.set(dChannel.to_dict())
