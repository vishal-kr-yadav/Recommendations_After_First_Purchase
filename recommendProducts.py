import pandas as pd

def userRecommendations(searchItem):

    userItemData = pd.read_csv('userData.csv')

    # Get list of unique items
    itemList = list(set(userItemData["ItemId"].tolist()))

    # Get count of users
    userCount = len(set(userItemData["ItemId"].tolist()))

    # Create an empty data frame to store item affinity scores for items.
    itemAffinity = pd.DataFrame(columns=('item1', 'item2', 'score'))

    rowCount = 0
    for ind1 in range(len(itemList)):

        # Get list of users who bought this item 1.
        item1Users = userItemData[userItemData.ItemId == itemList[ind1]]["UserId"].tolist()
        # Get item 2 - items that are not item 1 or those that are not analyzed already.
        for ind2 in range(ind1, len(itemList)):

            if (ind1 == ind2):
                continue

            # Get list of users who bought item 2
            item2Users = userItemData[userItemData.ItemId == itemList[ind2]]["UserId"].tolist()
            # print("Item 2",item2Users)

            # Find score. Find the common list of users and divide it by the total users.
            commonUsers = len(set(item1Users).intersection(set(item2Users)))
            score = commonUsers / userCount

            # Add a score for item 1, item 2
            itemAffinity.loc[rowCount] = [itemList[ind1], itemList[ind2], score]
            rowCount += 1
            # Add a score for item2, item 1. The same score would apply irrespective of the sequence.
            itemAffinity.loc[rowCount] = [itemList[ind2], itemList[ind1], score]
            rowCount += 1

    # Check final result
    # print(itemAffinity.head())

    recoList = itemAffinity[itemAffinity.item1 == searchItem] \
        [["item2", "score"]] \
        .sort_values("score", ascending=[0])
    print("===",recoList)
    return recoList
searchItem = 5001