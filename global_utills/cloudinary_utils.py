
def set_user_pic(image_url , user):
    import requests
    from cloudinary import uploader
    response = requests.get(image_url)
    if response.status_code == 200:
        upload_result = uploader.upload(response.content)
        user.picture = upload_result['secure_url']
        user.save()
        