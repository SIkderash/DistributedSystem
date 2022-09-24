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
    else:
        print("Bucket 'stories' already exists")

    
    client.put_object(
        "stories", id, img, -1, part_size =  5300000, 
    )
    
    print(
        "Story is successfully uploaded as " + id + "to bucket 'asiatrip'."
    )

def getObjects():
    
    client = Minio(
        "localhost:9000",
        access_key="gaXwCW85Aox3tsbM",
        secret_key="PAUPUSvhfaioWdfbC0mOE6D9wP1arIfM",
        secure=False
    )
    objects = client.list_objects("my-bucket")
    for obj in objects:
        print(obj)
    
    return objects


if __name__ == "__main__":
    try:
        minioClient()
    except S3Error as exc:
        print("error occurred.", exc)