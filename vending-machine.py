from byotest import*

usd_coins = [100,50,25,10,5,2,1]
eur_coins = [100,50,20,10,5,2,1]

#Get change function
def get_change(amount,coin_list=eur_coins):
        change = []
        for coin in coin_list:
            while coin <= amount:
                amount -= coin
                change.append(coin)
        return change   
    
        
#Tests
test_are_equal(get_change(0,eur_coins),[])
test_are_equal(get_change(1,eur_coins),[1])
test_are_equal(get_change(2,eur_coins),[2])
test_are_equal(get_change(5,eur_coins),[5])
test_are_equal(get_change(10,eur_coins),[10])
test_are_equal(get_change(20,eur_coins),[20])
test_are_equal(get_change(50,eur_coins),[50])
test_are_equal(get_change(100,eur_coins),[100])
test_are_equal(get_change(3,eur_coins),[2,1])
test_are_equal(get_change(7,eur_coins),[5,2])
test_are_equal(get_change(9,eur_coins),[5,2,2])
test_are_equal(get_change(75,usd_coins),[50,25])

print("All tests passed!")