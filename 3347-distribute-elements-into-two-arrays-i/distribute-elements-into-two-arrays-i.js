/**
 * @param {number[]} nums
 * @return {number[]}
 */
var resultArray = function(nums) {
    let arr1 = [nums[0]];
    let arr2 = [nums[1]];
    let i = 2;
    let n = nums.length;
    while (i<n){
        if (arr1.at(-1)>arr2.at(-1)) arr1.push(nums[i++])
        else arr2.push(nums[i++]);
    }
    return arr1.concat(arr2);
};