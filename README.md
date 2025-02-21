string_search
Empirical comparison of string search methods.

Usage
sql
Copy
Edit
usage: string_search.py [-h] --text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE  
                        --pattern_size PATTERN_SIZE [--rounds ROUNDS]  
                        --out_file OUT_FILE [--width WIDTH]  
                        [--height HEIGHT] [--algorithm {naive, boyer-moore}]  

optional arguments:  
  -h, --help            show this help message and exit  
  --text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE  
                        Text size parameters (start stop step)  
  --pattern_size PATTERN_SIZE  
                        Pattern size  
  --rounds ROUNDS       Number of rounds to run each algorithm (default: 10)  
  --out_file OUT_FILE   File to save plot to  
  --width WIDTH         Width of plot in inches (default: 8)  
  --height HEIGHT       Height of plot in inches (default: 5)  
  --algorithm {naive, boyer-moore}  
                        Choose between the naive and Boyer-Moore string search algorithms (default: naive)
Examples
Naive String Search
css
Copy
Edit
python src/string_search.py \  
    --text_range 100 10000 100 \  
    --pattern_size 100 \  
    --rounds 1 \  
    --algorithm naive \  
    --out_file doc/naive_search.png
<center><img src="/doc/naive_search.png" width="600"/></center>
Boyer-Moore String Search
css
Copy
Edit
python src/string_search.py \  
    --text_range 100 10000 100 \  
    --pattern_size 100 \  
    --rounds 1 \  
    --algorithm boyer-moore \  
    --out_file doc/boyer_moore_search.png
<center><img src="/doc/boyer_moore_search.png" width="600"/></center>
Summary of Results
The naive string search algorithm has a linear runtime complexity and constant memory usage.
The Boyer-Moore algorithm significantly improves runtime by skipping unnecessary comparisons, especially for long text sizes, resulting in sublinear average-case performance.
Empirical results show that Boyer-Moore outperforms the naive approach for large texts, making it more efficient for DNA sequence searches and other large-scale pattern matching tasks.










Search

Reason

ChatGPT can make mistakes. Check
