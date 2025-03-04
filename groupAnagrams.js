/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let map = {};
    let result = [];
    for(let i = 0; i< strs.length; i++){
        const word = strs[i];
        strs[i] = strs[i].split('').sort();
        if(map[strs[i]]){
            map[strs[i]].push(word);
        }
        else {
            map[strs[i]] = [word];
        }
    }
    for(let key in map){
        result.push(map[key]);
    }
    return result;
};

groupAnagrams(["eat","tea","tan","ate","nat","bat"
])