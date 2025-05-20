from bank_accounts import *

dave = BankAccount(1000, "Dave")
sara = BankAccount(2000, "Sara")

print("\n--Accounts initial balance:")
dave.getBalance()
sara.getBalance()

print("\n--Sara deposit of $500:")
sara.deposit(500)

print("\n--Dave failed and sucessful withdraw:")
dave.withdraw(10000)
dave.withdraw(10)

print("\n--Dave transfer to Sara:")
dave.transfer(10000, sara)
dave.transfer(100, sara)

print("\n--Interest Reward:")
jim = InterestRewardsAcct(1000, "Jim")

jim.getBalance()

jim.deposit(100)

jim.transfer(100, dave)

print("\n--Savings Account:")
blaze = SavingsAcct(1000, "Blaze")

blaze.getBalance()

blaze.deposit(100)

blaze.transfer(10000, sara)
blaze.transfer(1000, sara)
