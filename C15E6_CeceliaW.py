#Author: Cecelia Williams
#Last Revision: 4.28.2017
#Description: Chapter 15 Exercise 6
#   Create a new class, SMS_store.
#   has_been_viewed, from_number, time_arrived, text_of_SMS

class SMS_store:
    """ The class will instantiate SMS_store objects,
        similar to an inbox or outbox on a cellphone: """
    

    def __init__(self):
        """ Creates a new instance of SMS_store """
        self.inbox = [] 


    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Makes new SMS tuple, inserts it after other messages
            in the store. When creating this message, its
            has_been_viewed status is set False. """
        message_unread = []
        message_unread = [from_number, time_arrived, text_of_SMS]
        self.inbox.append(message_unread)
        #self = incoming_text

    def to_string(self):
        return "({0}".format(self.inbox)   

    def message_count(self):
        """ Returns the number of sms messages in my_inbox """
        text_messages = self
        texts = 0
        for i in text_messages:
            texts += 1
        return texts
        

    def get_unread_indexes(self):
        """ Returns list of indexes of all not-yet-viewed SMS messages """
        unread_texts = []
        for i in self:
            if i.texts(['Opened']) == 0:
                unread_texts.append[i]
        return unread_tests
    

    def get_message(self, i):
        """ Return (from_number, time_arrived, text_of_sms): for message[i]
            Also change its state to "has been viewed".
            If there is no message at position i, return None """
        message = self[i]
        for i in message:
            for j in inbox:
                message.append([from_number, time_arrived, text_of_sms])
        return message

    def delete(i):
        """ Delete the message at index i """
        del self[i]

        
    def clear():
        """ Delete all messages from inbox """
        self = []


#############################     TESTING SUITE     ##########################
#def store_test_suite:
cell_inbox = SMS_store()

cell_inbox.add_new_arrival('+7816175089','9:45A','Gotta work late tonight')
print()
cell_inbox.add_new_arrival('+5087816175','12:11P','WTG on new contract')
print()
cell_inbox.add_new_arrival('+6175087812','2:36P','love you babe')
print()
cell_inbox.add_new_arrival('+4012354215','6:01P','smh')
print()

print(cell_inbox.to_string())
'''
current_texts = [['+7816175089','9:45A','Gotta work late tonight'],
                 ['+5087816175','12:11P','WTG on new contract'],
                 ['+6175087812','2:36P','love you babe'],  
                 ['+4012354215','6:01P','smh']]
'Unopened', 
for m in current_texts:
    for n in m:
        cell_inbox.add_new_arrival(n[0], n[1], n[2])
print(cell_inbox)
'''
