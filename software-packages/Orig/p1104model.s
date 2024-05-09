@ p1104model.s
          .text
          .global _start
_start:
          ldr r1, anumber    @ get address of number
          ldr r0, [r1]       @ get first number 
          ldr r2, [r1, #4]   @ get second number
          add r0, r0, r2     @ add second number
          ldr r2, [r1, #8]   @ get third number
          add r0, r0, r2     @ add third number
          ldr r2, [r1, #12]  @ get fourth number
          add r0, r0, r2     @ add fourth number
          ldr r2, [r1, #16]  @ get fifth number
          add r0, r0, r2     @ add fifth number
          mov r7, #1
          svc 0
anumber:  .word number
          .data
number:   .word 22, 5, 2, 7, 1
