import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from storagemgmt.promocodes.youtube.CRUD.write import Write
from storagemgmt.promocodes.youtube.CRUD.read import Read

from storagemgmt.schema.collections.video import Video
from storagemgmt.schema.collections.channel import Channel




def writeVideoDocumentToVideosCollection(channel, video):
    Write.writeVideoDocumentToVideosCollection(db, dChannel=channel, dVideo=video)


def createChannelDocument(channel):
    Write.writeChannelDocumentID(db, dChannel=channel)


def readDocumentsFromDchannelVideosCollection(channel):
    Read.readVideoDocumentsInChannelDocument(db, dChannel=channel)


if __name__ == "__main__":
    #Use a service account.
    cred = credentials.Certificate(r'D:\further-promohub data\further-promohub-firebase-adminsdk-si7sx-64a88f371b.json')

    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    channel = Channel(channelID="a second channel")
    video = Video(video_id = 201, video_link="pretend_link", video_name="first video", promocode="second channel promocode")
    createChannelDocument(channel)
    writeVideoDocumentToVideosCollection(channel, video)
    readDocumentsFromDchannelVideosCollection(channel)