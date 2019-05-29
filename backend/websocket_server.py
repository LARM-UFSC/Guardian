import asyncio
import websockets
import engines

async def hello(websocket, path):
    way = engines.motors(forward_pin=13, backward_pin=11, servo=7)

    try:
        while True:
            cmd = await websocket.recv()
            if cmd == '8d' or cmd == '-58d':
                way.ahead()
            if cmd == '8u' or cmd == '-58u':
                way.stop()
            
            if cmd == '2d' or cmd == '-56u':
                way.backward()
            if cmd == '2u' or cmd == '-56u':
                way.stop()
            
            if cmd == '4d' or cmd == '-59u':
                way.turn_left()
            if cmd == '4u' or cmd == '-59u':
                way.reset_servo()
            
            if cmd == '6d' or cmd == '-57u':
                way.turn_right()
            if cmd == '6u' or cmd == '-57u':
                way.reset_servo()
            
            # if cmd == '1d':
            #     way.t_esquerda()
            # if cmd == '1u':
            #     way.stop()
            
            # if cmd == '3d':
            #     way.t_direita()
            # if cmd == '3u':
            #     way.stop()
            
            # if cmd == '7d':
            #     way.f_esquerda()
            # if cmd == '7u':
            #     way.stop()
            
            # if cmd == '9d':
            #     way.f_direita()
            # if cmd == '9u':
            #     way.stop()
    except:
        way.stop()
        GPIO.cleanup()  

def start():
    start_server = websockets.serve(hello, '', 8083)
    
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

    print("Websocker ready!")



if __name__ == "__main__":
    start()