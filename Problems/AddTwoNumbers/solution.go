
type ListNode struct {
	Val int
	Next *ListNode
}
 
func solution(l1 *ListNode, l2 *ListNode) *ListNode {
    tempHead := &ListNode{}
    currHead := tempHead
    carry := 0
    
    for l1 != nil || l2 != nil || carry != 0 {
        
        l1Value := 0
        if l1 != nil {
            l1Value = l1.Val
        }
        
        l2Value := 0
        if l2 != nil {
            l2Value = l2.Val
        }
        
        currSum := l1Value + l2Value + carry
        carry = currSum / 10
        currHead.Next = &ListNode{currSum % 10, nil}
        currHead = currHead.Next
        
        if l1 != nil {
            l1 = l1.Next
        }
        
        if l2 != nil {
            l2 = l2.Next
        }
    }
    
    return tempHead.Next
}