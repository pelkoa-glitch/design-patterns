from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        ...
        

class EmailSenderService(BaseSenderService):
    def send_notification(self, message: str):
        print(f'Sending \'{message}\' to customer\'s email.')
        
        
class PushSenderService(BaseSenderService):
    def send_notification(self, message: str):
        print(f'Sending push notification {message} to customer.')
        
        
class ComposedSenderService(BaseSenderService):
    def __init__(self, senders: list[BaseSenderService]) -> None:
        self.senders: list[BaseSenderService] = senders
            
    def send_notification(self, message: str):
        for sender in self.senders:
            sender.send_notification(message)    

        
def main():
    sender = ComposedSenderService(
        [EmailSenderService(),
         PushSenderService()]
    )
    sender.send_notification("Hello")
    
    
if __name__ == '__main__':
    main()    