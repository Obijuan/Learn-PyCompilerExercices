@ p1101model.s
          .text
          .global _start
_start:   mov r1, #1       @ move 1 into r1
          mov r2, #2       @ move 2 into r2
          add r0, r1, r2   @ add 1 and 2, result into r0
          mov r3, #3       @ move 3 into r3
          add r0, r0, r3   @ add previous sum and r3, result into r0
          mov r7, #1       @ terminate
          svc 0
