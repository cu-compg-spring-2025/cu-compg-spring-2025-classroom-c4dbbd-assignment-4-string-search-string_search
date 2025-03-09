# string_search  
Empirical comparison of string search methods.

## Usage  
usage: string_search.py [-h] --text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE
--pattern_size PATTERN_SIZE [--rounds ROUNDS]
--out_file OUT_FILE [--width WIDTH]
[--height HEIGHT] [--algorithm {naive, boyer-moore}]

optional arguments:
-h, --help Show this help message and exit
--text_range TEXT_RANGE TEXT_RANGE TEXT_RANGE
Specify the text size range (start, stop, step)
--pattern_size PATTERN_SIZE
Specify the size of the pattern to search
--rounds ROUNDS
Number of times to run each algorithm (default: 10)
--out_file OUT_FILE
Output file for saving the performance plot
--width WIDTH
Width of the plot in inches (default: 8)
--height HEIGHT
Height of the plot in inches (default: 5)
--algorithm {naive, boyer-moore}
Choose between naive and Boyer-Moore string search algorithms (default: naive)

sql
Copy
Edit

## Examples  

### Naive String Search  
The naive string search algorithm checks every possible alignment of the pattern within the text, making it straightforward but inefficient for large inputs. This example runs the naive string search on randomly generated DNA sequences:  
python src/string_search.py \
--text_range 100 10000 100 \
--pattern_size 100 \
--rounds 10 \
--algorithm naive \
--out_file doc/naive_search.png

sql
Copy
Edit
<center><img src="/doc/naive_search.png" width="600"/></center>  

### Boyer-Moore String Search  
The Boyer-Moore algorithm uses heuristics to skip unnecessary comparisons, making it significantly faster for large texts. This example runs the Boyer-Moore search with the same input parameters:  
python src/string_search.py \
--text_range 100 10000 100 \
--pattern_size 100 \
--rounds 10 \
--algorithm boyer-moore \
--out_file doc/boyer_moore_search.png

sql
Copy
Edit
<center><img src="/doc/boyer_moore_search.png" width="600"/></center>  

## Naive String Search  
The naive string search algorithm works by checking every possible alignment of the pattern $P$ within the text $T$:  

- **Algorithm Steps:**  
  - Start at the first position in $T$  
  - Compare each character of $P$ with the corresponding characters in $T$  
  - If all characters match, record the match position  
  - If a mismatch occurs, shift $P$ by one position and repeat  
  - Continue until $P$ has been compared at all valid positions in $T$  

- **Complexity:**  
  - **Worst-case runtime:** $O(nm)$, where $n$ is the length of $T$ and $m$ is the length of $P$  
  - **Memory usage:** $O(1)$, since only a few counters are maintained  

- **Advantages:**  
  - Simple to implement  
  - Works well for small inputs  

- **Disadvantages:**  
  - Inefficient for long texts  
  - Redundant comparisons slow down execution  

The naive method is useful for small-scale problems but is outperformed by more op
