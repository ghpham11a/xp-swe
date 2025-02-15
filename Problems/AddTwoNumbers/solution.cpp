#include <iostream>

struct ListNode 
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* solution(ListNode* l1, ListNode* l2) 
{
    ListNode *tempHead = new ListNode();
    ListNode *currHead = tempHead;
    int carry = 0;
    
    while (l1 != NULL || l2 != NULL || carry != 0)
    {
        int valueOne = 0;
        if (l1 != NULL) valueOne = l1->val;
        
        int valueTwo = 0;
        if (l2 != NULL) valueTwo = l2->val;
        
        int currSum = valueOne + valueTwo + carry;
        carry = currSum / 10;
        currHead->next = new ListNode(currSum % 10);
        currHead = currHead->next;
        
        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }
    
    return tempHead->next;
}

int main()
{
    return 0;
}