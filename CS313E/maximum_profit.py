import sys

# Add Your functions here
def max_profit(money, num_houses, prices, increase):
    #dynamic programming approach
    dp = [0] * (money + 1)
    for i in range(num_houses):
        for j in range(money, prices[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - prices[i]]+increase[i]*prices[i])
    return dp[round(money,2)]


# You are allowed to change the main function. 

# Do not change the template file name. 

def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


# The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
    
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])/100



# Add your implementation here .... 
    returns = {}
    for i in range(len(prices)):
        returns[prices[i]] = increase[i]*(prices[i])/100


# Add your functions and call them to generate the result. 
    print(f'{max_profit(money, num_houses, prices, increase):.2f}')
    

    
main()
