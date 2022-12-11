from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/11.in") #(ANS1=10605,ANS2=2713310158)
fin = (Path(__file__).parent / "in/11.in")

number_monkeys = 0

items_org = []
operations_org = []
test_vals_org = []
actions_org = []
with open(fin, "r") as f:
    data = f.read().split("\n\n")    
    
    number_monkeys = len(data)

    for x in data:
        _, item, operation, test, true_action, false_action = x.split("\n")

        item = item.replace("  Starting items: ","")
        items_org.append([int(a) for a in item.split(", ")])

        operation = operation.replace("  Operation: new = old ","")
        operations_org.append([operation[0],operation[2:]])

        test = test.replace("  Test: divisible by ","")
        test_vals_org.append(int(test))

        true_action = int(true_action.replace("   If true: throw to monkey ",""))
        false_action = int(false_action.replace("   If false: throw to monkey ",""))
        actions_org.append([true_action,false_action])

################ Common Function #################



################ Part 1 #################

items = deepcopy(items_org)
operations = deepcopy(operations_org)
test_vals = deepcopy(test_vals_org)
actions = deepcopy(actions_org)

rounds = 20
inspections = [0] * number_monkeys

for _ in range(rounds):
    for i in range(number_monkeys):
        while len(items[i]) > 0:
            item_under_inspection = items[i].pop(0)
            if operations[i][1] == "old":
                operation_val = item_under_inspection
            else:
                operation_val = int(operations[i][1])
            if operations[i][0] == "*":
                item_under_inspection *= operation_val
            else: #operation is +
                item_under_inspection += operation_val
            
            item_under_inspection = int(item_under_inspection // 3)

            if (item_under_inspection % test_vals[i]) == 0:
                items[actions[i][0]].append(item_under_inspection)
            else:
                items[actions[i][1]].append(item_under_inspection)
            
            inspections[i] += 1

inspections.sort()

print('ans1:',inspections[-1] * inspections[-2])

################ Part 2 #################

items = deepcopy(items_org)
operations = deepcopy(operations_org)
test_vals = deepcopy(test_vals_org)
actions = deepcopy(actions_org)

rounds = 10000
inspections = [0] * number_monkeys

lcm = 1
for val in test_vals:
    lcm *= val

for _ in range(rounds):
    for i in range(number_monkeys):
        while len(items[i]) > 0:
            item_under_inspection = items[i].pop(0)
            if operations[i][1] == "old":
                operation_val = item_under_inspection
            else:
                operation_val = int(operations[i][1])
            if operations[i][0] == "*":
                item_under_inspection *= operation_val
            else: #operation is +
                item_under_inspection += operation_val

            item_under_inspection = (item_under_inspection % lcm)
            
            if (item_under_inspection % test_vals[i]) == 0:
                items[actions[i][0]].append(item_under_inspection)
            else:
                items[actions[i][1]].append(item_under_inspection)
            
            inspections[i] += 1

inspections.sort()

print('ans2:',inspections[-1] * inspections[-2])

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))