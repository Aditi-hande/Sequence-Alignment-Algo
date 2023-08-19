# Sequence-Alignment-Algo
Sequence Alignmnet algorithm with dynamic programming approach and a more space efficient Divide and conquer plus DP approach.

A. Algorithm Description
Suppose we are given two strings 𝑋 and 𝑌, where 𝑋 consists of the sequence of
symbols 𝑥 and consists of the sequence of symbols . 1, 𝑥2 , ... , 𝑥𝑚 𝑌 𝑦1, 𝑦2 , ... , 𝑦𝑛
Consider the sets {1, 2, ... ,𝑚} and {1, 2, ... , 𝑛} as representing the different
positions in the strings 𝑋 and 𝑌, and consider a matching of these sets; Recall that
a matching is a set of ordered pairs with the property that each item occurs in at
most one pair. We say that a matching 𝑀 of these two sets is an alignment if there
are no “crossing” pairs: if (𝑖, 𝑗), (𝑖', 𝑗') ϵ 𝑀 and 𝑖 < 𝑖' , then 𝑗 < 𝑗'. Intuitively,
an alignment gives a way of lining up the two strings, by telling us which pairs of
positions will be lined up with one another.
Our definition of similarity will be based on finding the optimal alignment
between 𝑋 and 𝑌, according to the following criteria. Suppose 𝑀 is a given
alignment between 𝑋 and 𝑌:
1. First, there is a parameter δ that defines a gap penalty. For each 𝑒 > 0
position of 𝑋or 𝑌 that is not matched in 𝑀 — it is a gap — we incur a cost
of δ.
2. Second, for each pair of letters 𝑝, 𝑞 in our alphabet, there is a mismatch
cost of α for lining up with . Thus, for each , we pay the 𝑝𝑞 𝑝 𝑞 (𝑖, 𝑗) ϵ 𝑀
appropriate mismatch cost α for lining up with . One generally 𝑥𝑖𝑦𝑗
𝑥𝑖 𝑦𝑗
assumes that α = 0 for each letter —there is no mismatch cost to line up 𝑝𝑝 𝑝
a letter with another copy of itself—although this will not be necessary in
anything that follows.
3. The cost of 𝑀 is the sum of its gap and mismatch costs, and we seek an
alignment of minimum cost.
