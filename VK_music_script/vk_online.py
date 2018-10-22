from time import sleep
import vk_api
 
if __name__ == "__main__":
 
    vk_session = vk_api.VkApi('mobile_number', 'pass')
    vk_session.auth()
    vk = vk_session.get_api()
 
    me = vk.users.get(user_ids=42744726, fields='online')
    while True:
        vk.session.auth()
        sleep(0.1)
