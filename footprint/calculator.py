"""Calculates carbon footprint scores for individual categories and overall."""

class Calculator:
    
    def __init__(self, list):
        self.transportation_score = 0
        self.max_transportation = 55
        self.waste_score = 0
        self.max_waste = 110
        self.utility_score = 0
        self.max_utility = 30
        self.answers = list
        self.tiers = {}

        transportation_list = list[:3]
        waste_list = list[3:9]
        utility_list = list[9:12]
        self.transportation(transportation_list)
        self.waste(waste_list)
        self.utility(utility_list)

        self.total_score = self.transportation_score + self.waste_score + self.utility_score
        self.max_total = self.max_transportation + self.max_waste + self.max_utility

    def transportation(self, list):
        """
        Personal/public/flights and miles per year
        """
        # miles of car usage per year
        if list[0] > 15000:
            self.transportation_score += 15
        elif list[0] > 10000:
            self.transportation_score += 10
        elif list[0] > 1000:
            self.transportation_score += 6
        elif list[0] > 0:
            self.transportation_score += 4
        
        # miles of public transportation usage per year
        if list[1] > 20000:
            self.transportation_score += 20
        elif list[1] > 15000:
            self.transportation_score += 10
        elif list[1] > 10000:
            self.transportation_score += 6
        elif list[1] > 1000:
            self.transportation_score += 4
        elif list[1] > 0:
            self.transportation_score += 2

        # flight distance per year
        if list[2] == 0:
            self.transportation_score += 2
        elif list[2] == 1:
            self.transportation_score += 6
        elif list[2] == 2:
            self.transportation_score += 20
    
    def get_transportation(self):
        return '%.2f'%(float(self.transportation_score) / self.max_transportation * 100)

    def waste(self, list):
        """
        Eating meat???, household purchases????, trash cans per week, types of waste recycled
        """
        # Meat per week
        if list[0] == 7:
            self.waste_score += 10
        elif list[0] > 2:
            self.waste_score += 8
        elif list[0] > 0:
            self.waste_score += 5

        # Vegan y/n
        if list[1] == 1:
            self.waste_score += 2
        elif list[1] == 0 and list[0] == 0:
            self.waste_score += 4

        # Diet type (prepackaged, fresh, mix)
        if list[2] == 0:
            self.waste_score += 12
        elif list[2] == 1:
            self.waste_score += 6
        elif list[2] == 2:
            self.waste_score += 2

        # Household purchases per year
        if list[3] > 7:
            self.waste_score += 10
        elif list[3] > 5:
            self.waste_score += 8
        elif list[3] > 3:
            self.waste_score += 6
        elif list[3] > 0:
            self.waste_score += 4
        else:
            self.waste_score += 2
        
        # Trash cans filled per week
        if list[4] >= 4:
            self.waste_score += 50
        elif list[4] == 3:
            self.waste_score += 40
        elif list[4] == 2:
            self.waste_score += 30
        elif list[4] == 1:
            self.waste_score += 20
        else:
            self.waste_score += 5
        
        # Types of waste recycled:
        self.waste_score += 24
        self.waste_score -= 4 * list[5]
    
    def get_waste(self):
        return '%.2f'%(float(self.waste_score) / self.max_waste * 100)

    def utility(self, list):
        """
        People in household, house size, water (dishwasher/laundry)
        """
        # People in household
        if list[0] > 5:
            self.utility_score += 2
        elif list[0] == 5:
            self.utility_score += 4
        elif list[0] == 4:
            self.utility_score += 6
        elif list[0] == 3:
            self.utility_score += 8
        elif list[0] == 2:
            self.utility_score += 10
        elif list[0] == 1:
            self.utility_score += 12
        else:
            self.utility_score += 14
        
        # House size
        if list[1] == 0:
            self.utility_score += 10
        elif list[1] == 1:
            self.utility_score += 7
        elif list[2] == 2:
            self.utility_score += 4
        else:
            self.utility_score += 2
        
        # Water usage per week
        if list[2] > 18:
            self.utility_score += 6
        elif list[2] > 8:
            self.utility_score += 4
        elif list[2] >= 1:
            self.utility_score += 1

    def get_utility(self):
        return '%.2f'%(float(self.utility_score) / self.max_utility * 100)

    def tier(self):
        percent = self.get_transportation()
        tier(percent, "transportation")
        percent = self.get_waste()
        tier(percent, "waste")
        percent = self.get_utility()
        tier(percent, "utility")
        return self.tiers
    
    def tier(self, percentage, category):
        if percent > 75:
            self.tiers[category] = ["poor"]
        elif percent > 50:
            self.tiers[category] = ["average"]
        elif percent > 25:
            self.tiers[category] = ["good"]
        elif percent >= 0:
            self.tiers[category] = ["excellent"]


    # def goal_update(self, ):
    #     """ Completing a goal: subtract points?
    #     """



if __name__ == '__main__':
    
