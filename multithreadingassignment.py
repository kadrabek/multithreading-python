import threading
import time

#first thread with a fun fact about hummingbirds. has no delays.
def say_hello1():
    print(f"Thread 1: Hello! I'm thread 1!")
    time.sleep(1)
    print(f"Thread 1: Did you know? Hummingbirds are the only birds that can fly backward!")
    time.sleep(1)
    print(f"Thread 1: Bye now!")

#second thread with a fun fact about reindeers. has a three second delay. 
def say_hello2():
    time.sleep(3)
    print(f"Thread 2: Hello! I'm thread 2!")
    time.sleep(3)
    print(f"Thread 2: Did you know? Reindeer eyes turn blue in winter to see better in low light!")
    time.sleep(1)
    print(f"Thread 2: See you!")

#third thread with a fun fact about dolphins. has a 7 and 5 second delay.
def say_hello3():
    time.sleep(7)
    print(f"Thread 3: Hello! I'm thread 3!")
    time.sleep(5)
    print(f"Thread 3: Did you know? Dolphins use pufferfish toxins to enter a trance-like state!")
    time.sleep(1)
    print(f"Thread 3: Goodbye!")

#fourth thread with a fun fact about goats. has an 11 and 2 second delay.
def say_hello4():
    time.sleep(11)
    print(f"Thread 4: Hello! I'm thread 4!")
    time.sleep(2)
    print(f"Thread 4: Did you know? Goats can have accents, adjusting vocal sounds to their social group!")
    time.sleep(1)
    print(f"Thread 4: Bye Bye!")

#fifth thread with a fun fact about turtles. has a 15 and 7 second delay. 
def say_hello5():
    time.sleep(15)
    print(f"Thread 5: Hello! I'm thread 5!")
    time.sleep(7)
    print(f"Thread 5: Did you know? Turtles can breathe through their butts when hibernating underwater!")
    time.sleep(1)
    print(f"Thread 5: Bye!")

#all of the threads in one area with the target of each thread name shortened to t 1-5. 
t= threading.Thread(target=say_hello1)
t2= threading.Thread(target=say_hello2)
t3= threading.Thread(target=say_hello3)
t4= threading.Thread(target=say_hello4)
t5= threading.Thread(target=say_hello5)

#all of the threads start with a 5 second delay in between starting the next function. 
t.start()
time.sleep(5)
t2.start()
time.sleep(3)
t3.start()
time.sleep(1)
t4.start()
time.sleep(7)
t5.start()
time.sleep(9)

#final print message stateing that all threads have finished their fun facts with a 6 second delay before the message goes out. 
time.sleep(6)
print("All threads have finished their fun facts!")