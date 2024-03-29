"""
1048. Longest String Chain
Solved
Medium
Topics
Companies
Hint
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 
"""



class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chains = {}  # Stores the max chain length for each word
        sorted_words = sorted(words, key=len) # Sort words by length

        for word in sorted_words:
            chains[word] = 1  # Initialize the chain length for the current word
            
            for i in range(len(word)):
                # word = abc, i = 0, word[:i] = "" + word[i+1:] = "bc" = "bc"
                # word = abc, i = 1, word[:i] = "a" + word[i+1:] = "c" = "ac"
                # word = abc, i = 2, word[:i] = "ab" + word[i+1:] = "" = "ab"
                pred = word[:i] + word[i+1:]  # Generate predecessor by removing one character
                if pred in chains:
                    chains[word] = max(chains[word], chains[pred] + 1)

        return max(chains.values())