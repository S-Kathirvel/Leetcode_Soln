class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrinks = numBottles

        while numBottles >= numExchange:
            totalDrinks += (numBottles // numExchange)
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)

        return totalDrinks
            
