const reverseList = head => {
    if (!head || !head.next) return head;
    reversed = reverseList(head.next) //recurse to last element then bubble up
    head.next.next = head
    head.next = null
    return reversed
};