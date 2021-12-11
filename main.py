from linkedin import Linkedin
import secrets
import time

def connect_with_profiles(load, connection_note, profiles):
    for profile in profiles:
        load.go_to_url(profileURL=profile)

        res_check = load.checkConnection() # check current connection type

        j = 0
        if res_check == 'pending':
            print("In pending state")
        elif res_check == 'connected':
            j+=1
            print(f"Already connected {j}")
        elif (res_check == 'locked') or (res_check == 'follow'):
            print("Locked or Third connection")
        elif res_check == 'connect':
            print("Connecting ........")
            res = load.connect_to_profile(note=connection_note)

            if res == 'web driver exception':
                print("Code failed, debugging required")
                break

            if res != 'success':
                print(f'FAILED to connect with {profile}')
            elif res == 'success':
                print(f"Request sent successfully to {profile}")
    return

## instantiate LinkedIn object
load = Linkedin(username=secrets.username, password=secrets.password, path_to_driver=secrets.path_to_driver)

## Login
load.login()
time.sleep(5)

## any company's LinkedIn URL
## I am using Google 
google = "https://www.linkedin.com/company/google/people"

## Load Google organization URL on webpage
load.go_to_url(profileURL=google)

scroll_counter  = 5
load.scroll_down(scroll_counter=scroll_counter) ## scroll down for 50 seconds

profiles = load.get_all_profiles()

print(f'{len(profiles)} profiles found')

## Connect with connections
note = """I hope you are doing well. I am a student and looking for full time opprotunities in technology domain. It would be great if you consider my connection request.
Regards,
Sender"""
connect_with_profiles(load=load, connection_note=note, profiles=profiles)
load.end_session()




