class BankKards:
    def init(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def check_balance(self):
        print(f'Your balance is: {self.balance}')
        print('Wow! You are a rich man!\nヾ(o✪‿✪o)ｼ')

    def create_new_card(self):
        card11 = BankKards(username=input('Enter username for new card: '),
                           password=input('Enter password for your card: '), balance=0)
        print('-----------------------------------------------------------------------------')
        print('Well done! \nYou create new card!')
        print(
            f'Your card username is: {card11.username}, and password: {card11.password}. \nPlease keep in mind! \nAnd your balance is: 0\n( ◠ ◡ ◠ )')

    def block_kard(self):
        del self


card1 = BankKards('Dinara', 'dinara', 1234567890)
card2 = BankKards('Tofic', 'tofic', 1)
card3 = BankKards('Jannat', 'jannat', 12)
card4 = BankKards('Nastya', 'nastya', 123)
card5 = BankKards('Vika', 'vika', 1234)
card6 = BankKards('Eldiyar', 'eldiyar', 12345)
card7 = BankKards('Quba', 'quba', 123456)
card8 = BankKards('Sharip', 'sharip', 1234567)
card9 = BankKards('Ayday', 'ayday', 12345678)
card10 = BankKards('Sher', 'sher', 123456789)

cards = [(card1.username, card1.password), (card2.username, card2.password),
         (card3.username, card3.password), (card4.username, card4.password),
         (card5.username, card5.password), (card6.username, card6.password),
         (card7.username, card7.password), (card8.username, card8.password),
         (card9.username, card9.password), (card10.username, card10.password)]

print('Hello i am your kard manager!')
action = input('Do you want check your card?: ')
if action.lower() == 'yes':
    card_username = input('Enter your username: ')
    card_password = input('Enter your password: ')
    card_user = card_username, card_password

    if card_user in cards:
        print(f'Hello, {card_username}!')
        action2 = input('What you want to do(check balance, block card, create new card): ')

        for i in (card1, card2, card3, card4, card5, card6, card7, card8, card9, card10):
            if action2.lower() == 'check balance':
                i.check_balance()
                break

            elif action2.lower() == 'block card':
                sure = input('Are you sure?: ')

                if sure == 'yes':
                    print(f'Bye bye {i.username}')
                    print("You are succesfully block your card")
                    del i
                    break
                else:
                    continue

            elif action2.lower() == 'create new card':
                i.create_new_card()
                break

            else:
                print('I dont understand you! Please express yourself more clearly')

    elif card_user not in cards:
        print('Check your username and password. And try again')


elif action.lower() == 'no':
    print("Good bye")
else:
    print('I dont understand you! Please try later!\nMaybe you are drunked...')