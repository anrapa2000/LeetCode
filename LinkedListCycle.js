class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}


/**
 * @param {ListNode} head
 * @return {boolean}
 */


const node1 = new ListNode(3);
const node2 = new ListNode(2);
const node3 = new ListNode(0);
const node4 = new ListNode(-4);

node1.next = node2;
node2.next = node3;
node3.next = node4;
node4.next = node2;

const head = node1;

const result = hasCycle(head);var hasCycle = function(head) {
    const array = [];
    while(head){
        console.log(head.val)
        console.log(array.includes(head.val))
        if(array.includes(head.val)){
            return true;
        }        
        array.push(head.val)
        head = head.next;
    }
    return false
};