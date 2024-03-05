
class Video:
    def __init__(self, video_id, video_link, video_name, promocode, product="", affiliate_link=""): 
        self.video_id = video_id
        self.video_link = video_link
        self.video_name = video_name
        self.promocode = promocode     
        self.product = product
        self.affiliate_link = affiliate_link



    @staticmethod
    def from_dict(source):
        video = Video(
                    source["video_id"],
                    source["video_link"],
                    source["video_name"],
                    source["promocode"]
                )
        
        if "product" in source:
            video.product = source["product"]

        if "affiliate_link" in source:
            video.affiliate_link = source["affiliate_link"]

        return video



    def to_dict(self):
        video = {  
                    "video_id": self.video_id,
                    "video_link": self.video_link,
                    "video_name": self.video_name,
                    "promocode": self.promocode
                }

        if self.product:
            video["product"] = self.product

        if self.affiliate_link:
            video["affiliate_link"] = self.affiliate_link

        return video