# Sudoku Solver

### This solver will be based on the backtracking algorihm
##### It will also have import refinements, those being:
- Active generation of valid options
  - In typical solutions every number (1-9) is tested
  - Only valid options for that cell be used
- Simple elimination
  - In cases where there is only one valid option, it will fill that value in
- Modular elimination techniques
  - Dirty cell finding techniques to reduce possible options can easily be worked into the cell options generator


# To do:
- Use opencv2 to scan puzzles from an image
