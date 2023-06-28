[problem](https://cses.fi/problemset/task/1084/)

The main idea here it to start alloting smallest apartments to smallest applicants. From this we can conclude that this is a sorting problem.

    Firt sort both available apartments and requirements in increasing order

now try to assign smallest apartment to smallest applicant.

now there are various possibilities

    1) The apartment size is within the require limit. If that so, then simply move to next applicant and next apartment.
    Also increment your answer since this apartment was alloted to current applicant. 

    2) The apartment size is even bigger than maximum requirement. 
    In this case for sure this apartment can't be alloted to current applicant. Plus next apartments will be even bigger than this one so there is no way this applicant will get a match in future apartments.
    hence since we can't satify requirement of current applicant. we move to next applicant.

    3) If none of the above cases are true this means apartment size is even lesser than minimum requirement. In this case we move to next apartment in hope of bigger apartment for our applicant. 


time

for sorting **nlog(n) + mlog(m)**

for algorithm **O(min(n,m))**