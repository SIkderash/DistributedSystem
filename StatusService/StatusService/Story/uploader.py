import base64
from urllib import response
from minio import Minio
from minio.error import S3Error


def minioClient(id, img):

    client = Minio(
        "minio:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    found = client.bucket_exists("stories")
    if not found:
        client.make_bucket("stories")
        print("Bucket 'stories' created")
    else:
        print("Bucket 'stories' already exists")

    
    client.put_object(
        "stories", id, img, -1, part_size =  5300000, 
    )
    
    print(
        "Story is successfully uploaded as " + id + "to bucket 'asiatrip'."
    )

def getObjects(uids):
    
    client = Minio(
        "minio:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    ret = []

    for id in uids:
        response = client.get_object("stories", id)
        with open('my-testfile.png', 'wb') as file_data:
            for d in response.stream(32*1024):
                file_data.write(d)
        with open("my-testfile.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        ret.append(encoded_string)
    
    return ret
    