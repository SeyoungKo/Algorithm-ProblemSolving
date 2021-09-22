# Count Items Matching a Rule (1773)

class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        '''
        :param items: list
        :param ruleKey: string
        :param ruleValue: string
        :return: int
        '''
        count = 0
        rule_type = {'type': '', 'color': '', 'name': '', ruleKey: ruleValue}

        for item in items:
            for i, item in enumerate(item):
                if list(rule_type).index(ruleKey) == i and rule_type[ruleKey] == item:
                    count += 1
        return count

if __name__ == '__main__':
    # items = [["phone", "blue", "pixel"],
    #          ["computer", "silver", "lenovo"],
    #          ["phone", "gold", "iphone"]]
    # ruleKey = "color"
    # ruleValue = "silver"

    items = [["phone", "blue", "pixel"], ["computer", "silver", "phone"],
             ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"

    s = Solution()
    print(s.countMatches(items, ruleKey, ruleValue))