# NAME:         Nicholas Ngobi
# ASSIGNMENT:   Project  Stacks & Queues

from Queue import Queue

# count the longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    current_length = 1  # each starting character in a given string starts 1
    longLength = 0 # long length is initialized as 0 bc it's not yet known/ may as well be empty
    while not q.is_empty():# Condition to check or not the queue is empty
        current = q.deq() #Removes the front and stores it 
        while current == q.front(): # Removed/dequeued matches the new front of q/ this is a condition for values repeating
                                    # while true /once current != to the new front, the while loop will stop.
            q.deq()                 # dequeuing the q/ this will occur regardless 
            current_length += 1     # Increasing the current length
        if current_length > longLength:
            longLength = current_length
        current_length = 1          # reset back to 1 as we go to a new character.
    return longLength

def main():

    print(count_longest(Queue([l for l in "oooohheeee"])) == 4)
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))


# Don't run main on import
if __name__ == "__main__":
    main()

