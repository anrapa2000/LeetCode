/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    hash1 = {}
    hash2 = {}
    for(let i = 0;i<s.length; i++){
        if(hash1[s[i]]){
            hash1[s[i]]++
        } else {
            hash1[s[i]] = 1
        }
    }
    for(let j = 0;j<t.length; j++){
        if(hash2[t[j]]){
            hash2[t[j]]++
        } else {
            hash2[t[j]] = 1
        }
    }
    for(let key in hash1){
        if(hash1[key] !== hash2[key]){
            return false
        }
    }
    for(let key2 in hash2){
        console.log(key2)
        if(hash2[key2] !== hash1[key2]){
            return false
        }
    }
    return true
};

console.log(isAnagram("a", "ab")) // true