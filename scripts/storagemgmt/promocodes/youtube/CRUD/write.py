from storagemgmt.schema.collections.video import Video


class Write:
    #   Spec:
    #       C>D depth of 4
    #       cChannels > dChannelID > cVideos > dVideo_ID
    #       Adds dVideo_ID under cVideos of the supplied d<channelID>
    #   Params:
    #       req dChannel ID
    #       req Class d"Video" with atleast unique video_id
    @staticmethod
    def writeVideoDocumentToVideosCollection(db, dchannelID, dVideo:Video):
        
        channel_doc_ref = db.collection("channels").document(f"{dchannelID}")
        video_ref = channel_doc_ref.collection("videos").document(f"{dVideo.video_id}")
        video_ref.set(dVideo.to_dict())
