// 20. Valid Parentheses
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
 
// Example 1:

// Input: s = "()"

// Output: true

// Example 2:

// Input: s = "()[]{}"

// Output: true

// Example 3:

// Input: s = "(]"

// Output: false

// Example 4:

// Input: s = "([])"

// Output: true

// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'.

var isValid = function(s) {
    let stack = [];
    const output = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    if(s.length <= 1){
        return false
    }
    for(let char of s){
        if(output[char]){
            stack.push(char)
        }
        else {
            const openBracket = stack.pop()
            console.log(char, output[openBracket])
            if(char !== output[openBracket])
                return false
        }
    }
    return stack.length === 0 ? true : false
};

const string = isValid("((");
console.log(string)