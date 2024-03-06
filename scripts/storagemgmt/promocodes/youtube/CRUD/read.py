from google.cloud.firestore_v1.base_query import FieldFilter


class Read:

    #   Spec:
    #       CDCD depth of 4
    #       cChannels > dChannel > cVideos > dVideo
    #       Print all dVideo documents under a particular dChannel's cVideos
    #   Params:
    #       req: Class d"Channel" 
    @staticmethod
    def readVideoDocumentsInChannelDocument(db, dChannel):
        d_videos = (
            db.collection("channels").document(f"{dChannel.get_channelID()}").collection("videos")
             .stream()
             
        ) # Array of documents -  Specifically sourced from the remote collection "videos"

        for d_video in d_videos:
            print(f"{d_video.id} => {d_video.to_dict()}")

