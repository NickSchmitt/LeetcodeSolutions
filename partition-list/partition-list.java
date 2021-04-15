class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode lesser = new ListNode(0), greater = new ListNode(0),
                 lesserHead = lesser, greaterHead = greater, curr = head;
        while (curr != null) {
            if (curr.val < x) {
                lesserHead.next = curr;
                lesserHead = curr;
            } else {
                greaterHead.next = curr;
                greaterHead = curr;
            }
            curr = curr.next;
        }
        lesserHead.next = greater.next;
        greaterHead.next = null;
        return lesser.next;
    }
}