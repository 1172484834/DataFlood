from PlotTree import plotTree
from ReadFile import readFile
import sys

arr = [['接口: /transport-order', 'ss.change-event.vlms-transport-order-cheng-event'],
       ['ss.change-event.vlms-transport-order-cheng-event', 'ss.incomplete.logistic'],
       ['ss.incomplete.logistic', 'ss.model.logistics'], ['ss.model.logistics', 'ss.incomplete.model-d-status'],
       ['ss.incomplete.model-d-status', 'ss.model.model-d-status'],
       ['ss.model.model-d-status', 's7'], ['s7', 's9'], ['s9', 's10'], ['ss.model.logistics', 'ss.incomplete.calculus']]

arr = readFile().values

father = []
children = []
for i in range(len(arr)):
    father.append(arr[i][0])
    children.append(arr[i][1])

print("father:", father)
print("children:", children)


def findChildrenFlood(root, l):
    while len(root) != 0:
        temp = []
        l.append('-->')
        for i in range(len(root)):
            for j in range(len(father)):
                if root[i] == father[j]:
                    temp.append(children[j])
                    l.append(root[i] + '->' + children[j])
        root = temp


def findFatherFlood(root, l):
    while len(root) != 0:
        temp = []
        l.append('-->')
        for i in range(len(root)):
            for j in range(len(children)):
                if root[i] == children[j]:
                    temp.append(father[j])
                    l.append(father[j] + '->' + root[i])
        root = temp


def findFlood(topic):
    root1 = [topic]
    l1 = [topic]
    findChildrenFlood(root1, l1)
    root2 = [topic]
    l2 = [topic]
    findFatherFlood(root2, l2)
    return l1, l2


def combineResult(list1, list2):
    list1 = list1[2:-1]
    list2 = list2[2:-1][::-1]
    print("s2作为父节点, 关系结构: ", list1)
    print("s2作为子节点，关系结构：", list2)
    list2.append('-->')
    list2.extend(list1)
    print("整体的关系结构：", list2)
    return list2


if len(sys.argv) <= 1:
    print("请指明topic名称")
    exit(0)

topic = sys.argv[1]
l1, l2 = findFlood(topic)
result = combineResult(l1, l2)
plotTree(result, topic)
