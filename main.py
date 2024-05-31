import requests
import logging
import time


logging.basicConfig(format='%(asctime)s | %(levelname)-8s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


url = 'https://api-clicker.pixelverse.xyz/api/'
username = input("Please enter your telegram username without @: ") 
tg_id = input("Please enter your telegram id: ")
secret = input("Please enter secret: ")
data = input("Please enter your Initdata: ")

logging.info("Starting the clicker bot... with telegramUserId:" + tg_id)


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,id-ID;q=0.9,id;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'dnt': '1',
    'Initdata': data,
    'origin': 'https://sexyzbot.pxlvrs.io/',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://sexyzbot.pxlvrs.io/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'secret': secret,
    'tg-id': tg_id,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'username': username
}


def start_bot():
    try:
        while True:
            current_pet_id = ""

            # Get user data
            logging.info("Getting user data...")
            response = requests.get(url + 'users', headers=headers)
            if response.status_code == 200:
                user_data = response.json()
                current_pet_id = user_data['pet']['id']

            # Get pets
            logging.info("Getting pets...")
            response = requests.get(url + 'pets', headers=headers)
            if response.status_code == 200:
                pets_data = response.json()
                list_pet = pets_data['data']
                logging.info(f"Found {len(list_pet)} pets")

                # Loop through pets
                for pet in list_pet:
                    user_pet = pet['userPet']
                    id_pet = user_pet['id']

                    # Select pet
                    logging.info(f"Selecting pet with id: {id_pet}")
                    response = requests.post(url + f'pets/user-pets/{id_pet}/select', headers=headers)
                    if response.status_code == 201 or id_pet == current_pet_id:
                        logging.info("Pet selected")
                        current_pet_id = id_pet

                        # Get user data with current pet
                        response = requests.get(url + 'users', headers=headers)
                        if response.status_code == 200:
                            user_data = response.json()
                            clicks_count = user_data['clicksCount']
                            pet = user_data['pet']
                            pet_name = pet['pet']['name']
                            pet_energy = pet['energy']
                            level = pet['level']
                            level_up_price = pet['levelUpPrice']

                            logging.info(f"Pet name: {pet_name} - Energy: {pet_energy} - Level: {level} - Level up price: {level_up_price}")
                            
                            # claim pet
                            response = requests.post(url + 'mining/claim', headers=headers)
                            if response.status_code == 201:
                                claim_pet_data = response.json()
                                claim_amount = claim_pet_data['claimedAmount']
                                clicks_count = claim_amount + clicks_count
                                logging.info(f"Pet claimed, current point: {clicks_count}")

                            while clicks_count > level_up_price:
                                # Level up pet
                                logging.info(f"Level up pet with price: {level_up_price}")
                                response = requests.post(url + f'pets/user-pets/{id_pet}/level-up', headers=headers)
                                if response.status_code == 201:
                                    response_data = response.json()
                                    level = response_data['level']
                                    level_up_price = response_data['levelUpPrice']
                                    clicks_count -= level_up_price
                                    logging.info(f"Pet level up to {level}, next level price: {level_up_price}")
                                else:
                                    break
                        else:
                            logging.error("Error getting user data")
                            time.sleep(1)
                    else:
                        logging.error(f"Error selecting pet: {response.status_code} - {response.reason}")
                        time.sleep(1)
            else:
                logging.error("Error getting pets")
                time.sleep(1)

            logging.info("Sleeping for 10 minutes")
            time.sleep(600)  # Sleep for 10 minutes
    except Exception as e:
        logging.error("An error occurred:", exc_info=e)


# Start the bot
start_bot()
