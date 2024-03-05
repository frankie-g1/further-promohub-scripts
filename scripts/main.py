import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from storagemgmt.promocodes.youtube.CRUD.write import Write
from storagemgmt.schema.collections.video import Video


def writeVideoDocumentToVideosCollection():
    video = Video(video_id = 101, video_link="pretend_link", video_name="my first video!", promocode="newpromocode")
    Write.writeVideoDocumentToVideosCollection(db, channelID="channelID: <exampleGoogleDevChannelID>", Video=video)


if __name__ == "__main__":
    #Use a service account.
    cred = credentials.Certificate(r'D:\further-promohub data\further-promohub-firebase-adminsdk-si7sx-64a88f371b.json')

    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    