from abc import ABC, abstractmethod


class BaseSenderService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        ...
        

class EmailSenderService(BaseSenderService):
    def send_notification(self, message: str):
        print(f'Sending \'{message}\' to customer\'s email.')
        
        
        
def main():
    email_sender = EmailSenderService()
    email_sender.send_notification("Hello")
    
    
if __name__ == '__main__':
    main()    