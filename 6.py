from pymonad.tools import curry
from pymonad.state import State

initial_balance = 1000

@curry(3)
def update_balance(amount, description, previous_value):
    def action(balance):
        new_balance = balance + amount
        return (description, new_balance)
    return State(action)

deposit_200 = update_balance(200, "Пополнение +200")
withdraw_150 = update_balance(-150, "Снятие -150")
deposit_100 = update_balance(100, "Пополнение +100")

chain = (
    State.insert("Начало операции")  
    .then(deposit_200)  
    .then(withdraw_150) 
    .then(deposit_100)  
)

result, final_balance = chain.run(initial_balance)