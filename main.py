from prompt import send
import scratchattach as sa
import time

print("Receiving...")

session = sa.login("username", "password")
cloud = session.connect_cloud("1090355989")

while True:
    time.sleep(0.10)
    request = cloud.get_var("request")
    
    if request == "100":
        print("Ping requested")
        cloud.set_var("request", "500")
    
    if request == "150":
        try:
            send_value = cloud.get_var("parameter")
            send_value = sa.Encoding.decode(send_value)
            print(f"Send value: {send_value}")
            response = send(send_value)
            print(f"Response: {response}")
            encoded_answer = sa.Encoding.encode(response)
            cloud.set_var("parameter", encoded_answer)
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(0.10)
        cloud.set_var("request", "500")
