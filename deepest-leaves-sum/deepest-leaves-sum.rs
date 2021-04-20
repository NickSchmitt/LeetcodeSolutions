// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        
        // init queue and push root
        let mut queue = VecDeque::new();
        if let Some(root) = root {
            queue.push_back(root);
        }
        
        let mut row_sum = 0;
        
        while !queue.is_empty(){
            
            // reset row sum
            row_sum = 0;
            for _ in 0..queue.len(){
                if let Some(node) = queue.pop_front() {
                    // accumulate row sum until queue.len()
                    row_sum += node.borrow().val;
                    if let Some(left) = node.borrow_mut().left.take() {
                        queue.push_back(left);
                    }
                    if let Some(right) = node.borrow_mut().right.take() {
                        queue.push_back(right);
                    }
                }
            }
            
        }
        row_sum
    }
}